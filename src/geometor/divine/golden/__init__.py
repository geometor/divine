"""Find and analyze exact symbolic golden sections in GEOMETOR models.

This module provides fast numerical pre-filtering paired with 100% exact
Rational Trigonometry symbolic verification (:func:`geometor.model.quadrance`
and :func:`geometor.model.zero_test`) to detect golden sections and chains
across lines and collinear point configurations in :class:`geometor.model.Model`.
"""

from __future__ import annotations

import math
from collections.abc import Sequence
from itertools import combinations
from multiprocessing import Pool, cpu_count

import sympy as sp
import sympy.geometry as spg
from geometor.model import Model, quadrance, zero_test
from geometor.model.chains import Chain
from geometor.model.sections import Section
from geometor.model.utils import sort_points

from .chains import find_chains_in_sections, unpack_chains
from .groups import (
    group_sections_by_points,
    group_sections_by_segments,
    group_sections_by_size,
)
from .ranges import analyze_harmonics, analyze_harmonics_by_segment, check_range

__all__ = [
    "Φ",
    "analyze_harmonics",
    "analyze_harmonics_by_segment",
    "check_range",
    "find_chains_in_model",
    "find_chains_in_sections",
    "find_golden_sections_in_model",
    "find_golden_sections_in_points",
    "group_sections_by_points",
    "group_sections_by_segments",
    "group_sections_by_size",
    "is_section_golden",
    "phi",
    "points_on_line",
    "unpack_chains",
]

Φ = sp.GoldenRatio
phi = sp.Rational(1, 2) + (sp.sqrt(5) / 2)
_PHI_FLOAT = (1.0 + math.sqrt(5.0)) / 2.0
_PHI_SQ_FLOAT = _PHI_FLOAT + 1.0
_FLOAT_TOL = 1e-5


def _point_xy_float(pt: spg.Point2D) -> tuple[float, float]:
    return (float(pt.x.evalf()), float(pt.y.evalf()))


def _are_collinear_exact(p1: spg.Point2D, p2: spg.Point2D, p3: spg.Point2D) -> bool:
    det = (p2.x - p1.x) * (p3.y - p1.y) - (p2.y - p1.y) * (p3.x - p1.x)
    return zero_test(det)


def points_on_line(
    model: Model,
    line: spg.LinearEntity2D,
    *,
    include_guides: bool = False,
    point_floats: dict[spg.Point2D, tuple[float, float]] | None = None,
) -> list[spg.Point2D]:
    """Return all model points incident with ``line`` verified symbolically.

    Uses floating-point line residual screening followed by exact
    :func:`~geometor.model.zero_test` verification on the implicit line
    equation ``a*x + b*y + c = 0``.
    """
    p1, p2 = line.p1, line.p2
    a = p1.y - p2.y
    b = p2.x - p1.x
    c = p1.x * p2.y - p2.x * p1.y

    af = float(a.evalf())
    bf = float(b.evalf())
    cf = float(c.evalf())
    norm = math.hypot(af, bf)
    if norm == 0.0:
        return []

    pts_map = point_floats or {
        pt: _point_xy_float(pt)
        for pt in model.points
        if include_guides or not model[pt].guide
    }

    incident: list[spg.Point2D] = []
    for pt, (xf, yf) in pts_map.items():
        if not include_guides and model[pt].guide:
            continue
        if abs(af * xf + bf * yf + cf) <= 1e-6 * norm and (
            pt == p1 or pt == p2 or zero_test(a * pt.x + b * pt.y + c)
        ):
            incident.append(pt)
    return sort_points(incident)


