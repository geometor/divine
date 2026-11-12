"""Family 03: Squares, Grids & Golden Rectangles.

Catalogs exact symbolic Golden Ratio constructions arising from squares,
$2 \\times 2$ and $3 \\times 3$ lattice grids, inscribed incircles, the Greek cross,
and rotated unit squares curated on Cut-the-Knot.
"""

from __future__ import annotations

import sympy as sp

from .helpers import make_result, new_catalog_model
from .schema import ConstructionResult, ConstructionSpec


def build_tran_square_inscribed_semicircle() -> ConstructionResult:
    """Square inscribed in a right isosceles triangle inside a circle (Tran Quang Hung)."""
    m = new_catalog_model("tran-square-inscribed-semicircle")
    O = m.set_point(0, 0, classes=["given"], ID="O")
    A = m.set_point(-3, 0, classes=["given"], ID="A")
    B = m.set_point(3, 0, classes=["given"], ID="B")
    C = m.set_point(0, 3, ID="C")

    c_o = m.construct_circle(O, B, classes=["primary"], ID="cO")
    m.construct_polygon([A, B, C], ID="ABC")
    m.construct_line(A, B, ID="AB")

    # Inscribed square DEGF with F=(-1,0), G=(1,0) on AB and D=(-1,2) on AC, E=(1,2) on BC
    D = m.set_point(-1, 2, ID="D")
    E = m.set_point(1, 2, ID="E")
    G = m.set_point(1, 0, ID="G")
    F = m.set_point(-1, 0, ID="F")
    m.construct_polygon([D, E, G, F], classes=["golden"], ID="DEGF")

    ln_de = m.construct_line(D, E, classes=["golden"], ID="DE")
    Q = m.intersect(ln_de, c_o, beyond=(E, D), classes=["golden"], ID="Q")
    m.intersect(ln_de, c_o, beyond=(D, E), classes=["golden"], ID="P")
    _ = Q

    return make_result(m, ("D", "E"), ("E", "P"), ("D", "E", "P"))


def build_tran_square_midpoints() -> ConstructionResult:
    """Tran Quang Hung's square midpoint circle construction (Buratino 1)."""
    m = new_catalog_model("tran-square-midpoints")
    A = m.set_point(-2, 2, classes=["given"], ID="A")
    B = m.set_point(2, 2, classes=["given"], ID="B")
    C = m.set_point(2, -2, ID="C")
    D = m.set_point(-2, -2, ID="D")
    F = m.set_point(0, 0, ID="F")

    M = m.set_point(0, 2, ID="M")
    N = m.set_point(2, 0, ID="N")
    P = m.set_point(0, -2, ID="P")
    Q = m.set_point(-2, 0, ID="Q")

    m.construct_polygon([A, B, C, D], ID="ABCD")
    ln_qn = m.construct_line(Q, N, classes=["golden"], ID="QN")
    ln_mp = m.construct_line(M, P, classes=["auxiliary"], ID="MP")
    m.construct_segment(A, P, classes=["auxiliary"], ID="AP")

    K = m.set_point(-1, 0, ID="K")
    c_ka = m.construct_circle(K, A, classes=["compass"], ID="cKA")
    X = m.intersect(c_ka, ln_qn, between=(F, N), classes=["golden"], ID="X")

    ln_ax = m.construct_line(A, X, classes=["auxiliary"], ID="AX")
    Z = m.intersect(ln_ax, ln_mp, classes=["golden"], ID="Z")
    _ = Z

    return make_result(m, ("F", "X"), ("X", "N"), ("F", "X", "N"))


def build_nguyen_2x2_square() -> ConstructionResult:
    """Nguyen Thanh Dung's 2x2 square grid compass arc construction."""
    m = new_catalog_model("nguyen-2x2-square")
    P1 = m.set_point(-1, 1, ID="P1")
    P2 = m.set_point(1, 1, ID="P2")
    P3 = m.set_point(1, -1, ID="P3")
    P4 = m.set_point(-1, -1, ID="P4")

    A = m.set_point(-1, 0, classes=["given"], ID="A")
    O = m.set_point(0, 0, ID="O")
    B = m.set_point(1, 0, classes=["given"], ID="B")
    D = m.set_point(0, 1, ID="D")
    E = m.set_point(0, -1, ID="E")
    C = m.set_point(2, 0, ID="C")

    m.construct_polygon([P1, P2, P3, P4], ID="P1P2P3P4")
    ln_ab = m.construct_line(A, B, classes=["golden"], ID="AB")
    m.construct_segment(D, E, classes=["auxiliary"], ID="DE")
    m.construct_segment(C, D, classes=["auxiliary"], ID="CD")
    _ = O

    c_cd = m.construct_circle(C, D, classes=["golden"], ID="cCD")
    m.intersect(c_cd, ln_ab, between=(A, B), classes=["golden"], ID="M")

    return make_result(m, ("M", "B"), ("A", "M"), ("A", "M", "B"))


