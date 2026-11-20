"""Incremental point-birth golden section tracker."""

from __future__ import annotations

import math
from bisect import bisect_left
from dataclasses import dataclass, field

import sympy as sp
import sympy.geometry as spg
from geometor.model import Model, quadrance, zero_test
from geometor.model.sections import Section
from geometor.model.utils import sort_points

_PHI = sp.Rational(1, 2) + (sp.sqrt(5) / 2)
_PHI_FLOAT = (1.0 + math.sqrt(5.0)) / 2.0
_PHI_SQ_FLOAT = _PHI_FLOAT + 1.0
_FLOAT_TOL = 1e-5


def _point_xy_float(pt: spg.Point2D) -> tuple[float, float]:
    return (float(pt.x.evalf()), float(pt.y.evalf()))

__all__ = ["GoldenFieldTracker", "PointImpact"]


@dataclass(frozen=True)
class PointImpact:
    """A golden section brought into the field when a point is added."""

    section: Section
    role: str  # "left" | "middle" | "right" | "line"
    line: spg.Line


@dataclass
class _LineIndex:
    """Cached 1D projection index for a single line."""

    line: spg.Line
    a: sp.Expr
    b: sp.Expr
    c: sp.Expr
    af: float
    bf: float
    cf: float
    norm: float
    x0: float
    y0: float
    ux: float
    uy: float
    pts: list[spg.Point2D] = field(default_factory=list)
    proj: list[float] = field(default_factory=list)
    coords: list[tuple[float, float]] = field(default_factory=list)
    pt_set: set[spg.Point2D] = field(default_factory=set)

    @classmethod
    def from_line(cls, line: spg.Line) -> _LineIndex | None:
        p1, p2 = line.p1, line.p2
        a = p1.y - p2.y
        b = p2.x - p1.x
        c = p1.x * p2.y - p2.x * p1.y
        af, bf, cf = float(a.evalf()), float(b.evalf()), float(c.evalf())
        norm = math.hypot(af, bf)
        if norm == 0.0:
            return None

        x1, y1 = _point_xy_float(p1)
        x2, y2 = _point_xy_float(p2)
        if (x2, y2) < (x1, y1):
            x1, y1, x2, y2 = x2, y2, x1, y1
        dx, dy = x2 - x1, y2 - y1
        dnorm = math.hypot(dx, dy)
        if dnorm == 0.0:
            return None
        return cls(
            line=line,
            a=a,
            b=b,
            c=c,
            af=af,
            bf=bf,
            cf=cf,
            norm=norm,
            x0=x1,
            y0=y1,
            ux=dx / dnorm,
            uy=dy / dnorm,
        )

    def project(self, fx: float, fy: float) -> float:
        return (fx - self.x0) * self.ux + (fy - self.y0) * self.uy

    def is_incident(self, pt: spg.Point2D, fx: float, fy: float) -> bool:
        if abs(self.af * fx + self.bf * fy + self.cf) > 1e-6 * self.norm:
            return False
        if pt == self.line.p1 or pt == self.line.p2:
            return True
        return zero_test(self.a * pt.x + self.b * pt.y + self.c)


