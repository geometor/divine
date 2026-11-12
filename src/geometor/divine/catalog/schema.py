"""Data schemas and exact symbolic certification for the Golden Ratio Catalog.

Every cataloged construction in :mod:`geometor.divine.catalog` returns an exact
symbolic :class:`~geometor.model.Model` together with a verified
:class:`GoldenCertificate` recording exact SymPy lengths, Rational Trigonometry
quadrances, Lemoine *Géométrographie* step metrics, algebraic number field
membership, and all golden sections and chains discovered automatically by
:mod:`geometor.divine.golden`.
"""

from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass

import sympy as sp
import sympy.geometry as spg
from geometor.model import Model, canonicalize_golden, clean_expr, quadrance, zero_test

from ..golden import find_chains_in_model


@dataclass(frozen=True)
class GeometrographieStats:
    """Constructive step metrics in the tradition of Émile Lemoine's *Géométrographie*."""

    given_points: int
    constructed_lines: int
    constructed_circles: int
    constructed_segments: int
    constructed_polygons: int
    elementary_loci: int
    lemoine_simplicity: int


@dataclass(frozen=True)
class DetectedSection:
    """An exact collinear golden section discovered by :mod:`geometor.divine.golden`."""

    points: tuple[str, str, str]
    long_segment: tuple[str, str]
    short_segment: tuple[str, str]
    q_long: sp.Expr
    q_short: sp.Expr


@dataclass(frozen=True)
class DetectedChain:
    """A connected chain of exact collinear golden sections."""

    points: tuple[str, ...]
    section_count: int
    flow: str


@dataclass(frozen=True)
class GoldenCertificate:
    """Machine-verified exact symbolic certificate for a cataloged construction."""

    slug: str
    catalog_code: str
    family_slug: str
    title: str
    primary_long: tuple[str, str]
    primary_short: tuple[str, str]
    primary_collinear: tuple[str, str, str]
    length_long: sp.Expr
    length_short: sp.Expr
    ratio_expr: sp.Expr
    q_long: sp.Expr
    q_short: sp.Expr
    quadrance_ratio: sp.Expr
    number_field: str
    number_field_text: str
    stats: GeometrographieStats
    detected_sections: tuple[DetectedSection, ...]
    detected_chains: tuple[DetectedChain, ...]


@dataclass(frozen=True)
class ConstructionResult:
    """Raw output returned by an individual symbolic construction builder."""

    model: Model
    primary_long: tuple[str, str]
    primary_short: tuple[str, str]
    primary_collinear: tuple[str, str, str]


@dataclass(frozen=True)
class FamilySpec:
    """Metadata describing one of the seven geometric families in the catalog."""

    slug: str
    code_prefix: str
    order: int
    title: str
    short_title: str
    subtitle: str
    summary: str
    overview_rst: str


@dataclass(frozen=True)
class ConstructionSpec:
    """Complete catalog specification for a single Golden Ratio construction or theorem."""

    slug: str
    catalog_code: str
    family_slug: str
    order: int
    title: str
    short_title: str
    discoverers: tuple[str, ...]
    year: str
    citations: tuple[str, ...]
    ctk_url: str
    ctk_title: str
    number_field: str
    number_field_text: str
    enunciation: str
    given_prose: str
    steps_prose: tuple[str, ...]
    proof_prose: str
    notes_prose: str
    terms: tuple[str, ...]
    builder: Callable[[], ConstructionResult]
    svg_bbox: tuple[float, float, float, float] | None = None


def count_geometrographie(model: Model) -> GeometrographieStats:
    """Compute Euclidean locus counts and Lemoine simplicity metrics for ``model``."""
    given_pts = sum(
        1 for pt in model.points if not model[pt].guide and "given" in model[pt].classes
    )
    lines = sum(1 for ln in model.lines if not model[ln].guide)
    circles = sum(1 for c in model.circles if not model[c].guide)
    segments = sum(1 for s in model.segments if not model[s].guide)
    polygons = sum(1 for p in model.polygons if not model[p].guide)
    loci = lines + circles
    simplicity = 3 * lines + 3 * circles
    return GeometrographieStats(
        given_points=given_pts,
        constructed_lines=lines,
        constructed_circles=circles,
        constructed_segments=segments,
        constructed_polygons=polygons,
        elementary_loci=loci,
        lemoine_simplicity=simplicity,
    )


def _format_chain_flow(points: list[spg.Point2D]) -> str:
    """Compute consecutive segment-length progression symbols (``>``, ``<``, ``=``)."""
    if len(points) < 3:
        return ""
    qs = [
        (float((points[i + 1].x - points[i].x).evalf()) ** 2)
        + (float((points[i + 1].y - points[i].y).evalf()) ** 2)
        for i in range(len(points) - 1)
    ]
    symbols: list[str] = []
    for i in range(len(qs) - 1):
        diff = qs[i] - qs[i + 1]
        if abs(diff) <= 1e-9:
            symbols.append("=")
        elif diff > 0:
            symbols.append(">")
        else:
            symbols.append("<")
    return " ".join(symbols)