def build_tran_mcgucken_3x3_circle() -> ConstructionResult:
    """Tran Quang Hung & Elliot McGucken's 3x3 grid diagonal circle division."""
    m = new_catalog_model("tran-mcgucken-3x3-circle")
    S1 = m.set_point(-3, 3, ID="S1")
    A = m.set_point(3, 3, classes=["given"], ID="A")
    S3 = m.set_point(3, -3, ID="S3")
    S4 = m.set_point(-3, -3, ID="S4")

    C1 = m.set_point(-1, 1, ID="C1")
    C = m.set_point(1, 1, ID="C")
    C3 = m.set_point(1, -1, ID="C3")
    C4 = m.set_point(-1, -1, ID="C4")

    O = m.set_point(0, 0, classes=["given"], ID="O")
    T = m.set_point(1, 3, ID="T")

    m.construct_polygon([S1, A, S3, S4], ID="S1AS3S4")
    m.construct_polygon([C1, C, C3, C4], classes=["auxiliary"], ID="C1CC3C4")

    # Internal 3x3 grid lines
    G1 = m.set_point(-1, 3, guide=True, ID="G1")
    G2 = m.set_point(-1, -3, guide=True, ID="G2")
    G3 = m.set_point(1, -3, guide=True, ID="G3")
    G4 = m.set_point(-3, 1, guide=True, ID="G4")
    G5 = m.set_point(3, 1, guide=True, ID="G5")
    G6 = m.set_point(-3, -1, guide=True, ID="G6")
    G7 = m.set_point(3, -1, guide=True, ID="G7")
    m.construct_segment(G1, G2, classes=["auxiliary"], ID="gV1")
    m.construct_segment(T, G3, classes=["auxiliary"], ID="gV2")
    m.construct_segment(G4, G5, classes=["auxiliary"], ID="gH1")
    m.construct_segment(G6, G7, classes=["auxiliary"], ID="gH2")
    m.construct_segment(O, T, classes=["auxiliary"], ID="OT")

    ln_oa = m.construct_line(O, A, classes=["golden"], ID="OA")
    c_ot = m.construct_circle(O, T, classes=["golden"], ID="cOT")
    m.intersect(c_ot, ln_oa, between=(C, A), classes=["golden"], ID="B")

    return make_result(m, ("C", "B"), ("B", "A"), ("C", "B", "A"))


def build_tran_3x3_incenter() -> ConstructionResult:
    """Tran Quang Hung's 3x3 grid isosceles triangle incenter theorem."""
    m = new_catalog_model("tran-3x3-incenter")
    A = m.set_point(0, 0, classes=["given"], ID="A")
    Q1 = m.set_point(3, 0, classes=["given"], ID="Q1")
    Q2 = m.set_point(3, 3, ID="Q2")
    Q3 = m.set_point(0, 3, ID="Q3")

    S = m.set_point(1, 1, ID="S")
    K1 = m.set_point(2, 1, ID="K1")
    T = m.set_point(2, 2, ID="T")
    K2 = m.set_point(1, 2, ID="K2")

    U = m.set_point(3, 1, ID="U")
    V = m.set_point(1, 3, ID="V")

    m.construct_polygon([A, Q1, Q2, Q3], ID="AQ1Q2Q3")
    m.construct_polygon([S, K1, T, K2], classes=["auxiliary"], ID="SK1TK2")
    m.construct_polygon([A, U, V], ID="AUV")

    # Exact incenter P = ((5 - sqrt(5))/2, (5 - sqrt(5))/2) of AUV; tangent to UV at T=(2,2)
    px = (5 - sp.sqrt(5)) / 2
    P = m.set_point(px, px, classes=["golden"], ID="P")
    m.construct_line(A, Q2, classes=["golden"], ID="AT")
    m.construct_circle(P, T, classes=["golden"], ID="cPT")

    return make_result(m, ("P", "T"), ("S", "P"), ("S", "P", "T"))


def build_suppa_square_inradii() -> ConstructionResult:
    """Ercole Suppa's square midpoint inradii ratio (2015)."""
    m = new_catalog_model("suppa-square-inradii")
    D = m.set_point(0, 0, classes=["given"], ID="D")
    C = m.set_point(2, 0, classes=["given"], ID="C")
    B = m.set_point(2, 2, ID="B")
    A = m.set_point(0, 2, ID="A")
    M = m.set_point(0, 1, ID="M")

    m.construct_polygon([A, B, C, D], ID="ABCD")
    ln_cm = m.construct_line(C, M, ID="CM")
    m.construct_segment(B, M, ID="BM")

    # Incenter E of isosceles BCM (inradius R = 1/phi, tangent to BC at H=(2,1))
    ex = (5 - sp.sqrt(5)) / 2
    E = m.set_point(ex, 1, classes=["golden"], ID="E")
    H = m.set_point(2, 1, ID="H")
    m.construct_circle(E, H, classes=["golden"], ID="cEH")

    # Incenter F of right CDM (inradius r = 1/phi^2, tangent to CD at P=((3-sqrt(5))/2, 0))
    fx = (3 - sp.sqrt(5)) / 2
    F = m.set_point(fx, fx, classes=["golden"], ID="F")
    P = m.set_point(fx, 0, ID="P")
    m.construct_circle(F, P, classes=["compass"], ID="cFP")

    ln_ef = m.construct_line(E, F, classes=["golden"], ID="EF")
    m.intersect(ln_ef, ln_cm, classes=["golden"], ID="K")

    return make_result(m, ("E", "K"), ("K", "F"), ("E", "K", "F"))


