"""Publication-grade interactive ``.euclid-graphic`` SVG renderer for the Golden Ratio Catalog.

Generates crisp, theme-adaptive SVGs directly from exact symbolic
:class:`~geometor.model.Model` instances and :class:`~geometor.divine.catalog.schema.GoldenCertificate`
certificates. Conforms simultaneously to:

1. **Standalone SVG viewing** (embedded ``<style>`` with ``prefers-color-scheme``
   dark/light palettes, ``<defs>`` tick markers ``#geom-tick-1..3``, and luminous
   gold highlighting), and
2. **PHOTON Publish Book Codex interactive figures** (``svg.euclid-graphic``,
   ``#elements``, ``#graphics``, ``#highlights``, ``#points``, ``#labels``,
   3-vertex ``<path>`` segments, ``data-ref``, and ``data-aliases`` consumed by
   ``geometor_interactive.js``).
"""

from __future__ import annotations

import html
import math
import re
from pathlib import Path

import sympy as sp
import sympy.geometry as spg
from geometor.model import Model, zero_test
from geometor.model.sections import Section

from .schema import GoldenCertificate

__all__ = [
    "EMBEDDED_SVG_STYLE",
    "export_catalog_svg",
    "render_catalog_svg",
]

EMBEDDED_SVG_STYLE: str = """
  .euclid-graphic {
    font-family: "Inter", "Segoe UI", system-ui, -apple-system, sans-serif;
  }
  .euclid-graphic .svg-bg { fill: none; }
  .euclid-graphic .geom-circle.conic-curve { fill: none; stroke: #0284c7; stroke-width: 1.85; stroke-opacity: 0.82; }
  .euclid-graphic .geom-circle.aux-circle { fill: none; stroke: #0369a1; stroke-width: 1.35; stroke-dasharray: 5 3.5; stroke-opacity: 0.62; }
  .euclid-graphic .geom-circle.golden-circle { fill: none; stroke: #d4af37; stroke-width: 2.35; stroke-opacity: 0.92; }
  .euclid-graphic .geom-polygon.poly-shape { fill: #0284c7; fill-opacity: 0.07; stroke: #334155; stroke-width: 1.85; stroke-linejoin: round; }
  .euclid-graphic .geom-polygon.golden-poly { fill: #d4af37; fill-opacity: 0.11; stroke: #d4af37; stroke-width: 2.1; stroke-linejoin: round; }
  .euclid-graphic .geom-line { fill: none; stroke: #475569; stroke-width: 1.45; stroke-linecap: round; stroke-opacity: 0.72; }
  .euclid-graphic .geom-line.aux-line { fill: none; stroke: #64748b; stroke-width: 1.2; stroke-dasharray: 5 3.5; stroke-opacity: 0.58; }
  .euclid-graphic .geom-segment.struct-segment { fill: none; stroke: #334155; stroke-width: 1.95; stroke-linecap: round; stroke-opacity: 0.88; }
  .euclid-graphic .geom-segment.aux-segment { fill: none; stroke: #64748b; stroke-width: 1.35; stroke-dasharray: 4.5 3; stroke-linecap: round; stroke-opacity: 0.68; }
  .euclid-graphic .geom-segment.golden-segment { fill: none; stroke: #b45309; stroke-width: 2.8; stroke-linecap: round; stroke-opacity: 0.55; }
  .euclid-graphic .geom-segment.golden-major-glow { fill: none; stroke: #d4af37; stroke-opacity: 0.28; stroke-width: 9.5; stroke-linecap: round; pointer-events: none; }
  .euclid-graphic .geom-segment.golden-major { fill: none; stroke: #d4af37; color: #78350f; stroke-width: 4.3; stroke-linecap: round; }
  .euclid-graphic .geom-segment.golden-minor { fill: none; stroke: #c2410c; color: #7c2d12; stroke-width: 3.7; stroke-linecap: round; }
  .euclid-graphic .geom-overlay { fill: none; stroke: none; stroke-width: 10; stroke-linecap: round; opacity: 0; pointer-events: none; }
  .euclid-graphic .geom-point { fill: #0369a1; stroke: #fafaf9; stroke-width: 1.5; }
  .euclid-graphic .geom-point.given-point { fill: #0f172a; }
  .euclid-graphic .geom-point.golden-point { fill: #d4af37; stroke: #1c1917; stroke-width: 1.7; }
  .euclid-graphic .geom-point-halo { fill: none; stroke: #d4af37; stroke-opacity: 0.55; stroke-width: 1.8; pointer-events: none; }
  .euclid-graphic .geom-label {
    fill: #1c1917;
    font-size: 13.5px;
    font-weight: 600;
    paint-order: stroke fill;
    stroke: #fafaf9;
    stroke-opacity: 0.92;
    stroke-width: 3.6px;
    stroke-linejoin: round;
    user-select: none;
  }
  .euclid-graphic .geom-label-sub { font-size: 10px; font-weight: 600; }
  @media (prefers-color-scheme: dark) {
    .euclid-graphic .geom-circle.conic-curve { stroke: #38bdf8; }
    .euclid-graphic .geom-circle.aux-circle { stroke: #7dd3fc; }
    .euclid-graphic .geom-circle.golden-circle { stroke: #f5c542; }
    .euclid-graphic .geom-polygon.poly-shape { fill: #38bdf8; stroke: #cbd5e1; }
    .euclid-graphic .geom-polygon.golden-poly { fill: #f5c542; stroke: #f5c542; }
    .euclid-graphic .geom-line { stroke: #94a3b8; }
    .euclid-graphic .geom-line.aux-line { stroke: #64748b; }
    .euclid-graphic .geom-segment.struct-segment { stroke: #cbd5e1; }
    .euclid-graphic .geom-segment.aux-segment { stroke: #64748b; }
    .euclid-graphic .geom-segment.golden-segment { stroke: #facc15; }
    .euclid-graphic .geom-segment.golden-major-glow { stroke: #f5c542; stroke-opacity: 0.32; }
    .euclid-graphic .geom-segment.golden-major { stroke: #f5c542; color: #fef3c7; }
    .euclid-graphic .geom-segment.golden-minor { stroke: #fb923c; color: #ffedd5; }
    .euclid-graphic .geom-point { fill: #38bdf8; stroke: #141417; }
    .euclid-graphic .geom-point.given-point { fill: #e2e8f0; }
    .euclid-graphic .geom-point.golden-point { fill: #f5c542; stroke: #141417; }
    .euclid-graphic .geom-point-halo { stroke: #f5c542; }
    .euclid-graphic .geom-label { fill: #f4f4f5; stroke: #141417; }
  }
""".strip()