def certify_construction(spec: ConstructionSpec) -> tuple[Model, GoldenCertificate]:
    """Execute ``spec.builder()`` and verify its exact symbolic golden certificate."""
    res = spec.builder()
    model = res.model

    # 1. Enforce 0% floating-point contamination across all model points
    for pt in model.points:
        if pt.x.atoms(sp.Float) or pt.y.atoms(sp.Float):
            msg = f"{spec.slug}: Floating-point atom detected in point {model[pt].ID}: ({pt.x}, {pt.y})"
            raise ValueError(msg)

    # 2. Verify primary golden ratio segments symbolically
    u = model.get_element_by_ID(res.primary_long[0])
    v = model.get_element_by_ID(res.primary_long[1])
    w = model.get_element_by_ID(res.primary_short[0])
    z = model.get_element_by_ID(res.primary_short[1])

    q_long = canonicalize_golden(clean_expr(quadrance(u, v)))
    q_short = canonicalize_golden(clean_expr(quadrance(w, z)))
    phi_sym = sp.Rational(1, 2) + sp.sqrt(5) / 2

    if not zero_test(q_long - (phi_sym + 1) * q_short):
        msg = (
            f"{spec.slug}: Primary quadrance ratio failed exact golden test: "
            f"Q({res.primary_long})={q_long}, Q({res.primary_short})={q_short}"
        )
        raise AssertionError(msg)

    len_long = canonicalize_golden(clean_expr(sp.sqrt(q_long)))
    len_short = canonicalize_golden(clean_expr(sp.sqrt(q_short)))
    if float(len_long.evalf()) <= float(len_short.evalf()):
        msg = (
            f"{spec.slug}: Expected primary_long > primary_short, got "
            f"{float(len_long.evalf())} <= {float(len_short.evalf())}"
        )
        raise AssertionError(msg)

    raw_ratio = canonicalize_golden(clean_expr(len_long / len_short))
    if not (
        zero_test(raw_ratio - sp.GoldenRatio)
        or zero_test(q_long - (sp.GoldenRatio + 1) * q_short)
    ):
        msg = f"{spec.slug}: Symbolic ratio {raw_ratio} != GoldenRatio"
        raise AssertionError(msg)

    ratio_expr = sp.GoldenRatio if zero_test(raw_ratio - phi_sym) else raw_ratio
    quadrance_ratio = sp.GoldenRatio + 1

    # 3. Verify primary_collinear points exist and form an exact collinear golden section
    cp0 = model.get_element_by_ID(res.primary_collinear[0])
    cp1 = model.get_element_by_ID(res.primary_collinear[1])
    cp2 = model.get_element_by_ID(res.primary_collinear[2])
    det_col = (cp1.x - cp0.x) * (cp2.y - cp0.y) - (cp1.y - cp0.y) * (cp2.x - cp0.x)
    if not zero_test(det_col):
        msg = f"{spec.slug}: primary_collinear {res.primary_collinear} is not collinear"
        raise AssertionError(msg)
    cq1 = quadrance(cp0, cp1)
    cq2 = quadrance(cp1, cp2)
    cq_hi, cq_lo = (cq1, cq2) if float(cq1.evalf()) >= float(cq2.evalf()) else (cq2, cq1)
    if not zero_test(cq_hi - (phi_sym + 1) * cq_lo):
        msg = f"{spec.slug}: primary_collinear {res.primary_collinear} is not golden"
        raise AssertionError(msg)

    # 4. Run automated geometor.divine golden-section & chain discovery
    sections, chains = find_chains_in_model(model)
    detected_secs: list[DetectedSection] = []
    for sec in sections:
        p0, p1, p2 = sec.points[0], sec.points[1], sec.points[2]
        ids = (model[p0].ID, model[p1].ID, model[p2].ID)
        sq1 = canonicalize_golden(clean_expr(quadrance(p0, p1)))
        sq2 = canonicalize_golden(clean_expr(quadrance(p1, p2)))
        if float(sq1.evalf()) >= float(sq2.evalf()):
            long_seg = (ids[0], ids[1])
            short_seg = (ids[1], ids[2])
            ql, qs = sq1, sq2
        else:
            long_seg = (ids[1], ids[2])
            short_seg = (ids[0], ids[1])
            ql, qs = sq2, sq1
        detected_secs.append(
            DetectedSection(
                points=ids,
                long_segment=long_seg,
                short_segment=short_seg,
                q_long=ql,
                q_short=qs,
            )
        )

    detected_chns: list[DetectedChain] = []
    for chn in chains:
        pts = chn.points
        pt_ids = tuple(model[p].ID for p in pts)
        detected_chns.append(
            DetectedChain(
                points=pt_ids,
                section_count=len(chn.sections),
                flow=_format_chain_flow(pts),
            )
        )

    stats = count_geometrographie(model)

    cert = GoldenCertificate(
        slug=spec.slug,
        catalog_code=spec.catalog_code,
        family_slug=spec.family_slug,
        title=spec.title,
        primary_long=res.primary_long,
        primary_short=res.primary_short,
        primary_collinear=res.primary_collinear,
        length_long=len_long,
        length_short=len_short,
        ratio_expr=ratio_expr,
        q_long=q_long,
        q_short=q_short,
        quadrance_ratio=quadrance_ratio,
        number_field=spec.number_field,
        number_field_text=spec.number_field_text,
        stats=stats,
        detected_sections=tuple(detected_secs),
        detected_chains=tuple(detected_chns),
    )
    return model, cert
