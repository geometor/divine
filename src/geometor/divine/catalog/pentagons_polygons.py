"""Family 05: Regular Pentagons, Pentagrams, Irregular Pentagons & Polygonal Stars.

Catalogs Claudius Ptolemy's *Almagest* pentagon and pentagram, Dao Thanh Oai's
regular pentagon perpendicular, V. V. Prasolov & Bùi Quang Tuân's equi-area
irregular pentagon, and Tran Quang Hung's pentagon-hexagon, six-pentagon star,
and fivefold *Wu Xing* equilateral star theorems.
"""

from __future__ import annotations

import sympy as sp

from .helpers import make_result, new_catalog_model
from .schema import ConstructionResult, ConstructionSpec


def _pentagon_radicals() -> tuple[sp.Expr, sp.Expr, sp.Expr, sp.Expr, sp.Expr]:
    """Return exact coordinated pentagon constants ``(phi, s36, c36, s72, c72)``.

    Writing ``sin(72°) = phi * sin(36°)`` keeps all fivefold coordinates in a
    single quadratic extension over ``Q(phi)``, eliminating independent nested
    radical quotients during symbolic line intersections.
    """
    phi = sp.Rational(1, 2) + sp.sqrt(5) / 2
    s36 = sp.sqrt(10 - 2 * sp.sqrt(5)) / 4
    c36 = phi / 2
    s72 = phi * s36
    c72 = (phi - 1) / 2
    return phi, s36, c36, s72, c72


def _reflect_across_side2(
    wx: sp.Expr,
    wy: sp.Expr,
    ux: sp.Expr,
    uy: sp.Expr,
    vx: sp.Expr,
    vy: sp.Expr,
) -> tuple[sp.Expr, sp.Expr]:
    """Reflect ``(wx, wy)`` across segment ``UV`` when ``Q(U, V) == 4`` (length 2)."""
    dx = vx - ux
    dy = vy - uy
    dot = (wx - ux) * dx + (wy - uy) * dy
    rx = sp.expand(ux + (dot * dx) / 2 - (wx - ux))
    ry = sp.expand(uy + (dot * dy) / 2 - (wy - uy))
    return rx, ry


def build_ptolemy_pentagon_pentagram() -> ConstructionResult:
    """Claudius Ptolemy's Almagest I.10 regular pentagon & pentagram construction."""
    m = new_catalog_model("ptolemy-pentagon-pentagram")
    _phi, s36, c36, s72, c72 = _pentagon_radicals()

    O = m.set_point(0, 0, classes=["given"], ID="O")
    B = m.set_point(1, 0, classes=["given"], ID="B")
    A = m.set_point(-1, 0, ID="A")
    C = m.set_point(0, 1, ID="C")
    M = m.set_point(sp.Rational(1, 2), 0, ID="M")

    c_o = m.construct_circle(O, B, classes=["primary"], ID="cO")
    _ = c_o
    ln_ab = m.construct_line(A, B, classes=["auxiliary"], ID="AB")
    m.construct_segment(O, C, classes=["auxiliary"], ID="OC")

    c_mc = m.construct_circle(M, C, classes=["compass"], ID="cMC")
    E = m.intersect(c_mc, ln_ab, between=(A, O), classes=["golden"], ID="E")
    m.construct_segment(C, E, classes=["auxiliary"], ID="CE")

    # Inscribed regular pentagon C P1 P2 P3 P4 of side |CE| = 2 * s36
    P1 = m.set_point(-s72, c72, ID="P1")
    P2 = m.set_point(-s36, -c36, ID="P2")
    P3 = m.set_point(s36, -c36, ID="P3")
    P4 = m.set_point(s72, c72, ID="P4")
    m.construct_polygon([C, P1, P2, P3, P4], ID="CP1P2P3P4")

    # Inscribed regular pentagram diagonals
    ln_p1p4 = m.construct_line(P1, P4, classes=["golden"], ID="P1P4")
    ln_cp2 = m.construct_line(C, P2, classes=["auxiliary"], ID="CP2")
    ln_cp3 = m.construct_line(C, P3, classes=["auxiliary"], ID="CP3")
    m.construct_segment(P1, P3, classes=["auxiliary"], ID="P1P3")
    m.construct_segment(P2, P4, classes=["auxiliary"], ID="P2P4")

    K1 = m.intersect(ln_p1p4, ln_cp2, classes=["golden"], ID="K1")
    m.intersect(ln_p1p4, ln_cp3, classes=["golden"], ID="K2")
    _ = K1

    return make_result(m, ("P1", "K2"), ("K2", "P4"), ("P1", "K2", "P4"))