def _fmt(val: float) -> str:
    if abs(val - round(val)) < 1e-5:
        return str(round(val))
    return f"{val:.2f}".rstrip("0").rstrip(".")


def _esc_attr(val: str) -> str:
    return (
        val.replace("&", "&amp;")
        .replace('"', "&quot;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
    )


def _clip_line_to_rect(
    line: spg.Line,
    xmin: float,
    xmax: float,
    ymin: float,
    ymax: float,
) -> tuple[tuple[float, float], tuple[float, float]] | None:
    a_f = float(line.coefficients[0].evalf())
    b_f = float(line.coefficients[1].evalf())
    c_f = float(line.coefficients[2].evalf())
    eps = 1e-11
    hits: list[tuple[float, float]] = []

    if abs(b_f) > eps:
        for x_edge in (xmin, xmax):
            y_val = -(a_f * x_edge + c_f) / b_f
            if ymin - 1e-7 <= y_val <= ymax + 1e-7:
                hits.append((x_edge, min(max(y_val, ymin), ymax)))

    if abs(a_f) > eps:
        for y_edge in (ymin, ymax):
            x_val = -(b_f * y_edge + c_f) / a_f
            if xmin - 1e-7 <= x_val <= xmax + 1e-7:
                hits.append((min(max(x_val, xmin), xmax), y_edge))

    unique_hits: list[tuple[float, float]] = []
    for hx, hy in hits:
        if not any(math.hypot(hx - ux, hy - uy) < 1e-5 for ux, uy in unique_hits):
            unique_hits.append((hx, hy))

    if len(unique_hits) < 2:
        return None

    best_pair = (unique_hits[0], unique_hits[1])
    best_dist = -1.0
    for i in range(len(unique_hits)):
        for j in range(i + 1, len(unique_hits)):
            d = math.hypot(
                unique_hits[j][0] - unique_hits[i][0],
                unique_hits[j][1] - unique_hits[i][1],
            )
            if d > best_dist:
                best_dist = d
                best_pair = (unique_hits[i], unique_hits[j])
    return best_pair


def _split_point_label(pt_id: str) -> tuple[str, str]:
    m = re.match(r"^([A-Za-z]+)(\d+)$", pt_id)
    if m:
        return (m.group(1), m.group(2))
    return (pt_id, "")


def _point_to_segment_dist(
    px: float,
    py: float,
    x1: float,
    y1: float,
    x2: float,
    y2: float,
) -> float:
    dx = x2 - x1
    dy = y2 - y1
    len_sq = dx * dx + dy * dy
    if len_sq < 1e-9:
        return math.hypot(px - x1, py - y1)
    t = max(0.0, min(1.0, ((px - x1) * dx + (py - y1) * dy) / len_sq))
    proj_x = x1 + t * dx
    proj_y = y1 + t * dy
    return math.hypot(px - proj_x, py - proj_y)


def _segment_aliases(u_id: str, v_id: str, primary_ref: str) -> str:
    cands = [
        f"[ {u_id} {v_id} ]",
        f"[ {v_id} {u_id} ]",
        f"/ {u_id} {v_id} /",
        f"/ {v_id} {u_id} /",
        f"{u_id}{v_id}",
        f"{v_id}{u_id}",
    ]
    out = [c for c in dict.fromkeys(cands) if c != primary_ref]
    return " | ".join(out)


def render_catalog_svg(
    model: Model,
    cert: GoldenCertificate | None = None,
    *,
    graphic_id: str = "g1",
    title: str = "Golden Ratio Construction",
    width: int = 680,
    height: int = 480,
    margin: float = 42.0,
    bbox: tuple[float, float, float, float] | None = None,
    include_guides: bool = False,
) -> str:
    """Render ``model`` and optional ``cert`` into an interactive ``.euclid-graphic`` SVG."""
    visible_points = [
        pt for pt in model.points if include_guides or not model[pt].guide
    ]
    visible_lines = [
        ln for ln in model.lines if include_guides or not model[ln].guide
    ]
    visible_segments = [
        seg for seg in model.segments if include_guides or not model[seg].guide
    ]
    visible_polygons = [
        poly for poly in model.polygons if include_guides or not model[poly].guide
    ]
    visible_circles = [
        cir for cir in model.circles if include_guides or not model[cir].guide
    ]
    visible_sections = [
        sec
        for sec in model
        if isinstance(sec, Section) and (include_guides or not model[sec].guide)
    ]

    if bbox is not None:
        xmin_m, xmax_m, ymin_m, ymax_m = bbox
    elif visible_points or visible_circles:
        xs = [float(p.x.evalf()) for p in visible_points]
        ys = [float(p.y.evalf()) for p in visible_points]
        for cir in visible_circles:
            # Frame primary circles fully; for huge auxiliary compass arcs (>2.6x point span),
            # frame tightly around points + a generous margin so points stay crisp and legible.
            ccx = float(cir.center.x.evalf())
            ccy = float(cir.center.y.evalf())
            cr = float(cir.radius.evalf())
            pt_span = max(
                (max(xs) - min(xs)) if len(xs) >= 2 else 1.0,
                (max(ys) - min(ys)) if len(ys) >= 2 else 1.0,
                1.0,
            )
            if cr <= 2.35 * pt_span or "primary" in model[cir].classes:
                xs.extend((ccx - cr, ccx + cr))
                ys.extend((ccy - cr, ccy + cr))
        xmin_m, xmax_m = min(xs), max(xs)
        ymin_m, ymax_m = min(ys), max(ys)
        span_x = max(xmax_m - xmin_m, 0.8)
        span_y = max(ymax_m - ymin_m, 0.8)
        pad_x = 0.11 * span_x
        pad_y = 0.12 * span_y
        xmin_m -= pad_x
        xmax_m += pad_x
        ymin_m -= pad_y
        ymax_m += pad_y
    else:
        xmin_m, xmax_m, ymin_m, ymax_m = -2.0, 2.0, -2.0, 2.0

    span_x = max(xmax_m - xmin_m, 1e-6)
    span_y = max(ymax_m - ymin_m, 1e-6)
    avail_w = max(width - 2.0 * margin, 120.0)
    avail_h = max(height - 2.0 * margin, 120.0)
    scale = min(avail_w / span_x, avail_h / span_y)

    cx_m = 0.5 * (xmin_m + xmax_m)
    cy_m = 0.5 * (ymin_m + ymax_m)
    cx_s = 0.5 * width
    cy_s = 0.5 * height

    def to_svg(mx: float, my: float) -> tuple[float, float]:
        return (cx_s + (mx - cx_m) * scale, cy_s - (my - cy_m) * scale)

    inset_px = 12.0
    clip_xmin = cx_m - (cx_s - inset_px) / scale
    clip_xmax = cx_m + (width - inset_px - cx_s) / scale
    clip_ymin = cy_m - (height - inset_px - cy_s) / scale
    clip_ymax = cy_m + (cy_s - inset_px) / scale

    pt_svg_coords: dict[spg.Point2D, tuple[float, float]] = {}
    id_to_pt: dict[str, spg.Point2D] = {}
    for pt in visible_points:
        pt_svg_coords[pt] = to_svg(float(pt.x.evalf()), float(pt.y.evalf()))
        pid = model[pt].ID
        if pid:
            id_to_pt[pid] = pt

    drawn_segments_px: list[tuple[float, float, float, float]] = []
    drawn_circles_px: list[tuple[float, float, float]] = []

    # 1. Circles
    circle_elems: list[str] = []
    for cir in visible_circles:
        el = model[cir]
        ccx_s, ccy_s = to_svg(float(cir.center.x.evalf()), float(cir.center.y.evalf()))
        r_px = float(cir.radius.evalf()) * scale
        drawn_circles_px.append((ccx_s, ccy_s, r_px))

        cid = model[cir.center].ID if cir.center in model else ""
        on_ids: list[str] = []
        r_sq = cir.radius**2
        for pt in visible_points:
            pid = model[pt].ID
            if not pid:
                continue
            px_s, py_s = pt_svg_coords[pt]
            if abs(math.hypot(px_s - ccx_s, py_s - ccy_s) - r_px) <= 1.2 and zero_test(
                (pt.x - cir.center.x) ** 2 + (pt.y - cir.center.y) ** 2 - r_sq
            ):
                on_ids.append(pid)

        primary_c_ref = el.ID or (f"( {cid} )" if cid else "")
        c_aliases: list[str] = []
        if cid:
            for cand_c in (f"({cid})", f"( {cid} )"):
                if cand_c != primary_c_ref:
                    c_aliases.append(cand_c)
            for pid in on_ids:
                for cand_cp in (f"( {cid} {pid} )", f"{cid}({pid})"):
                    if cand_cp != primary_c_ref:
                        c_aliases.append(cand_cp)
        if len(on_ids) >= 3:
            cand3 = f"( {on_ids[0]} {on_ids[1]} {on_ids[2]} )"
            if cand3 != primary_c_ref:
                c_aliases.append(cand3)

        css_cls = "geom-circle conic-curve"
        if "golden" in el.classes:
            css_cls = "geom-circle golden-circle"
        elif "auxiliary" in el.classes or "compass" in el.classes:
            css_cls = "geom-circle aux-circle"

        c_ref_attr = f' data-ref="{_esc_attr(primary_c_ref)}"' if primary_c_ref else ""
        c_alias_attr = (
            f' data-aliases="{_esc_attr(" | ".join(dict.fromkeys(c_aliases)))}"'
            if c_aliases
            else ""
        )
        eq_str = str(cir.equation())
        circle_elems.append(
            f'      <circle class="{css_cls}" cx="{_fmt(ccx_s)}" cy="{_fmt(ccy_s)}" '
            f'r="{_fmt(r_px)}"{c_ref_attr}{c_alias_attr} fill="none">'
            f"<title>{html.escape(primary_c_ref)}: {html.escape(eq_str)} = 0</title></circle>"
        )

    # 2. Polygons
    polygon_elems: list[str] = []
    for poly in visible_polygons:
        el = model[poly]
        pts_attr = " ".join(
            f"{_fmt(to_svg(float(v.x.evalf()), float(v.y.evalf()))[0])},"
            f"{_fmt(to_svg(float(v.x.evalf()), float(v.y.evalf()))[1])}"
            for v in poly.vertices
        )
        vert_ids = [model[v].ID for v in poly.vertices if v in model and model[v].ID]
        for idx_v in range(len(poly.vertices)):
            v1 = poly.vertices[idx_v]
            v2 = poly.vertices[(idx_v + 1) % len(poly.vertices)]
            sx1, sy1 = to_svg(float(v1.x.evalf()), float(v1.y.evalf()))
            sx2, sy2 = to_svg(float(v2.x.evalf()), float(v2.y.evalf()))
            drawn_segments_px.append((sx1, sy1, sx2, sy2))

        poly_ref = f"< {' '.join(vert_ids)} >" if vert_ids else el.ID
        p_aliases: list[str] = []
        if el.ID and el.ID != poly_ref:
            p_aliases.append(el.ID)
        if vert_ids:
            joined = "".join(vert_ids)
            p_aliases.extend([joined, f"<{joined}>"])
        p_cls = "geom-polygon golden-poly" if "golden" in el.classes else "geom-polygon poly-shape"
        p_alias_attr = (
            f' data-aliases="{_esc_attr(" | ".join(dict.fromkeys(p_aliases)))}"'
            if p_aliases
            else ""
        )
        polygon_elems.append(
            f'      <polygon class="{p_cls}" points="{pts_attr}" '
            f'data-ref="{_esc_attr(poly_ref)}"{p_alias_attr} />'
        )

    # 3. Infinite lines
    line_elems: list[str] = []
    for ln in visible_lines:
        clipped = _clip_line_to_rect(ln, clip_xmin, clip_xmax, clip_ymin, clip_ymax)
        if clipped is None:
            continue
        (mx1, my1), (mx2, my2) = clipped
        sx1, sy1 = to_svg(mx1, my1)
        sx2, sy2 = to_svg(mx2, my2)
        smx, smy = 0.5 * (sx1 + sx2), 0.5 * (sy1 + sy2)
        drawn_segments_px.append((sx1, sy1, sx2, sy2))

        el = model[ln]
        l_cls = "geom-line aux-line" if "auxiliary" in el.classes else "geom-line"

        incident_ids: list[str] = []
        p1, p2 = ln.p1, ln.p2
        a_l = p1.y - p2.y
        b_l = p2.x - p1.x
        c_l = p1.x * p2.y - p2.x * p1.y
        for pt in visible_points:
            pid = model[pt].ID
            if not pid:
                continue
            px, py = pt_svg_coords[pt]
            if _point_to_segment_dist(px, py, sx1, sy1, sx2, sy2) < 1.2 and zero_test(
                a_l * pt.x + b_l * pt.y + c_l
            ):
                incident_ids.append(pid)

        primary_ref = el.ID or (
            f"[ {incident_ids[0]} {incident_ids[-1]} ]" if len(incident_ids) >= 2 else ""
        )
        aliases: list[str] = []
        for i in range(len(incident_ids)):
            for j in range(i + 1, len(incident_ids)):
                u_id, v_id = incident_ids[i], incident_ids[j]
                for cand in (
                    f"[ {u_id} {v_id} ]",
                    f"[ {v_id} {u_id} ]",
                    f"{u_id}{v_id}",
                    f"{v_id}{u_id}",
                ):
                    if cand != primary_ref:
                        aliases.append(cand)

        ref_attr = f' data-ref="{_esc_attr(primary_ref)}"' if primary_ref else ""
        alias_attr = (
            f' data-aliases="{_esc_attr(" | ".join(dict.fromkeys(aliases)))}"'
            if aliases
            else ""
        )
        eq_str = str(ln.equation())
        line_elems.append(
            f'      <path class="{l_cls}" '
            f'd="M {_fmt(sx1)} {_fmt(sy1)} L {_fmt(smx)} {_fmt(smy)} L {_fmt(sx2)} {_fmt(sy2)}"'
            f'{ref_attr}{alias_attr} fill="none">'
            f"<title>{html.escape(primary_ref)}: {html.escape(eq_str)} = 0</title></path>"
        )

    # 4. Explicit structural segments
    segment_elems: list[str] = []
    for seg in visible_segments:
        el = model[seg]
        p1, p2 = seg.p1, seg.p2
        sx1, sy1 = to_svg(float(p1.x.evalf()), float(p1.y.evalf()))
        sx2, sy2 = to_svg(float(p2.x.evalf()), float(p2.y.evalf()))
        smx, smy = 0.5 * (sx1 + sx2), 0.5 * (sy1 + sy2)
        drawn_segments_px.append((sx1, sy1, sx2, sy2))

        u_id = model[p1].ID if p1 in model else ""
        v_id = model[p2].ID if p2 in model else ""
        primary_ref = el.ID or (f"/ {u_id} {v_id} /" if u_id and v_id else "")
        alias_str = _segment_aliases(u_id, v_id, primary_ref) if u_id and v_id else ""
        s_cls = (
            "geom-segment aux-segment"
            if "auxiliary" in el.classes
            else "geom-segment struct-segment"
        )
        ref_attr = f' data-ref="{_esc_attr(primary_ref)}"' if primary_ref else ""
        alias_attr = f' data-aliases="{_esc_attr(alias_str)}"' if alias_str else ""
        segment_elems.append(
            f'      <path class="{s_cls}" '
            f'd="M {_fmt(sx1)} {_fmt(sy1)} L {_fmt(smx)} {_fmt(smy)} L {_fmt(sx2)} {_fmt(sy2)}"'
            f'{ref_attr}{alias_attr} fill="none" />'
        )

    # 5. Secondary golden sections registered in model
    section_elems: list[str] = []
    for sec in visible_sections:
        if len(sec.points) >= 3:
            el = model[sec]
            p_start, p_end = sec.points[0], sec.points[-1]
            sx1, sy1 = to_svg(float(p_start.x.evalf()), float(p_start.y.evalf()))
            sx2, sy2 = to_svg(float(p_end.x.evalf()), float(p_end.y.evalf()))
            smx, smy = 0.5 * (sx1 + sx2), 0.5 * (sy1 + sy2)
            sec_ids = [model[p].ID for p in sec.points if p in model and model[p].ID]
            sec_ref = f"/ {' '.join(sec_ids)} /" if sec_ids else el.ID
            sec_aliases = "".join(sec_ids)
            alias_attr = f' data-aliases="{_esc_attr(sec_aliases)}"' if sec_aliases else ""
            section_elems.append(
                f'      <path class="geom-segment golden-segment" '
                f'd="M {_fmt(sx1)} {_fmt(sy1)} L {_fmt(smx)} {_fmt(smy)} L {_fmt(sx2)} {_fmt(sy2)}" '
                f'data-ref="{_esc_attr(sec_ref)}"{alias_attr} fill="none" />'
            )

    # 6. Luminous-gold primary GoldenCertificate segments (long = phi, short = 1)
    golden_highlight_elems: list[str] = []
    golden_point_ids: set[str] = set()
    if cert is not None:
        u_id, v_id = cert.primary_long
        w_id, z_id = cert.primary_short
        golden_point_ids.update((u_id, v_id, w_id, z_id))
        golden_point_ids.update(cert.primary_collinear)

        if u_id in id_to_pt and v_id in id_to_pt:
            pu, pv = id_to_pt[u_id], id_to_pt[v_id]
            ux, uy = pt_svg_coords[pu]
            vx, vy = pt_svg_coords[pv]
            mx, my = 0.5 * (ux + vx), 0.5 * (uy + vy)
            drawn_segments_px.append((ux, uy, vx, vy))
            p_ref = f"/ {u_id} {v_id} /"
            p_alias = _segment_aliases(u_id, v_id, p_ref)
            golden_highlight_elems.append(
                f'      <path class="geom-segment golden-major-glow" '
                f'd="M {_fmt(ux)} {_fmt(uy)} L {_fmt(mx)} {_fmt(my)} L {_fmt(vx)} {_fmt(vy)}" fill="none" />'
            )
            golden_highlight_elems.append(
                f'      <path class="geom-segment golden-major" '
                f'd="M {_fmt(ux)} {_fmt(uy)} L {_fmt(mx)} {_fmt(my)} L {_fmt(vx)} {_fmt(vy)}" '
                f'marker-mid="url(#geom-tick-1)" '
                f'data-ref="{_esc_attr(p_ref)}" data-aliases="{_esc_attr(p_alias)}" fill="none">'
                f"<title>Golden major {html.escape(u_id + v_id)} = {html.escape(str(cert.length_long))}</title></path>"
            )

        if w_id in id_to_pt and z_id in id_to_pt:
            pw, pz = id_to_pt[w_id], id_to_pt[z_id]
            wx, wy = pt_svg_coords[pw]
            zx, zy = pt_svg_coords[pz]
            mx, my = 0.5 * (wx + zx), 0.5 * (wy + zy)
            drawn_segments_px.append((wx, wy, zx, zy))
            s_ref = f"/ {w_id} {z_id} /"
            s_alias = _segment_aliases(w_id, z_id, s_ref)
            golden_highlight_elems.append(
                f'      <path class="geom-segment golden-minor" '
                f'd="M {_fmt(wx)} {_fmt(wy)} L {_fmt(mx)} {_fmt(my)} L {_fmt(zx)} {_fmt(zy)}" '
                f'marker-mid="url(#geom-tick-2)" '
                f'data-ref="{_esc_attr(s_ref)}" data-aliases="{_esc_attr(s_alias)}" fill="none">'
                f"<title>Golden minor {html.escape(w_id + z_id)} = {html.escape(str(cert.length_short))}</title></path>"
            )

    # 7. Interactive #highlights overlays for every pair of named visible points
    # so any :g:`AB` segment reference in prose highlights cleanly even when only
    # polygons or circles were drawn.
    overlay_elems: list[str] = []
    named_pts = [pt for pt in visible_points if model[pt].ID]
    if len(named_pts) <= 22:
        for i in range(len(named_pts) - 1):
            p1 = named_pts[i]
            id1 = model[p1].ID
            sx1, sy1 = pt_svg_coords[p1]
            for j in range(i + 1, len(named_pts)):
                p2 = named_pts[j]
                id2 = model[p2].ID
                sx2, sy2 = pt_svg_coords[p2]
                smx, smy = 0.5 * (sx1 + sx2), 0.5 * (sy1 + sy2)
                ov_ref = f"{id1}{id2}"
                ov_alias = f"{id2}{id1} | / {id1} {id2} / | / {id2} {id1} / | [ {id1} {id2} ] | [ {id2} {id1} ]"
                overlay_elems.append(
                    f'      <path class="geom-overlay" '
                    f'd="M {_fmt(sx1)} {_fmt(sy1)} L {_fmt(smx)} {_fmt(smy)} L {_fmt(sx2)} {_fmt(sy2)}" '
                    f'data-ref="{_esc_attr(ov_ref)}" data-aliases="{_esc_attr(ov_alias)}" fill="none" />'
                )

    # 8. Points and collision-avoiding labels
    def _pt_z_key(pt: spg.Point2D) -> int:
        pid = model[pt].ID
        if pid in golden_point_ids:
            return 30
        if "given" in model[pt].classes:
            return 20
        return 10

    sorted_pts = sorted(visible_points, key=_pt_z_key)
    point_elems: list[str] = []
    label_elems: list[str] = []
    placed_label_boxes: list[tuple[float, float, float, float]] = []
    all_pt_px = [pt_svg_coords[p] for p in sorted_pts]

    candidate_angles = [k * (math.pi / 8.0) for k in range(16)]

    for pt in sorted_pts:
        sx, sy = pt_svg_coords[pt]
        if sx < -8 or sx > width + 8 or sy < -8 or sy > height + 8:
            continue

        el = model[pt]
        pid = el.ID
        is_gold_pt = pid in golden_point_ids or "golden" in el.classes
        is_given_pt = "given" in el.classes

        if is_gold_pt:
            css_cls = "geom-point golden-point"
            radius = 4.6
        elif is_given_pt:
            css_cls = "geom-point given-point"
            radius = 4.1
        else:
            css_cls = "geom-point"
            radius = 3.6

        if cert is not None and pid == cert.primary_collinear[1]:
            point_elems.append(
                f'      <circle class="geom-point-halo" cx="{_fmt(sx)}" cy="{_fmt(sy)}" '
                f'r="{_fmt(radius + 4.4)}" fill="none" />'
            )

        x_latex = sp.latex(pt.x)
        y_latex = sp.latex(pt.y)
        tooltip = f"{pid} = ({pt.x}, {pt.y})"
        ref_attr = f' data-ref="{_esc_attr(pid)}"' if pid else ""

        point_elems.append(
            f'      <circle class="{css_cls}" cx="{_fmt(sx)}" cy="{_fmt(sy)}" r="{_fmt(radius)}"'
            f'{ref_attr} data-latex-x="{_esc_attr(x_latex)}" data-latex-y="{_esc_attr(y_latex)}">'
            f"<title>{html.escape(tooltip)}</title></circle>"
        )

        if not pid or "nolabel" in el.classes:
            continue

        base_txt, sub_txt = _split_point_label(pid)
        est_w = 8.8 * len(base_txt) + 6.0 * len(sub_txt) + 4.0
        est_h = 14.0

        best_pos = (sx + 6.0, sy - 9.0)
        best_box = (sx, sy - est_h, sx + est_w, sy)
        best_score = -1e12

        for extra_r in (0.0, 6.5):
            dist_r = radius + 11.5 + extra_r
            for ang in candidate_angles:
                cand_cx = sx + math.cos(ang) * (dist_r + 0.35 * est_w)
                cand_cy = sy + math.sin(ang) * (dist_r + 0.25 * est_h)
                box = (
                    cand_cx - 0.5 * est_w,
                    cand_cy - 0.5 * est_h,
                    cand_cx + 0.5 * est_w,
                    cand_cy + 0.5 * est_h,
                )

                score = -0.35 * extra_r
                if box[0] < 6 or box[2] > width - 6 or box[1] < 6 or box[3] > height - 6:
                    score -= 600.0

                for lx1, ly1, lx2, ly2 in drawn_segments_px:
                    d_line = _point_to_segment_dist(cand_cx, cand_cy, lx1, ly1, lx2, ly2)
                    if d_line < 12.0:
                        score -= (12.0 - d_line) * 16.0

                for ccx_p, ccy_p, r_p in drawn_circles_px:
                    d_arc = abs(math.hypot(cand_cx - ccx_p, cand_cy - ccy_p) - r_p)
                    if d_arc < 10.5:
                        score -= (10.5 - d_arc) * 12.0

                for opx, opy in all_pt_px:
                    d_pt = math.hypot(cand_cx - opx, cand_cy - opy)
                    if d_pt < 15.0:
                        score -= (15.0 - d_pt) * 22.0

                for bx1, by1, bx2, by2 in placed_label_boxes:
                    ox = max(0.0, min(box[2], bx2) - max(box[0], bx1))
                    oy = max(0.0, min(box[3], by2) - max(box[1], by1))
                    if ox > 0 and oy > 0:
                        score -= ox * oy * 7.0

                if score > best_score:
                    best_score = score
                    best_pos = (cand_cx - 0.45 * est_w, cand_cy + 0.34 * est_h)
                    best_box = box

        placed_label_boxes.append(best_box)
        lx, ly = best_pos
        if sub_txt:
            inner_txt = (
                f"{html.escape(base_txt)}"
                f'<tspan class="geom-label-sub" dy="3">{html.escape(sub_txt)}</tspan>'
            )
        else:
            inner_txt = html.escape(base_txt)

        label_elems.append(
            f'      <text class="geom-label" x="{_fmt(lx)}" y="{_fmt(ly)}"'
            f"{ref_attr}>{inner_txt}</text>"
        )

    defs_block = [
        "  <defs>",
        '    <marker id="geom-tick-1" markerUnits="userSpaceOnUse" viewBox="-5 -8 10 16" markerWidth="10" markerHeight="16" orient="auto">',
        '      <line x1="0" y1="-6.2" x2="0" y2="6.2" stroke="currentColor" stroke-width="1.85" stroke-linecap="round" />',
        "    </marker>",
        '    <marker id="geom-tick-2" markerUnits="userSpaceOnUse" viewBox="-7 -8 14 16" markerWidth="14" markerHeight="16" orient="auto">',
        '      <line x1="-2.4" y1="-6.2" x2="-2.4" y2="6.2" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" />',
        '      <line x1="2.4" y1="-6.2" x2="2.4" y2="6.2" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" />',
        "    </marker>",
        '    <marker id="geom-tick-3" markerUnits="userSpaceOnUse" viewBox="-9 -8 18 16" markerWidth="18" markerHeight="16" orient="auto">',
        '      <line x1="-4.4" y1="-6.2" x2="-4.4" y2="6.2" stroke="currentColor" stroke-width="1.65" stroke-linecap="round" />',
        '      <line x1="0" y1="-6.2" x2="0" y2="6.2" stroke="currentColor" stroke-width="1.65" stroke-linecap="round" />',
        '      <line x1="4.4" y1="-6.2" x2="4.4" y2="6.2" stroke="currentColor" stroke-width="1.65" stroke-linecap="round" />',
        "    </marker>",
        "  </defs>",
    ]

    parts = [
        (f'<svg xmlns="http://www.w3.org/2000/svg" class="euclid-graphic" '
        f'viewBox="0 0 {width} {height}" data-graphic-id="{_esc_attr(graphic_id)}" '
        f'role="img" aria-label="{_esc_attr(title)}">'),
        f"  <title>{html.escape(title)}</title>",
        *defs_block,
        "  <style>",
        EMBEDDED_SVG_STYLE,
        "  </style>",
        f'  <rect class="svg-bg" x="0" y="0" width="{width}" height="{height}" rx="6" fill="none" />',
        '  <g id="elements">',
        '    <g id="graphics">',
        *circle_elems,
        *polygon_elems,
        *line_elems,
        *segment_elems,
        *section_elems,
        *golden_highlight_elems,
        "    </g>",
        '    <g id="highlights">',
        *overlay_elems,
        "    </g>",
        '    <g id="points">',
        *point_elems,
        "    </g>",
        '    <g id="labels">',
        *label_elems,
        "    </g>",
        "  </g>",
        "</svg>",
        "",
    ]
    return "\n".join(parts)


def export_catalog_svg(
    model: Model,
    output_path: str | Path,
    cert: GoldenCertificate | None = None,
    *,
    graphic_id: str = "g1",
    title: str = "Golden Ratio Construction",
    width: int = 680,
    height: int = 480,
    margin: float = 42.0,
    bbox: tuple[float, float, float, float] | None = None,
    include_guides: bool = False,
) -> Path:
    """Write an interactive ``.euclid-graphic`` SVG for ``model`` to ``output_path``."""
    target = Path(output_path)
    target.parent.mkdir(parents=True, exist_ok=True)
    svg_text = render_catalog_svg(
        model,
        cert=cert,
        graphic_id=graphic_id,
        title=title,
        width=width,
        height=height,
        margin=margin,
        bbox=bbox,
        include_guides=include_guides,
    )
    target.write_text(svg_text, encoding="utf-8")
    return target.resolve()