class GoldenFieldTracker:
    """Incrementally track golden sections created as points and lines enter a Model."""

    def __init__(self, *, include_guides: bool = False, tag_model: bool = True) -> None:
        self.include_guides = include_guides
        self.tag_model = tag_model
        self._lines: dict[spg.Line, _LineIndex] = {}
        self._seen_triples: set[tuple[spg.Point2D, ...]] = set()
        self.sections: list[Section] = []
        self.impact_by_point: dict[spg.Point2D, list[PointImpact]] = {}

    def attach(self, model: Model) -> GoldenFieldTracker:
        """Register this tracker as ``model``'s analysis hook."""
        model.set_analysis_hook(lambda m, pt: self.on_point_added(m, pt))
        return self

    def _register_section(
        self,
        model: Model,
        owner_pt: spg.Point2D,
        sec_pts: list[spg.Point2D],
        role: str,
        line: spg.Line,
    ) -> None:
        ordered = sort_points(sec_pts)
        key = tuple(ordered)
        if key in self._seen_triples:
            return
        self._seen_triples.add(key)
        sec = Section(ordered)
        self.sections.append(sec)
        self.impact_by_point.setdefault(owner_pt, []).append(
            PointImpact(section=sec, role=role, line=line)
        )
        if self.tag_model:
            model.set_section(sec.points, classes=["golden"])

    def _verify_triple(
        self,
        p0: spg.Point2D,
        p1: spg.Point2D,
        p2: spg.Point2D,
        c0: tuple[float, float],
        c1: tuple[float, float],
        c2: tuple[float, float],
    ) -> bool:
        q1_f = (c1[0] - c0[0]) ** 2 + (c1[1] - c0[1]) ** 2
        q2_f = (c2[0] - c1[0]) ** 2 + (c2[1] - c1[1]) ** 2
        if q1_f <= 1e-20 or q2_f <= 1e-20:
            return False
        q_max_f, q_min_f = (q1_f, q2_f) if q1_f >= q2_f else (q2_f, q1_f)
        if abs((q_max_f / q_min_f) - _PHI_SQ_FLOAT) > _FLOAT_TOL:
            return False
        q1 = quadrance(p0, p1)
        q2 = quadrance(p1, p2)
        q_long, q_short = (q1, q2) if q1_f >= q2_f else (q2, q1)
        if zero_test(q_long - (_PHI + 1) * q_short):
            return True
        return Section([p0, p1, p2]).is_golden

    def _index_new_lines(self, model: Model, exclude_pt: spg.Point2D | None = None) -> None:
        for line in model.lines:
            if line in self._lines:
                continue
            if not self.include_guides and model[line].guide:
                continue
            lidx = _LineIndex.from_line(line)
            if lidx is None:
                continue
            self._lines[line] = lidx
            # Populate existing points already in the model on this line
            for pt in model.points:
                if pt == exclude_pt:
                    continue
                if not self.include_guides and model[pt].guide:
                    continue
                fx, fy = _point_xy_float(pt)
                if lidx.is_incident(pt, fx, fy):
                    self._insert_and_check(model, lidx, pt, fx, fy)

    def _insert_and_check(
        self,
        model: Model,
        lidx: _LineIndex,
        pt: spg.Point2D,
        fx: float,
        fy: float,
    ) -> None:
        if pt in lidx.pt_set:
            return
        s_val = lidx.project(fx, fy)
        pos = bisect_left(lidx.proj, s_val)
        lidx.proj.insert(pos, s_val)
        lidx.pts.insert(pos, pt)
        lidx.coords.insert(pos, (fx, fy))
        lidx.pt_set.add(pt)

        n = len(lidx.pts)
        if n < 3:
            return

        proj = lidx.proj
        pts = lidx.pts
        coords = lidx.coords

        # Role 1: pt is LEFT endpoint (pt, Q, R)
        for j in range(pos + 1, n - 1):
            d1 = proj[j] - s_val
            if d1 <= 1e-10:
                continue
            sj = proj[j]
            for target_d2 in (d1 / _PHI_FLOAT, d1 * _PHI_FLOAT):
                tol = 2.0 * _FLOAT_TOL * target_d2 + 1e-9
                target_s = sj + target_d2
                k = bisect_left(proj, target_s - tol, j + 1)
                while k < n and proj[k] <= target_s + tol:
                    if self._verify_triple(pt, pts[j], pts[k], (fx, fy), coords[j], coords[k]):
                        self._register_section(model, pt, [pt, pts[j], pts[k]], "left", lidx.line)
                    k += 1

        # Role 2: pt is MIDDLE divider (Q, pt, R)
        for i in range(pos):
            d1 = s_val - proj[i]
            if d1 <= 1e-10:
                continue
            for target_d2 in (d1 / _PHI_FLOAT, d1 * _PHI_FLOAT):
                tol = 2.0 * _FLOAT_TOL * target_d2 + 1e-9
                target_s = s_val + target_d2
                k = bisect_left(proj, target_s - tol, pos + 1)
                while k < n and proj[k] <= target_s + tol:
                    if self._verify_triple(pts[i], pt, pts[k], coords[i], (fx, fy), coords[k]):
                        self._register_section(model, pt, [pts[i], pt, pts[k]], "middle", lidx.line)
                    k += 1

        # Role 3: pt is RIGHT endpoint (Q, R, pt)
        for j in range(1, pos):
            d2 = s_val - proj[j]
            if d2 <= 1e-10:
                continue
            sj = proj[j]
            for target_d1 in (d2 / _PHI_FLOAT, d2 * _PHI_FLOAT):
                tol = 2.0 * _FLOAT_TOL * target_d1 + 1e-9
                target_s = sj - target_d1
                i = bisect_left(proj, target_s - tol, 0, j)
                while i < j and proj[i] <= target_s + tol:
                    if self._verify_triple(pts[i], pts[j], pt, coords[i], coords[j], (fx, fy)):
                        self._register_section(model, pt, [pts[i], pts[j], pt], "right", lidx.line)
                    i += 1

    def on_point_added(self, model: Model, pt: spg.Point2D) -> None:
        """Index any new lines and check all new golden sections created by ``pt``."""
        if not self.include_guides and model[pt].guide:
            return
        self._index_new_lines(model, exclude_pt=pt)
        fx, fy = _point_xy_float(pt)
        for lidx in self._lines.values():
            if lidx.is_incident(pt, fx, fy):
                self._insert_and_check(model, lidx, pt, fx, fy)

    def sync(self, model: Model) -> None:
        """Index any lines added after the last point event."""
        self._index_new_lines(model, exclude_pt=None)