def build_dao_tran_pentagon_bisector_incircle() -> ConstructionResult:
    """Dao Thanh Oai's perpendicular at a vertex of a regular pentagon."""
    m = new_catalog_model("dao-tran-pentagon-bisector-incircle")
    phi, s36, _c36, _s72, _c72 = _pentagon_radicals()
    phi2 = phi + 1

    A = m.set_point(-1, 0, classes=["given"], ID="A")
    B = m.set_point(1, 0, classes=["given"], ID="B")
    C = m.set_point(phi, 2 * phi * s36, ID="C")
    D = m.set_point(0, 2 * phi2 * s36, ID="D")
    E = m.set_point(-phi, 2 * phi * s36, ID="E")

    m.construct_polygon([A, B, C, D, E], ID="ABCDE")
    ln_ab = m.construct_line(A, B, classes=["golden"], ID="AB")
    m.construct_line(D, E, classes=["auxiliary"], ID="DE")

    # Perpendicular to DE at E: direction (2*s36, -phi)
    G1 = m.set_point(-phi + 2 * s36, 2 * phi * s36 - phi, guide=True, ID="G1")
    ln_ef = m.construct_line(E, G1, classes=["golden"], ID="EF")
    m.intersect(ln_ef, ln_ab, classes=["golden"], ID="F")

    return make_result(m, ("F", "B"), ("A", "F"), ("A", "F", "B"))


def build_prasolov_bui_irregular_pentagon() -> ConstructionResult:
    """V. V. Prasolov & Bùi Quang Tuân's equi-area irregular pentagon."""
    m = new_catalog_model("prasolov-bui-irregular-pentagon")
    phi = sp.Rational(1, 2) + sp.sqrt(5) / 2
    inv_phi = phi - 1

    # Sheared non-regular pentagon over Q(phi) whose five corner triangles all have exact area 2
    A = m.set_point(0, 0, classes=["given"], ID="A")
    B = m.set_point(2 * phi, 0, classes=["given"], ID="B")
    C = m.set_point(3 * phi + 1, 2 * inv_phi, ID="C")
    D = m.set_point(2 * phi + 1, 2, ID="D")
    E = m.set_point(inv_phi, 2 * inv_phi, ID="E")

    m.construct_polygon([A, B, C, D, E], ID="ABCDE")

    ln_bd = m.construct_line(B, D, classes=["golden"], ID="BD")
    ln_ce = m.construct_line(C, E, classes=["auxiliary"], ID="CE")
    ln_ac = m.construct_line(A, C, classes=["auxiliary"], ID="AC")
    m.construct_segment(D, A, classes=["auxiliary"], ID="DA")
    m.construct_segment(E, B, classes=["auxiliary"], ID="EB")

    m.intersect(ln_bd, ln_ce, classes=["golden"], ID="M")
    N = m.intersect(ln_bd, ln_ac, classes=["golden"], ID="N")
    _ = N

    return make_result(m, ("B", "M"), ("M", "D"), ("B", "M", "D"))


def build_tran_pentagon_hexagon() -> ConstructionResult:
    """Tran Quang Hung's regular pentagon inscribed on the base of a regular hexagon."""
    m = new_catalog_model("tran-pentagon-hexagon")
    phi, s36, _c36, _s72, _c72 = _pentagon_radicals()
    phi2 = phi + 1
    s3 = sp.sqrt(3)

    A = m.set_point(-1, 0, classes=["given"], ID="A")
    F = m.set_point(1, 0, classes=["given"], ID="F")
    E = m.set_point(2, s3, ID="E")
    D = m.set_point(1, 2 * s3, ID="D")
    C = m.set_point(-1, 2 * s3, ID="C")
    B = m.set_point(-2, s3, ID="B")
    m.construct_polygon([A, B, C, D, E, F], ID="ABCDEF")

    M = m.set_point(-phi, 2 * phi * s36, ID="M")
    N = m.set_point(0, 2 * phi2 * s36, ID="N")
    P = m.set_point(phi, 2 * phi * s36, ID="P")
    m.construct_polygon([A, M, N, P, F], classes=["golden"], ID="AMNPF")
    m.construct_segment(M, P, classes=["auxiliary"], ID="MP")

    ln_bc = m.construct_line(B, C, classes=["golden"], ID="BC")
    ln_de = m.construct_line(D, E, classes=["auxiliary"], ID="DE")

    # Perpendiculars to horizontal diagonal MP at M and P
    GM = m.set_point(-phi, 2 * phi * s36 + 1, guide=True, ID="GM")
    GP = m.set_point(phi, 2 * phi * s36 + 1, guide=True, ID="GP")
    ln_mq = m.construct_line(M, GM, classes=["golden"], ID="MQ")
    ln_pr = m.construct_line(P, GP, classes=["auxiliary"], ID="PR")

    m.intersect(ln_mq, ln_bc, classes=["golden"], ID="Q")
    R = m.intersect(ln_pr, ln_de, classes=["golden"], ID="R")
    _ = R

    return make_result(m, ("C", "Q"), ("Q", "B"), ("C", "Q", "B"))