def is_section_golden(section_points: Sequence[spg.Point2D]) -> bool:
    """Check whether three ordered collinear points form an exact golden section.

    First screens segment quadrances numerically, then proves exact equality
    ``Q_long - (phi + 1) * Q_short == 0`` symbolically via
    :func:`~geometor.model.quadrance` and :func:`~geometor.model.zero_test`.

    Args:
        section_points: Sequence of three ordered collinear points ``(P, Q, R)``.

    Returns:
        bool: ``True`` if ``max(|PQ|, |QR|) / min(|PQ|, |QR|) == phi`` exactly.
    """
    if len(section_points) != 3:
        return False
    p0, p1, p2 = section_points[0], section_points[1], section_points[2]

    x0, y0 = _point_xy_float(p0)
    x1, y1 = _point_xy_float(p1)
    x2, y2 = _point_xy_float(p2)

    q1_f = (x1 - x0) ** 2 + (y1 - y0) ** 2
    q2_f = (x2 - x1) ** 2 + (y2 - y1) ** 2
    if q1_f <= 1e-20 or q2_f <= 1e-20:
        return False

    q_max_f, q_min_f = (q1_f, q2_f) if q1_f >= q2_f else (q2_f, q1_f)
    if abs((q_max_f / q_min_f) - _PHI_SQ_FLOAT) > _FLOAT_TOL:
        return False

    q1 = quadrance(p0, p1)
    q2 = quadrance(p1, p2)
    q_long, q_short = (q1, q2) if q1_f >= q2_f else (q2, q1)
    if zero_test(q_long - (phi + 1) * q_short):
        return True

    return Section(list(section_points)).is_golden


def find_golden_sections_in_points(
    pts: Sequence[spg.Point2D],
    *,
    use_pool: bool = False,
) -> list[Section]:
    """Find all exact golden sections among 3-point combinations of collinear points.

    Args:
        pts: Collinear SymPy points to analyze.
        use_pool: If ``True``, evaluate candidates across a process pool;
            defaults to fast in-process screening + exact algebraic proof.

    Returns:
        list[Section]: Exact golden sections ordered along the line.
    """
    unique_pts = list(dict.fromkeys(pts))
    if len(unique_pts) < 3:
        return []

    sorted_pts = sort_points(unique_pts)
    candidates = [list(combo) for combo in combinations(sorted_pts, 3)]

    if use_pool:
        with Pool(cpu_count()) as pool:
            flags = pool.map(is_section_golden, candidates)
        return [Section(c) for c, ok in zip(candidates, flags) if ok]

    coords = [_point_xy_float(p) for p in sorted_pts]
    n = len(sorted_pts)
    goldens: list[Section] = []

    for i in range(n - 2):
        xi, yi = coords[i]
        pi = sorted_pts[i]
        for j in range(i + 1, n - 1):
            xj, yj = coords[j]
            q1_f = (xj - xi) ** 2 + (yj - yi) ** 2
            if q1_f <= 1e-20:
                continue
            pj = sorted_pts[j]
            q1_sym: sp.Expr | None = None
            for k in range(j + 1, n):
                xk, yk = coords[k]
                q2_f = (xk - xj) ** 2 + (yk - yj) ** 2
                if q2_f <= 1e-20:
                    continue
                q_max_f, q_min_f = (q1_f, q2_f) if q1_f >= q2_f else (q2_f, q1_f)
                if abs((q_max_f / q_min_f) - _PHI_SQ_FLOAT) > _FLOAT_TOL:
                    continue

                pk = sorted_pts[k]
                if q1_sym is None:
                    q1_sym = quadrance(pi, pj)
                q2_sym = quadrance(pj, pk)
                q_long, q_short = (q1_sym, q2_sym) if q1_f >= q2_f else (q2_sym, q1_sym)
                if zero_test(q_long - (phi + 1) * q_short):
                    goldens.append(Section([pi, pj, pk]))
                else:
                    sec = Section([pi, pj, pk])
                    if sec.is_golden:
                        goldens.append(sec)

    return goldens