def build_bui_cross_and_square() -> ConstructionResult:
    """Bùi Quang Tuân & Alexandre Borovik's Greek cross and square in a circle."""
    m = new_catalog_model("bui-cross-and-square")
    s5 = sp.sqrt(5)

    O = m.set_point(0, 0, classes=["given"], ID="O")
    A = m.set_point(1, 3, classes=["given"], ID="A")
    m.construct_circle(O, A, classes=["primary"], ID="cO")

    # Greek cross of five 2x2 squares inscribed in cO (radius sqrt(10))
    X1 = m.set_point(-1, 3, ID="X1")
    C = m.set_point(1, 1, ID="C")
    X2 = m.set_point(3, 1, ID="X2")
    X3 = m.set_point(3, -1, ID="X3")
    D = m.set_point(1, -1, ID="D")
    X4 = m.set_point(1, -3, ID="X4")
    X5 = m.set_point(-1, -3, ID="X5")
    X6 = m.set_point(-1, -1, ID="X6")
    X7 = m.set_point(-3, -1, ID="X7")
    X8 = m.set_point(-3, 1, ID="X8")
    X9 = m.set_point(-1, 1, ID="X9")
    m.construct_polygon([X1, A, C, X2, X3, D, X4, X5, X6, X7, X8, X9], ID="CROSS")

    # Inscribed concentric square S1 S2 S3 S4 of side 2*sqrt(5)
    S1 = m.set_point(-s5, s5, ID="S1")
    S2 = m.set_point(s5, s5, ID="S2")
    S3 = m.set_point(s5, -s5, ID="S3")
    S4 = m.set_point(-s5, -s5, ID="S4")
    m.construct_polygon([S1, S2, S3, S4], classes=["golden"], ID="S1S2S3S4")

    ln_ac = m.construct_line(A, C, classes=["golden"], ID="AC")
    ln_s1s2 = m.construct_line(S1, S2, classes=["auxiliary"], ID="S1S2")
    ln_s4s3 = m.construct_line(S4, S3, classes=["auxiliary"], ID="S4S3")
    m.intersect(ln_ac, ln_s1s2, classes=["golden"], ID="B")
    E = m.intersect(ln_ac, ln_s4s3, classes=["golden"], ID="E")
    _ = E

    return make_result(m, ("B", "C"), ("A", "B"), ("A", "B", "C"))


def build_arioni_rotating_square() -> ConstructionResult:
    """John Arioni's 30-degree rotated unit square and diagonal circle."""
    m = new_catalog_model("arioni-rotating-square")
    s3 = sp.sqrt(3)

    D = m.set_point(0, 0, classes=["given"], ID="D")
    G = m.set_point(1, 0, classes=["given"], ID="G")
    H = m.set_point(1, 1, ID="H")
    J = m.set_point(0, 1, ID="J")
    m.construct_polygon([D, G, H, J], ID="DGHJ")

    # Unit square DCBA rotated clockwise by 30 degrees around D
    A = m.set_point(sp.Rational(1, 2), s3 / 2, ID="A")
    B = m.set_point((1 + s3) / 2, (s3 - 1) / 2, ID="B")
    C = m.set_point(s3 / 2, -sp.Rational(1, 2), ID="C")
    m.construct_polygon([D, C, B, A], ID="DCBA")
    m.construct_segment(A, C, classes=["auxiliary"], ID="AC")

    ln_dg = m.construct_line(D, G, classes=["golden"], ID="DG")
    c_ac = m.construct_circle(A, C, classes=["golden"], ID="cAC")
    m.intersect(c_ac, ln_dg, beyond=(D, G), classes=["golden"], ID="E")
    F = m.intersect(c_ac, ln_dg, beyond=(G, D), classes=["golden"], ID="F")
    _ = F

    return make_result(m, ("D", "G"), ("G", "E"), ("D", "G", "E"))