def build_tran_star_six_pentagons() -> ConstructionResult:
    """Tran Quang Hung's star formed by reflecting a regular pentagon across its five sides."""
    m = new_catalog_model("tran-star-six-pentagons")
    phi, s36, _c36, _s72, _c72 = _pentagon_radicals()
    phi2 = phi + 1

    verts_xy = [
        (sp.Integer(-1), sp.Integer(0)),
        (sp.Integer(1), sp.Integer(0)),
        (phi, 2 * phi * s36),
        (sp.Integer(0), 2 * phi2 * s36),
        (-phi, 2 * phi * s36),
    ]
    names = ["A", "B", "C", "D", "E"]
    pts = [
        m.set_point(
            x,
            y,
            classes=["given"] if nm in ("A", "B") else [],
            ID=nm,
        )
        for nm, (x, y) in zip(names, verts_xy, strict=True)
    ]
    m.construct_polygon(pts, ID="ABCDE")

    # Reflect ABCDE across each of its 5 sides (each of exact length 2 => Q = 4)
    outer_pts = []
    for i in range(5):
        ux, uy = verts_xy[i]
        vx, vy = verts_xy[(i + 1) % 5]
        tri = []
        for idx_k, k in enumerate((4, 3, 2), start=1):
            wx, wy = verts_xy[(i + k) % 5]
            rx, ry = _reflect_across_side2(wx, wy, ux, uy, vx, vy)
            p_out = m.set_point(rx, ry, guide=(idx_k == 2), ID=f"R{i + 1}{idx_k}")
            tri.append(p_out)
            outer_pts.append(p_out)
        m.construct_polygon([pts[i], pts[(i + 1) % 5], tri[2], tri[1], tri[0]], classes=["auxiliary"])

    ln_ab = m.construct_line(pts[0], pts[1], classes=["golden"], ID="AB")

    # Connect outer perimeter vertices with step 6 (the chiral {5/2} star on lateral vertices)
    # Indices in outer_pts (length 15): 0, 3, 6, 9, 12 (idx_k=1) and 2, 5, 8, 11, 14 (idx_k=3)
    s_a = m.construct_line(outer_pts[0], outer_pts[6], classes=["golden"], ID="S1")
    s_b = m.construct_line(outer_pts[3], outer_pts[9], classes=["auxiliary"], ID="S2")
    for idx in (0, 3, 6, 9, 12):
        m.construct_segment(outer_pts[idx], outer_pts[(idx + 6) % 15], classes=["auxiliary"])
    for idx in (2, 5, 8, 11, 14):
        m.construct_segment(outer_pts[idx], outer_pts[(idx + 6) % 15], classes=["auxiliary"])

    G = m.intersect(s_a, ln_ab, classes=["golden"], ID="G")
    H = m.intersect(s_b, ln_ab, classes=["golden"], ID="H")
    _ = H

    # Order long/short dynamically: G = (2 - sqrt(5), 0) or (sqrt(5) - 2, 0) on A=(-1,0)..B=(1,0)
    if float((G.x - pts[0].x).evalf()) >= float((pts[1].x - G.x).evalf()):
        return make_result(m, ("A", "G"), ("G", "B"), ("A", "G", "B"))
    return make_result(m, ("G", "B"), ("A", "G"), ("A", "G", "B"))