def _discover_unlined_collinear_sets(
    pts: list[spg.Point2D],
    point_floats: dict[spg.Point2D, tuple[float, float]],
    covered_point_sets: list[frozenset[spg.Point2D]],
) -> list[list[spg.Point2D]]:
    """Find maximal collinear point sets of size >= 3 not already covered by model lines."""
    n = len(pts)
    if n < 3:
        return []

    buckets: dict[tuple[int, int, int], set[int]] = {}
    for i in range(n - 1):
        x1, y1 = point_floats[pts[i]]
        for j in range(i + 1, n):
            x2, y2 = point_floats[pts[j]]
            dx, dy = x2 - x1, y2 - y1
            length = math.hypot(dx, dy)
            if length <= 1e-9:
                continue
            nx, ny = -dy / length, dx / length
            if nx < -1e-9 or (abs(nx) <= 1e-9 and ny < 0):
                nx, ny = -nx, -ny
            d = nx * x1 + ny * y1
            key = (round(nx * 20000), round(ny * 20000), round(d * 20000))
            buckets.setdefault(key, set()).update((i, j))

    maximal_sets: list[list[spg.Point2D]] = []
    seen_exact: list[frozenset[spg.Point2D]] = list(covered_point_sets)

    for idx_set in buckets.values():
        if len(idx_set) < 3:
            continue
        idx_list = sorted(idx_set)
        used: set[tuple[int, int]] = set()
        for a_pos in range(len(idx_list) - 1):
            ia = idx_list[a_pos]
            for b_pos in range(a_pos + 1, len(idx_list)):
                ib = idx_list[b_pos]
                if (ia, ib) in used:
                    continue
                pa, pb = pts[ia], pts[ib]
                collinear_indices = [ia, ib]
                for ic in idx_list:
                    if ic == ia or ic == ib:
                        continue
                    if _are_collinear_exact(pa, pb, pts[ic]):
                        collinear_indices.append(ic)
                for u in collinear_indices:
                    for v in collinear_indices:
                        if u < v:
                            used.add((u, v))
                if len(collinear_indices) >= 3:
                    pt_group = [pts[idx] for idx in collinear_indices]
                    frozen = frozenset(pt_group)
                    if not any(frozen.issubset(existing) for existing in seen_exact):
                        seen_exact.append(frozen)
                        maximal_sets.append(sort_points(pt_group))

    return maximal_sets


def find_golden_sections_in_model(
    model: Model,
    *,
    include_collinear: bool = True,
    include_guides: bool = False,
    use_pool: bool = False,
) -> tuple[list[Section], dict[spg.Line, list[Section]]]:
    """Analyze all lines and collinear point triples in ``model`` for golden sections.

    Args:
        model: The exact symbolic :class:`~geometor.model.Model` to analyze.
        include_collinear: When ``True`` (default), also sweep maximal collinear
            point triples on segments or circle-only configurations without
            requiring an infinite :class:`sympy.geometry.Line` in ``model.lines``.
        include_guides: Whether to include guide points and guide lines.
        use_pool: Whether to use ``multiprocessing.Pool`` per line.

    Returns:
        tuple: ``(sections, sections_by_line)`` containing deduplicated exact
        golden :class:`Section` instances and a mapping from carrier lines to
        their golden sections.
    """
    eligible_pts = [
        pt for pt in model.points if include_guides or not model[pt].guide
    ]
    point_floats = {pt: _point_xy_float(pt) for pt in eligible_pts}

    sections: list[Section] = []
    seen_triples: set[tuple[spg.Point2D, ...]] = set()
    sections_by_line: dict[spg.Line, list[Section]] = {}
    covered_sets: list[frozenset[spg.Point2D]] = []

    # 1. Explicit infinite lines and explicit segment carriers in the model
    explicit_lines = [
        ln for ln in model.lines if include_guides or not model[ln].guide
    ]
    for line in explicit_lines:
        line_pts = points_on_line(
            model, line, include_guides=include_guides, point_floats=point_floats
        )
        if len(line_pts) >= 3:
            covered_sets.append(frozenset(line_pts))
        line_sections = find_golden_sections_in_points(line_pts, use_pool=use_pool)
        sections_by_line[line] = line_sections
        for sec in line_sections:
            key = tuple(sec.points)
            if key not in seen_triples:
                seen_triples.add(key)
                sections.append(sec)

    # 2. Implicit collinear point sets (e.g., segment-only or compass-only models)
    if include_collinear:
        implicit_groups = _discover_unlined_collinear_sets(
            eligible_pts, point_floats, covered_sets
        )
        for pt_group in implicit_groups:
            line_sections = find_golden_sections_in_points(pt_group, use_pool=use_pool)
            if line_sections:
                carrier = spg.Line(pt_group[0], pt_group[-1])
                sections_by_line[carrier] = line_sections
                for sec in line_sections:
                    key = tuple(sec.points)
                    if key not in seen_triples:
                        seen_triples.add(key)
                        sections.append(sec)

    return sections, sections_by_line


def find_chains_in_model(
    model: Model,
    *,
    include_collinear: bool = True,
    include_guides: bool = False,
) -> tuple[list[Section], list[Chain]]:
    """Scan ``model`` for all exact golden sections and connected golden chains."""
    sections, _ = find_golden_sections_in_model(
        model, include_collinear=include_collinear, include_guides=include_guides
    )
    tree = find_chains_in_sections(sections)
    chains = unpack_chains(tree)
    return sections, chains