SQUARES_RECTANGLES_SPECS: tuple[ConstructionSpec, ...] = (
    ConstructionSpec(
        slug="01-tran-square-inscribed-semicircle",
        catalog_code="GC-03.01",
        family_slug="03-squares-rectangles",
        order=1,
        title="Tran Quang Hung's Square Inscribed in a Right Isosceles Semicircle",
        short_title="Square in Semicircle",
        discoverers=("tran-quang-hung",),
        year="2014",
        citations=("bogomolny-rectangles", "bogomolny-golden-ratio"),
        ctk_url="https://www.cut-the-knot.org/do_you_know/GoldenRatioInRectangles.shtml",
        ctk_title="Golden Ratio in Square and Circle",
        number_field=r"\mathbb{Q}(\phi)",
        number_field_text="Q(φ)",
        enunciation=(
            "Let :g:`ABC` be a right isosceles triangle inscribed in a semicircle of :g:`cO` on "
            "diameter :g:`AB`, and let square :g:`DEGF` sit on :g:`AB` with vertices :g:`D` and :g:`E` "
            "on legs :g:`AC` and :g:`BC`. Extending top side :g:`DE` to meet circle :g:`cO` at :g:`Q` "
            "and :g:`P` divides :g:`DP` in the golden ratio: :math:`|DE|/|EP| = |DP|/|DE| = \\phi`."
        ),
        given_prose=(
            "Circle :g:`cO` centered at :g:`O` :math:`= (0,0)` of radius :math:`3` with diameter "
            ":g:`A` :math:`= (-3,0)`, :g:`B` :math:`= (3,0)` and apex :g:`C` :math:`= (0,3)`."
        ),
        steps_prose=(
            "Inscribe right isosceles triangle :g:`ABC` in the upper semicircle on diameter :g:`AB`.",
            "Inscribe square :g:`DEGF` of side :math:`2` with :g:`F` :math:`= (-1,0)`, :g:`G` :math:`= (1,0)` on :g:`AB` and :g:`D` :math:`= (-1,2)`, :g:`E` :math:`= (1,2)` on :g:`AC`, :g:`BC`.",
            "Extend line :g:`DE` horizontally to meet circle :g:`cO` at :g:`Q` :math:`= (-\\sqrt{5}, 2)` and :g:`P` :math:`= (\\sqrt{5}, 2)`.",
        ),
        proof_prose=(
            "At :math:`x = \\pm 1`, legs :g:`AC` (:math:`y = x + 3`) and :g:`BC` (:math:`y = -x + 3`) "
            "have height :math:`y = 2`, matching the horizontal side :math:`|DE| = 2` of inscribed "
            "square :g:`DEGF`. On circle :math:`x^2 + y^2 = 9`, setting :math:`y = 2` yields "
            ":math:`x = \\pm\\sqrt{5}`, so :math:`|EP| = \\sqrt{5} - 1 = 2/\\phi` and "
            ":math:`|DE|/|EP| = 2 / (2/\\phi) = \\phi`."
        ),
        notes_prose=(
            "Because :math:`(Q, D, E, P)` is symmetric across the vertical axis, it forms a complete "
            "4-point golden chain with lengths :math:`2/\\phi, 2, 2/\\phi`."
        ),
        terms=("golden-ratio", "golden-section", "golden-chain", "intersecting-chords-theorem"),
        builder=build_tran_square_inscribed_semicircle,
    ),
    ConstructionSpec(
        slug="02-tran-square-midpoints",
        catalog_code="GC-03.02",
        family_slug="03-squares-rectangles",
        order=2,
        title="Tran Quang Hung's Square Midpoint Circle Division",
        short_title="Square Midpoint Circle",
        discoverers=("tran-quang-hung",),
        year="2015",
        citations=("bogomolny-buratino1", "bogomolny-golden-ratio"),
        ctk_url="https://www.cut-the-knot.org/do_you_know/Buratino1.shtml",
        ctk_title="Golden Ratio in Square via Midpoints",
        number_field=r"\mathbb{Q}(\phi)",
        number_field_text="Q(φ)",
        enunciation=(
            "Let :g:`ABCD` be a square with center :g:`F` and side midpoints :g:`M`, :g:`N`, :g:`P`, :g:`Q`. "
            "The circle :g:`cKA` on diameter :g:`AP` intersects midline :g:`QN` at :g:`X` between :g:`F` "
            "and :g:`N` such that :math:`|FX|/|XN| = \\phi`, while chord :g:`AX` cuts :g:`MP` at :g:`Z` "
            "with :math:`|MZ|/|ZF| = \\phi`."
        ),
        given_prose=(
            "Square :g:`ABCD` of side :math:`4` centered at :g:`F` :math:`= (0,0)` with vertices "
            ":math:`(\\pm 2, \\pm 2)`."
        ),
        steps_prose=(
            "Mark side midpoints :g:`M` :math:`= (0,2)`, :g:`N` :math:`= (2,0)`, :g:`P` :math:`= (0,-2)`, :g:`Q` :math:`= (-2,0)` and center :g:`F` :math:`= (0,0)`.",
            "Bisect :g:`AP` at :g:`K` :math:`= (-1,0)` and draw circle :g:`cKA` of radius :math:`\\sqrt{5}` on diameter :g:`AP`.",
            "Mark :g:`X` where :g:`cKA` crosses :g:`QN` between :g:`F` and :g:`N`, and :g:`Z` where :g:`AX` crosses :g:`MP`.",
        ),
        proof_prose=(
            "Circle :g:`cKA` has equation :math:`(x + 1)^2 + y^2 = 5`. Along :g:`QN` (:math:`y = 0`), "
            "the positive root is :math:`x_X = \\sqrt{5} - 1 = 2/\\phi`. Since :math:`x_N = 2`, "
            ":math:`|XN| = 3 - \\sqrt{5} = 2/\\phi^2`, whence :math:`|FX|/|XN| = (2/\\phi)/(2/\\phi^2) = \\phi`."
        ),
        notes_prose=(
            "Right angle :math:`\\angle AXP = 90^\\circ` (Thales' theorem on diameter :g:`AP`) also "
            "makes :math:`\\triangle PFX \\sim \\triangle AFZ`, transferring the golden division from "
            "horizontal half-midline :g:`FN` directly onto vertical half-midline :g:`FM`."
        ),
        terms=("golden-ratio", "golden-section"),
        builder=build_tran_square_midpoints,
    ),
    ConstructionSpec(
        slug="03-nguyen-2x2-square",
        catalog_code="GC-03.03",
        family_slug="03-squares-rectangles",
        order=3,
        title="Nguyen Thanh Dung's 2×2 Grid Compass Arc",
        short_title="2×2 Grid Compass Arc",
        discoverers=("nguyen-thanh-dung",),
        year="2016",
        citations=("bogomolny-2x2", "bogomolny-golden-ratio"),
        ctk_url="https://www.cut-the-knot.org/do_you_know/2x2GoldenRatio.shtml",
        ctk_title="Golden Ratio in 2x2 Square",
        number_field=r"\mathbb{Q}(\phi)",
        number_field_text="Q(φ)",
        enunciation=(
            "On a :math:`2 \\times 2` square grid :g:`P1P2P3P4` with horizontal midline :g:`AB`, "
            "center :g:`O`, and top midpoint :g:`D`, extend :g:`AB` by one grid unit to :g:`C`. "
            "Circle :g:`cCD` centered at :g:`C` through :g:`D` cuts :g:`AB` at :g:`M` in the golden "
            "ratio: :math:`|MB|/|AM| = |AB|/|MB| = \\phi`."
        ),
        given_prose=(
            "A :math:`2 \\times 2` grid with midline endpoints :g:`A` :math:`= (-1,0)` and :g:`B` :math:`= (1,0)`."
        ),
        steps_prose=(
            "Form the :math:`2 \\times 2` grid :g:`P1P2P3P4` centered at :g:`O` :math:`= (0,0)` with top midpoint :g:`D` :math:`= (0,1)`.",
            "Mark :g:`C` :math:`= (2,0)` on ray :g:`AB` at unit distance beyond :g:`B`.",
            "Draw circle :g:`cCD` centered at :g:`C` through :g:`D`, intersecting :g:`AB` internally at :g:`M`.",
        ),
        proof_prose=(
            "In right triangle :math:`\\triangle COD`, legs :math:`|OC| = 2` and :math:`|OD| = 1` give "
            "radius :math:`|CD| = \\sqrt{5}`. Hence :math:`x_M = 2 - \\sqrt{5}`, giving "
            ":math:`|MB| = 1 - (2 - \\sqrt{5}) = \\sqrt{5} - 1 = 2/\\phi` and "
            ":math:`|AM| = (2 - \\sqrt{5}) - (-1) = 3 - \\sqrt{5} = 2/\\phi^2`, so :math:`|MB|/|AM| = \\phi`."
        ),
        notes_prose=(
            "Lattice coordinates supply orthogonal unit and double-unit segments without auxiliary "
            "angle bisections, making lattice-grid constructions popular in recreational and olympiad geometry."
        ),
        terms=("golden-ratio", "golden-section", "quadrance"),
        builder=build_nguyen_2x2_square,
    ),
    ConstructionSpec(
        slug="04-tran-mcgucken-3x3-circle",
        catalog_code="GC-03.04",
        family_slug="03-squares-rectangles",
        order=4,
        title="Tran Quang Hung & Elliot McGucken's 3×3 Grid Circle",
        short_title="3×3 Grid Diagonal Circle",
        discoverers=("tran-quang-hung", "elliot-mcgucken"),
        year="2016",
        citations=("bogomolny-3x3-1", "bogomolny-golden-ratio"),
        ctk_url="https://www.cut-the-knot.org/do_you_know/3x3GoldenRatio.shtml",
        ctk_title="Golden Ratio in 3x3 Square",
        number_field=r"\mathbb{Q}(\sqrt{2}, \phi)",
        number_field_text="Q(√2, φ)",
        enunciation=(
            "In a :math:`3 \\times 3` square grid :g:`S1AS3S4` centered at :g:`O`, let :g:`C` be the "
            "upper-right vertex of the central grid cell, :g:`A` the outer upper-right corner, and :g:`T` "
            "the adjacent trisection vertex on the top edge. Circle :g:`cOT` cuts diagonal segment "
            ":g:`CA` at :g:`B` such that :math:`|CB|/|BA| = \\phi`."
        ),
        given_prose=(
            "A :math:`3 \\times 3` square grid on :math:`[-3, 3]^2` centered at :g:`O` :math:`= (0,0)` "
            "with outer vertex :g:`A` :math:`= (3,3)`."
        ),
        steps_prose=(
            "Identify central cell corner :g:`C` :math:`= (1,1)` and top boundary grid node :g:`T` :math:`= (1,3)`.",
            "Draw diagonal line :g:`OA` through :g:`C` and :g:`A`.",
            "Draw circle :g:`cOT` centered at :g:`O` through :g:`T`, cutting segment :g:`CA` at :g:`B`.",
        ),
        proof_prose=(
            "Circle :g:`cOT` has quadrance radius :math:`Q(O, T) = 1^2 + 3^2 = 10`. Along diagonal "
            ":math:`y = x`, :math:`2x^2 = 10` gives :g:`B` :math:`= (\\sqrt{5}, \\sqrt{5})`. Since "
            "collinear points :math:`C(1,1), B(\\sqrt{5},\\sqrt{5}), A(3,3)` project linearly onto the "
            ":math:`x`-axis, :math:`|CB|/|BA| = (\\sqrt{5} - 1)/(3 - \\sqrt{5}) = \\phi`."
        ),
        notes_prose=(
            "Notice the structural kinship with the Greek Cross (:doc:`../07-bui-cross-and-square/index`): "
            "the four trisection nodes on the boundary of a :math:`3 \\times 3` grid are precisely the "
            "twelve outer corners of a five-square Greek cross."
        ),
        terms=("golden-ratio", "golden-section", "quadrance"),
        builder=build_tran_mcgucken_3x3_circle,
    ),
    ConstructionSpec(
        slug="05-tran-3x3-incenter",
        catalog_code="GC-03.05",
        family_slug="03-squares-rectangles",
        order=5,
        title="Tran Quang Hung's 3×3 Grid Incenter Division",
        short_title="3×3 Grid Incenter",
        discoverers=("tran-quang-hung",),
        year="2016",
        citations=("bogomolny-3x3-2", "bogomolny-golden-ratio"),
        ctk_url="https://www.cut-the-knot.org/do_you_know/3x3GoldenRatio2.shtml",
        ctk_title="Another Golden Ratio in 3x3 Square",
        number_field=r"\mathbb{Q}(\sqrt{2}, \phi)",
        number_field_text="Q(√2, φ)",
        enunciation=(
            "In a :math:`3 \\times 3` grid :g:`AQ1Q2Q3` on :math:`[0,3]^2`, let :g:`S` :math:`= (1,1)` "
            "and :g:`T` :math:`= (2,2)` be opposite corners of the central unit cell, and let :g:`U` :math:`= (3,1)` "
            "and :g:`V` :math:`= (1,3)`. The incenter :g:`P` of isosceles triangle :g:`AUV` divides "
            "diagonal :g:`ST` of the central cell in the golden ratio: :math:`|PT|/|SP| = \\phi`."
        ),
        given_prose=(
            "Outer :math:`3 \\times 3` square :g:`AQ1Q2Q3` with :g:`A` :math:`= (0,0)` and :g:`Q1` :math:`= (3,0)`."
        ),
        steps_prose=(
            "Mark central cell diagonal vertices :g:`S` :math:`= (1,1)` and :g:`T` :math:`= (2,2)` along symmetry axis :g:`AT`.",
            "Form lattice isosceles triangle :g:`AUV` with :g:`U` :math:`= (3,1)` and :g:`V` :math:`= (1,3)` (whose base :g:`UV` has midpoint :g:`T`).",
            "Construct incenter :g:`P` and incircle :g:`cPT` tangent to :g:`UV` at :g:`T`.",
        ),
        proof_prose=(
            "Triangle :g:`AUV` has side lengths :math:`|AU| = |AV| = \\sqrt{10}` and :math:`|UV| = 2\\sqrt{2}`. "
            "By the angle-bisector theorem on altitude :g:`AT` (:math:`|AT| = 2\\sqrt{2}`), "
            ":math:`|PT|/|AP| = (|UV|/2)/|AU| = \\sqrt{2}/\\sqrt{10} = 1/\\sqrt{5}`, so "
            ":math:`x_P = 2 \\cdot \\frac{\\sqrt{5}}{\\sqrt{5} + 1} = \\frac{5 - \\sqrt{5}}{2}`. "
            "Hence :math:`2 - x_P = \\frac{\\sqrt{5}-1}{2} = 1/\\phi` and :math:`x_P - 1 = \\frac{3-\\sqrt{5}}{2} = 1/\\phi^2`, "
            "proving :math:`|PT|/|SP| = \\phi`."
        ),
        notes_prose=(
            "Because :g:`T` is simultaneously a grid vertex and the tangency point of incircle :g:`cPT` on "
            "base :g:`UV`, the inradius of :math:`\\triangle AUV` equals :math:`|PT| = \\sqrt{2}/\\phi`."
        ),
        terms=("golden-ratio", "golden-section"),
        builder=build_tran_3x3_incenter,
    ),
    ConstructionSpec(
        slug="06-suppa-square-inradii",
        catalog_code="GC-03.06",
        family_slug="03-squares-rectangles",
        order=6,
        title="Ercole Suppa's Square Midpoint Inradii Ratio (2015)",
        short_title="Suppa's Square Inradii",
        discoverers=("ercole-suppa",),
        year="2015",
        citations=("bogomolny-suppa-square", "bogomolny-golden-ratio"),
        ctk_url="https://www.cut-the-knot.org/do_you_know/GoldenRatioInSquare.shtml",
        ctk_title="Golden Ratio via Two Incircles in a Square",
        number_field=r"\mathbb{Q}(\phi)",
        number_field_text="Q(φ)",
        enunciation=(
            "In square :g:`ABCD`, let :g:`M` be the midpoint of side :g:`AD`. The inradii :math:`R` "
            "and :math:`r` of triangles :math:`\\triangle BCM` (incircle :g:`cEH`) and :math:`\\triangle CDM` "
            "(incircle :g:`cFP`) satisfy :math:`R / r = \\phi`, and segment :g:`EF` joining their incenters "
            "is divided by :g:`CM` at :g:`K` with :math:`|EK|/|KF| = \\phi`."
        ),
        given_prose=(
            "Square :g:`ABCD` of side :math:`2` with :g:`D` :math:`= (0,0)`, :g:`C` :math:`= (2,0)`, "
            ":g:`B` :math:`= (2,2)`, :g:`A` :math:`= (0,2)` and midpoint :g:`M` :math:`= (0,1)`."
        ),
        steps_prose=(
            "Join :g:`CM` and :g:`BM`, partitioning the lower and right regions into right :math:`\\triangle CDM` and isosceles :math:`\\triangle BCM`.",
            "Inscribe circle :g:`cEH` in :math:`\\triangle BCM` (incenter :g:`E`, tangent to :g:`BC` at :g:`H`) and circle :g:`cFP` in :math:`\\triangle CDM` (incenter :g:`F`, tangent to :g:`CD` at :g:`P`).",
            "Join incenters :g:`EF` to intersect shared side :g:`CM` at :g:`K`.",
        ),
        proof_prose=(
            "For :math:`\\triangle BCM`, area :math:`= 2` and semiperimeter :math:`s_1 = 1 + \\sqrt{5}` "
            "give inradius :math:`R = \\frac{2}{\\sqrt{5}+1} = \\frac{\\sqrt{5}-1}{2} = 1/\\phi`. "
            "For right :math:`\\triangle CDM` with legs :math:`1, 2` and hypotenuse :math:`\\sqrt{5}`, "
            "inradius :math:`r = \\frac{1 + 2 - \\sqrt{5}}{2} = \\frac{3 - \\sqrt{5}}{2} = 1/\\phi^2`. "
            "Since :g:`E` and :g:`F` lie at perpendicular distances :math:`R` and :math:`r` on opposite "
            "sides of shared line :g:`CM`, similar right triangles yield :math:`|EK|/|KF| = R/r = \\phi`."
        ),
        notes_prose=(
            "Suppa's theorem exhibits consecutive negative powers of :math:`\\phi` (:math:`\\phi^{-1}` "
            "and :math:`\\phi^{-2}`, whose sum :math:`\\phi^{-1} + \\phi^{-2} = 1` equals half the side of the square) "
            "as exact Euclidean inradii."
        ),
        terms=("golden-ratio", "golden-section"),
        builder=build_suppa_square_inradii,
    ),
    ConstructionSpec(
        slug="07-bui-cross-and-square",
        catalog_code="GC-03.07",
        family_slug="03-squares-rectangles",
        order=7,
        title="Bùi Quang Tuân & Alexandre Borovik's Greek Cross & Square",
        short_title="Greek Cross & Square",
        discoverers=("bui-quang-tuan", "alexandre-borovik"),
        year="2015",
        citations=("bogomolny-golden-cross", "bogomolny-golden-ratio"),
        ctk_url="https://www.cut-the-knot.org/do_you_know/GoldenCross.shtml",
        ctk_title="Golden Cross and Golden Square",
        number_field=r"\mathbb{Q}(\phi)",
        number_field_text="Q(φ)",
        enunciation=(
            "Inscribe a symmetrical five-square Greek cross :g:`CROSS` and a concentric axis-aligned "
            "square :g:`S1S2S3S4` in the same circle :g:`cO`. Along any inner arm line :g:`AC` of the "
            "cross, the square edge :g:`S1S2` cuts :g:`AC` at :g:`B` such that :math:`|BC|/|AB| = \\phi`, "
            "while :math:`|BD|/|CD| = \\phi`."
        ),
        given_prose=(
            "Circle :g:`cO` centered at :g:`O` :math:`= (0,0)` through cross corner :g:`A` :math:`= (1,3)` "
            "(radius :math:`\\sqrt{10}`)."
        ),
        steps_prose=(
            "Inscribe the five-square Greek cross :g:`CROSS` of square side :math:`2`, with right upper arm edge passing through :g:`A` :math:`= (1,3)`, :g:`C` :math:`= (1,1)`, and :g:`D` :math:`= (1,-1)`.",
            "Inscribe concentric square :g:`S1S2S3S4` of side :math:`2\\sqrt{5}` with vertices :math:`(\\pm\\sqrt{5}, \\pm\\sqrt{5})` on :g:`cO`.",
            "Mark :g:`B` :math:`= (1, \\sqrt{5})` and :g:`E` :math:`= (1, -\\sqrt{5})` where horizontal square edges :g:`S1S2` and :g:`S4S3` meet line :g:`AC`.",
        ),
        proof_prose=(
            "Each cross arm has half-width :math:`1` and outer reach :math:`3`, so :math:`R^2 = 1^2 + 3^2 = 10`. "
            "An axis-aligned square in the same circle satisfies :math:`x^2 + y^2 = 10` with :math:`|x| = |y| = \\sqrt{5}`. "
            "On vertical line :math:`x = 1`, points :math:`A(1,3), B(1,\\sqrt{5}), C(1,1), D(1,-1)` have "
            ":math:`|BC| = \\sqrt{5} - 1 = 2/\\phi`, :math:`|AB| = 3 - \\sqrt{5} = 2/\\phi^2`, and "
            ":math:`|BD| = \\sqrt{5} + 1 = 2\\phi`, giving both :math:`|BC|/|AB| = \\phi` and :math:`|BD|/|CD| = \\phi`."
        ),
        notes_prose=(
            "Alexandre Borovik noted that the overlap between the vertical arm of width :math:`2` and "
            "segment :g:`BD` of height :math:`2\\phi` forms an exact :term:`golden rectangle <golden-rectangle>`."
        ),
        terms=("golden-ratio", "golden-section", "golden-chain", "golden-rectangle"),
        builder=build_bui_cross_and_square,
    ),
    ConstructionSpec(
        slug="08-arioni-rotating-square",
        catalog_code="GC-03.08",
        family_slug="03-squares-rectangles",
        order=8,
        title="John Arioni's 30°-Rotated Unit Square & Diagonal Circle",
        short_title="Arioni's Rotated Square",
        discoverers=("john-arioni",),
        year="2016",
        citations=("bogomolny-arioni-square", "bogomolny-golden-ratio"),
        ctk_url="https://www.cut-the-knot.org/do_you_know/JohnArioni.shtml",
        ctk_title="Golden Ratio by Rotating a Square",
        number_field=r"\mathbb{Q}(\sqrt{3}, \phi)",
        number_field_text="Q(√3, φ)",
        enunciation=(
            "Rotate unit square :g:`DGHJ` clockwise by :math:`30^\\circ` around vertex :g:`D` to obtain "
            "congruent square :g:`DCBA`. Circle :g:`cAC` centered at :g:`A` through opposite vertex :g:`C` "
            "intersects line :g:`DG` at :g:`E` and :g:`F` such that :math:`|DG|/|GE| = |DE|/|DG| = \\phi`."
        ),
        given_prose=(
            "Unit square :g:`DGHJ` on base :g:`D` :math:`= (0,0)`, :g:`G` :math:`= (1,0)`."
        ),
        steps_prose=(
            "Rotate :g:`DGHJ` clockwise by :math:`30^\\circ` about :g:`D` so :g:`A` :math:`= (\\tfrac{1}{2}, \\tfrac{\\sqrt{3}}{2})` and :g:`C` :math:`= (\\tfrac{\\sqrt{3}}{2}, -\\tfrac{1}{2})`.",
            "Draw diagonal :g:`AC` (of length :math:`\\sqrt{2}`) of the rotated unit square :g:`DCBA`.",
            "Draw circle :g:`cAC` centered at :g:`A` through :g:`C`, cutting base line :g:`DG` at :g:`E` and :g:`F`.",
        ),
        proof_prose=(
            "Center :g:`A` has altitude :math:`y_A = \\frac{\\sqrt{3}}{2}` above line :g:`DG` (:math:`y = 0`) "
            "and abscissa :math:`x_A = \\frac{1}{2}`, while radius :math:`|AC| = \\sqrt{2}`. "
            "Setting :math:`y = 0` in :math:`(x - \\tfrac{1}{2})^2 + (\\tfrac{\\sqrt{3}}{2})^2 = 2` gives "
            ":math:`(x - \\tfrac{1}{2})^2 = \\frac{5}{4}`, hence :math:`x_E = \\frac{1 + \\sqrt{5}}{2} = \\phi` "
            "and :math:`x_F = -1/\\phi`, forming the 4-point golden chain :math:`(F, D, G, E)`."
        ),
        notes_prose=(
            "Rotating by :math:`30^\\circ` converts the square's diagonal quadrance :math:`2` minus the "
            "equilateral altitude quadrance :math:`3/4` directly into :math:`5/4`."
        ),
        terms=("golden-ratio", "golden-section", "golden-chain", "quadrance"),
        builder=build_arioni_rotating_square,
    ),
)