def build_tran_wu_xing_equilaterals() -> ConstructionResult:
    """Tran Quang Hung's fivefold Wu Xing congruent equilateral triangles & pentagram."""
    m = new_catalog_model("tran-wu-xing-equilaterals")
    _phi, s36, c36, s72, c72 = _pentagon_radicals()
    s3 = sp.sqrt(3)

    O = m.set_point(0, 0, classes=["given"], ID="O")
    v_coords = [
        (sp.Integer(0), sp.Integer(1)),
        (-s72, c72),
        (-s36, -c36),
        (s36, -c36),
        (s72, c72),
    ]

    v_pts = []
    w_pts = []
    for i, (vx, vy) in enumerate(v_coords, start=1):
        vp = m.set_point(vx, vy, classes=["given"] if i == 1 else [], ID=f"V{i}")
        wx = sp.expand(vx / 2 + (s3 * vy) / 2)
        wy = sp.expand(-(s3 * vx) / 2 + vy / 2)
        wp = m.set_point(wx, wy, ID=f"W{i}")
        v_pts.append(vp)
        w_pts.append(wp)
        m.construct_polygon([O, vp, wp], ID=f"OV{i}W{i}")

    # Pentagram star connecting V1..V5 skipping one vertex at a time
    ln_v2v5 = m.construct_line(v_pts[1], v_pts[4], classes=["golden"], ID="V2V5")
    for i in range(5):
        m.construct_segment(v_pts[i], v_pts[(i + 2) % 5], classes=["auxiliary"])

    ln_ow1 = m.construct_line(O, w_pts[0], classes=["golden"], ID="OW1")
    m.intersect(ln_v2v5, ln_ow1, classes=["golden"], ID="F")

    return make_result(m, ("O", "F"), ("F", "W1"), ("O", "F", "W1"))


PENTAGONS_POLYGONS_SPECS: tuple[ConstructionSpec, ...] = (
    ConstructionSpec(
        slug="01-ptolemy-pentagon-pentagram",
        catalog_code="GC-05.01",
        family_slug="05-pentagons-polygons",
        order=1,
        title="Claudius Ptolemy's Regular Pentagon & Pentagram (Almagest I.10)",
        short_title="Ptolemy's Pentagon & Pentagram",
        discoverers=("claudius-ptolemy", "euclid"),
        year="c. 150 CE",
        citations=("ptolemy-almagest", "euclid-elements", "bogomolny-pentagon"),
        ctk_url="https://www.cut-the-knot.org/pythagoras/pentagon.shtml",
        ctk_title="Regular Pentagon and Golden Ratio",
        number_field=r"\mathbb{Q}(\phi, \sqrt{10 - 2\sqrt{5}})",
        number_field_text="Q(φ, √(10−2√5))",
        enunciation=(
            "In unit circle :g:`cO` with perpendicular radii :g:`OB` and :g:`OC`, let :g:`M` bisect "
            ":g:`OB`. Circle :g:`cMC` cuts :g:`AB` at :g:`E` with :math:`|OB|/|EO| = \\phi` and chord "
            ":math:`|CE|` equal to the side of inscribed regular pentagon :g:`CP1P2P3P4`, whose "
            "pentagram diagonals :g:`P1P4`, :g:`CP2`, :g:`CP3` cut one another in golden chains "
            ":math:`|P1K2|/|K2P4| = \\phi`."
        ),
        given_prose=(
            "Unit circle :g:`cO` centered at :g:`O` :math:`= (0,0)` through :g:`B` :math:`= (1,0)`, "
            "diameter :g:`AB`, and perpendicular apex :g:`C` :math:`= (0,1)`."
        ),
        steps_prose=(
            "Bisect radius :g:`OB` at :g:`M` :math:`= (\\tfrac{1}{2}, 0)` and swing circle :g:`cMC` to meet :g:`AB` at :g:`E` :math:`= (-1/\\phi, 0)`.",
            "Step off chord length :math:`|CE| = \\sqrt{3 - \\phi}` around :g:`cO` from :g:`C` to inscribe regular pentagon :g:`CP1P2P3P4`.",
            "Draw pentagram diagonals :g:`P1P4`, :g:`CP2`, and :g:`CP3`, intersecting along :g:`P1P4` at :g:`K1` and :g:`K2`.",
        ),
        proof_prose=(
            "Right triangle :math:`\\triangle MOC` has :math:`|MC| = \\frac{\\sqrt{5}}{2}`, so "
            ":math:`|OE| = \\frac{\\sqrt{5}-1}{2} = 1/\\phi` (the regular decagon side, Euclid XIII.9–10) "
            "and :math:`|CE|^2 = 1 + 1/\\phi^2 = 3 - \\phi = 4\\sin^2 36^\\circ` (the regular pentagon side). "
            "By Euclid XIII.8, every pair of crossing pentagram diagonals cuts each other in extreme and "
            "mean ratio, forming the 4-point golden chain :math:`(P1, K1, K2, P4)`."
        ),
        notes_prose=(
            "Ptolemy introduced this streamlined circle-and-midpoint construction in *Almagest* I.10 "
            "to compute his chord table at :math:`36^\\circ` and :math:`72^\\circ`, dramatically simplifying "
            "Euclid's Book IV Proposition 11."
        ),
        terms=("golden-ratio", "golden-section", "golden-chain", "extreme-and-mean-ratio"),
        builder=build_ptolemy_pentagon_pentagram,
    ),
    ConstructionSpec(
        slug="02-dao-tran-pentagon-bisector-incircle",
        catalog_code="GC-05.02",
        family_slug="05-pentagons-polygons",
        order=2,
        title="Dao Thanh Oai's Regular Pentagon Edge Perpendicular",
        short_title="Pentagon Edge Perpendicular",
        discoverers=("dao-thanh-oai", "tran-quang-hung"),
        year="2015",
        citations=("bogomolny-pentagon-dao", "bogomolny-pentagon-tqh", "bogomolny-golden-ratio"),
        ctk_url="https://www.cut-the-knot.org/do_you_know/GoldenRatioInRegularPentagon.shtml",
        ctk_title="Golden Ratio in Regular Pentagon",
        number_field=r"\mathbb{Q}(\phi, \sqrt{10 - 2\sqrt{5}})",
        number_field_text="Q(φ, √(10−2√5))",
        enunciation=(
            "In regular pentagon :g:`ABCDE`, erect line :g:`EF` perpendicular to side :g:`DE` at "
            "vertex :g:`E`. Line :g:`EF` intersects opposite non-adjacent side :g:`AB` internally at "
            ":g:`F` such that :math:`|FB|/|AF| = |AB|/|FB| = \\phi`."
        ),
        given_prose=(
            "Regular pentagon :g:`ABCDE` of side :math:`2` on base :g:`A` :math:`= (-1,0)`, "
            ":g:`B` :math:`= (1,0)`."
        ),
        steps_prose=(
            "Construct regular pentagon :g:`ABCDE` counterclockwise on base :g:`AB`.",
            "Erect line :g:`EF` perpendicular to upper-left side :g:`DE` at vertex :g:`E`.",
            "Mark intersection :g:`F` of :g:`EF` with base :g:`AB`.",
        ),
        proof_prose=(
            "Interior angle :math:`\\angle DEA = 108^\\circ`, while :math:`\\angle DEF = 90^\\circ`, "
            "leaving :math:`\\angle AEF = 18^\\circ`. Since :math:`\\angle EAF = 108^\\circ`, triangle "
            ":math:`\\triangle EAF` has :math:`\\angle EFA = 54^\\circ`. By the Law of Sines on "
            ":math:`\\triangle EAF` with :math:`|EA| = 2`, :math:`|AF| = \\frac{2\\sin 18^\\circ}{\\sin 54^\\circ} "
            "= \\frac{2(1/(2\\phi))}{\\phi/2} = \\frac{2}{\\phi^2}`, whence :math:`|FB| = 2 - \\frac{2}{\\phi^2} = \\frac{2}{\\phi}` "
            "and :math:`|FB|/|AF| = \\phi`."
        ),
        notes_prose=(
            "Tran Quang Hung discovered a dual regular-pentagon division via the incircle and radius "
            "midpoint (`AnotherGoldenRatioInRegularPentagon.shtml`), reflecting the ubiquitous :math:`18^\\circ\\text{-}54^\\circ\\text{-}72^\\circ` cosine ratios."
        ),
        terms=("golden-ratio", "golden-section"),
        builder=build_dao_tran_pentagon_bisector_incircle,
    ),
    ConstructionSpec(
        slug="03-prasolov-bui-irregular-pentagon",
        catalog_code="GC-05.03",
        family_slug="05-pentagons-polygons",
        order=3,
        title="Prasolov & Bùi Quang Tuân's Equi-Area Irregular Pentagon",
        short_title="Equi-Area Irregular Pentagon",
        discoverers=("v-v-prasolov", "bui-quang-tuan"),
        year="2006",
        citations=("prasolov-2006", "bogomolny-irregular-pentagon", "bogomolny-golden-ratio"),
        ctk_url="https://www.cut-the-knot.org/do_you_know/NoRegularPentagon.shtml",
        ctk_title="Golden Ratio in an Irregular Pentagon",
        number_field=r"\mathbb{Q}(\phi)",
        number_field_text="Q(φ)",
        enunciation=(
            "Let :g:`ABCDE` be *any* convex pentagon—regular or irregular—whose five peripheral "
            "triangles :math:`\\triangle ABE, \\triangle ABC, \\triangle BCD, \\triangle CDE, \\triangle DEA` "
            "have equal area. Then every diagonal is parallel to the opposite side and is divided by "
            "the crossing diagonals in the golden ratio, e.g. :math:`|BM|/|MD| = \\phi`."
        ),
        given_prose=(
            "Sheared irregular convex pentagon :g:`ABCDE` over :math:`\\mathbb{Q}(\\phi)` with "
            ":g:`A` :math:`= (0,0)` and :g:`B` :math:`= (2\\phi, 0)`, each peripheral triangle having exact area :math:`2`."
        ),
        steps_prose=(
            "Place irregular vertices :g:`A` :math:`= (0,0)`, :g:`B` :math:`= (2\\phi, 0)`, :g:`C` :math:`= (3\\phi+1, 2/\\phi)`, :g:`D` :math:`= (2\\phi+1, 2)`, and :g:`E` :math:`= (1/\\phi, 2/\\phi)`.",
            "Draw diagonals :g:`BD`, :g:`CE`, and :g:`AC`.",
            "Mark intersections :g:`M` :math:`= BD \\cap CE` and :g:`N` :math:`= BD \\cap AC`.",
        ),
        proof_prose=(
            "Equal areas :math:`[ABE] = [ABC]` with shared base :g:`AB` force :math:`CE \\parallel AB`; "
            "cyclically, every diagonal is parallel to its opposite side, so :math:`ABME` is a parallelogram "
            "with :math:`|EM| = |AB|`. Set :math:`x = |BM|/|MD|`. Then :math:`[ABE] = [BM E]` (half of "
            "parallelogram :math:`ABME`), while :math:`[CDE] = [BCD]` implies :math:`|CE|/|EM| = 1 + 1/x` "
            "and :math:`x = 1 + 1/x`, forcing :math:`x = \\phi` purely from affine area invariance!"
        ),
        notes_prose=(
            "Because parallelisms and length ratios on parallel lines are affine invariants, *every* "
            "affine image of a regular pentagon retains all five golden pentagram chains while losing "
            "all metric symmetry—and lives entirely over :math:`\\mathbb{Q}(\\phi)` without :math:`\\sin 36^\\circ`."
        ),
        terms=("golden-ratio", "golden-section", "golden-chain"),
        builder=build_prasolov_bui_irregular_pentagon,
    ),
    ConstructionSpec(
        slug="04-tran-pentagon-hexagon",
        catalog_code="GC-05.04",
        family_slug="05-pentagons-polygons",
        order=4,
        title="Tran Quang Hung's Shared-Base Regular Pentagon & Hexagon",
        short_title="Pentagon Inside Hexagon",
        discoverers=("tran-quang-hung",),
        year="2015",
        citations=("bogomolny-5-6", "bogomolny-golden-ratio"),
        ctk_url="https://www.cut-the-knot.org/do_you_know/5-6-GoldenRatioIn.shtml",
        ctk_title="Golden Ratio in Pentagon and Hexagon",
        number_field=r"\mathbb{Q}(\sqrt{3}, \phi, \sqrt{10 - 2\sqrt{5}})",
        number_field_text="Q(√3, φ, √(10−2√5))",
        enunciation=(
            "Erect regular hexagon :g:`ABCDEF` and regular pentagon :g:`AMNPF` on the same side "
            ":g:`AF`. The perpendiculars :g:`MQ` and :g:`PR` to diagonal :g:`MP` at :g:`M` and :g:`P` "
            "intersect upper hexagon sides :g:`BC` and :g:`DE` at :g:`Q` and :g:`R` such that "
            ":math:`|CQ|/|QB| = |DR|/|RE| = \\phi`."
        ),
        given_prose=(
            "Shared horizontal base :g:`A` :math:`= (-1,0)`, :g:`F` :math:`= (1,0)` of length :math:`2`."
        ),
        steps_prose=(
            "Construct regular hexagon :g:`ABCDEF` of side :math:`2` above :g:`AF`, with upper-left side :g:`B` :math:`= (-2, \\sqrt{3})` to :g:`C` :math:`= (-1, 2\\sqrt{3})`.",
            "Construct regular pentagon :g:`AMNPF` of side :math:`2` on the same side of :g:`AF`, with horizontal diagonal :g:`MP`.",
            "Erect perpendiculars :g:`MQ` and :g:`PR` to :g:`MP` at :g:`M` and :g:`P`, cutting :g:`BC` at :g:`Q` and :g:`DE` at :g:`R`.",
        ),
        proof_prose=(
            "For base :math:`|AF| = 2`, diagonal :g:`MP` of regular pentagon :g:`AMNPF` has length "
            ":math:`2\\phi`, so :g:`M` has abscissa :math:`x_M = -\\phi` while :g:`B` and :g:`C` have "
            "abscissas :math:`x_B = -2` and :math:`x_C = -1`. Because :g:`MQ` is vertical (:math:`x = -\\phi`), "
            "linear projection onto the :math:`x`-axis yields "
            ":math:`|CQ|/|QB| = (-1 - (-\\phi))/(-\\phi - (-2)) = (\\phi - 1)/(2 - \\phi) = (1/\\phi)/(1/\\phi^2) = \\phi`."
        ),
        notes_prose=(
            "Projected onto the horizontal axis, the hexagon's lateral overhang has width :math:`1` "
            "while the pentagon's lateral overhang has width :math:`\\phi - 1 = 1/\\phi`, immediately "
            "sectioning the overhang in extreme and mean ratio."
        ),
        terms=("golden-ratio", "golden-section"),
        builder=build_tran_pentagon_hexagon,
    ),
    ConstructionSpec(
        slug="05-tran-star-six-pentagons",
        catalog_code="GC-05.05",
        family_slug="05-pentagons-polygons",
        order=5,
        title="Tran Quang Hung's Six-Pentagon Reflection Star",
        short_title="Six-Pentagon Reflection Star",
        discoverers=("tran-quang-hung",),
        year="2016",
        citations=("bogomolny-six-pentagons", "bogomolny-golden-ratio"),
        ctk_url="https://www.cut-the-knot.org/do_you_know/StarSixPentagonsGoldenRatio.shtml",
        ctk_title="Star, Six Pentagons and Golden Ratio",
        number_field=r"\mathbb{Q}(\phi, \sqrt{10 - 2\sqrt{5}})",
        number_field_text="Q(φ, √(10−2√5))",
        enunciation=(
            "Reflect regular pentagon :g:`ABCDE` across each of its five sides to obtain five surrounding "
            "congruent pentagons. Joining the outer lateral vertices across two intervening pentagons "
            "(such as chord :g:`S1`) cuts every side of :g:`ABCDE` in the golden ratio, dividing :g:`AB` "
            "at :g:`G` and :g:`H` in a 4-point golden chain."
        ),
        given_prose=(
            "Central regular pentagon :g:`ABCDE` of side :math:`2` on base :g:`A` :math:`= (-1,0)`, "
            ":g:`B` :math:`= (1,0)`."
        ),
        steps_prose=(
            "Reflect :g:`ABCDE` across each of its five sides :g:`AB`, :g:`BC`, :g:`CD`, :g:`DE`, :g:`EA`.",
            "Join the outer lateral vertices in the two chiral :math:`\\{5/2\\}` star polygons (including chord :g:`S1`).",
            "Mark intersections :g:`G` and :g:`H` where the star chords cross side :g:`AB`.",
        ),
        proof_prose=(
            "By fivefold dihedral symmetry :math:`D_5`, the two chiral :math:`\\{5/2\\}` star polygons "
            "on the reflected lateral vertices meet side :g:`AB` at mirror-symmetric points :g:`G` and :g:`H`. "
            "Using exact reflection across unit-quadrance-scaled sides, chord :g:`S1` meets :math:`y = 0` "
            "at :math:`x = \\pm(\\sqrt{5} - 2)`, partitioning :math:`[-1, 1]` into segments of lengths "
            ":math:`2/\\phi^2, 2/\\phi^3, 2/\\phi^2` and proving :math:`|AG|/|GB| = \\phi^{\\pm 1}`."
        ),
        notes_prose=(
            "Remarkably, at each golden division point :g:`G` and :g:`H` on a side of :g:`ABCDE`, "
            "two distinct star chords concur directly on the pentagon edge."
        ),
        terms=("golden-ratio", "golden-section", "golden-chain"),
        builder=build_tran_star_six_pentagons,
    ),
    ConstructionSpec(
        slug="06-tran-wu-xing-equilaterals",
        catalog_code="GC-05.06",
        family_slug="05-pentagons-polygons",
        order=6,
        title="Tran Quang Hung's Fivefold Wu Xing Equilateral Star",
        short_title="Wu Xing Equilateral Star",
        discoverers=("tran-quang-hung",),
        year="2015",
        citations=("bogomolny-wu-xing", "bogomolny-golden-ratio"),
        ctk_url="https://www.cut-the-knot.org/do_you_know/GoldenRatioInWuXing.shtml",
        ctk_title="Golden Ratio in Wu Xing",
        number_field=r"\mathbb{Q}(\sqrt{3}, \phi, \sqrt{10 - 2\sqrt{5}})",
        number_field_text="Q(√3, φ, √(10−2√5))",
        enunciation=(
            "Arrange five congruent equilateral triangles :g:`OV1W1` … :g:`OV5W5` of unit side with "
            "fivefold rotational symmetry around shared vertex :g:`O`. The pentagram star joining outer "
            "vertices :g:`V1` … :g:`V5` cuts the radial sides of the equilateral triangles in the golden "
            "ratio, e.g. chord :g:`V2V5` cuts :g:`OW1` at :g:`F` with :math:`|OF|/|FW1| = \\phi`."
        ),
        given_prose=(
            "Center :g:`O` :math:`= (0,0)` and leading apex :g:`V1` :math:`= (0,1)` of five :math:`72^\\circ`-spaced "
            "unit equilateral triangles."
        ),
        steps_prose=(
            "Construct the five :math:`72^\\circ`-rotated unit equilateral triangles :g:`OV1W1` … :g:`OV5W5` sharing vertex :g:`O`.",
            "Draw pentagram chord :g:`V2V5` (along with the remaining four chords of star :math:`\\{5/2\\}`).",
            "Mark intersection :g:`F` of horizontal pentagram chord :g:`V2V5` with equilateral side :g:`OW1`.",
        ),
        proof_prose=(
            "Vertices :g:`V2` and :g:`V5` lie at angles :math:`90^\\circ \\pm 72^\\circ`, so chord :g:`V2V5` "
            "is horizontal at height :math:`y = \\sin 18^\\circ = \\frac{\\sqrt{5}-1}{4} = \\frac{1}{2\\phi}`. "
            "Meanwhile, rotating :g:`V1` :math:`= (0,1)` clockwise by :math:`60^\\circ` places :g:`W1` at "
            ":math:`(\\tfrac{\\sqrt{3}}{2}, \\tfrac{1}{2})` (:math:`30^\\circ` above the horizontal). "
            "Hence :g:`OW1` reaches height :math:`y_F = \\frac{1}{2\\phi}` at distance "
            ":math:`|OF| = \\frac{y_F}{\\sin 30^\\circ} = \\frac{1}{\\phi}`, leaving :math:`|FW1| = 1 - \\frac{1}{\\phi} = \\frac{1}{\\phi^2}` "
            "and proving :math:`|OF|/|FW1| = \\phi`."
        ),
        notes_prose=(
            "This construction fuses :math:`C_5` (:math:`72^\\circ`) and :math:`C_3` (:math:`60^\\circ`) "
            "rotational symmetries: their :math:`12^\\circ` phase difference aligns :math:`\\sin 18^\\circ` "
            "with :math:`\\cos 60^\\circ = 1/2`."
        ),
        terms=("golden-ratio", "golden-section"),
        builder=build_tran_wu_xing_equilaterals,
    ),
)
