"""Family 06: Circles, Tangent Packings, Yin-Yang & Sangaku Configurations.

Catalogs Bùi Quang Tuân's infinite chord families and four-circle chain,
Elliot McGucken & Thanos Kalogerakis's equal tangent circles, Tran Quang Hung's
three mutually tangent circles, Jerzy Kocik's Golden Window, John Arioni's
Yin-Yang secant, and three congruent circles in a semicircle.
"""

from __future__ import annotations

import sympy as sp

from .helpers import make_result, new_catalog_model
from .schema import ConstructionResult, ConstructionSpec


def build_bui_circle_droves() -> ConstructionResult:
    """Bùi Quang Tuân's infinite rational secant family dividing a radius in phi."""
    m = new_catalog_model("bui-circle-droves")
    s3 = sp.sqrt(3)
    s5 = sp.sqrt(5)

    O = m.set_point(0, 0, classes=["given"], ID="O")
    B = m.set_point(1, 0, classes=["given"], ID="B")
    A = m.set_point(-1, 0, ID="A")

    c_o = m.construct_circle(O, B, classes=["primary"], ID="cO")
    _ = c_o
    ln_ab = m.construct_line(A, B, classes=["golden"], ID="AB")

    # First pair (x1 = 0, y1 = 2/3): C1=(0,1), D1=(2/3, -sqrt(5)/3)
    C1 = m.set_point(0, 1, ID="C1")
    D1 = m.set_point(sp.Rational(2, 3), -s5 / 3, ID="D1")
    ln_c1d1 = m.construct_line(C1, D1, classes=["golden"], ID="C1D1")

    # Second pair (x2 = -1/2, y2 = 7/8): C2=(-1/2, sqrt(3)/2), D2=(7/8, -sqrt(15)/8)
    C2 = m.set_point(-sp.Rational(1, 2), s3 / 2, ID="C2")
    D2 = m.set_point(sp.Rational(7, 8), -(s3 * s5) / 8, ID="D2")
    ln_c2d2 = m.construct_line(C2, D2, classes=["auxiliary"], ID="C2D2")
    _ = ln_c2d2

    m.intersect(ln_c1d1, ln_ab, classes=["golden"], ID="M")

    return make_result(m, ("M", "B"), ("O", "M"), ("O", "M", "B"))


def build_mcgucken_kalogerakis_equal_circles() -> ConstructionResult:
    """Elliot McGucken & Thanos Kalogerakis's two externally tangent equal circles."""
    m = new_catalog_model("mcgucken-kalogerakis-equal-circles")
    B = m.set_point(0, 0, classes=["given"], ID="B")
    C = m.set_point(1, 0, classes=["given"], ID="C")
    D = m.set_point(2, 0, ID="D")
    F = m.set_point(0, 1, ID="F")
    A = m.set_point(0, -1, ID="A")

    m.construct_circle(B, C, classes=["primary"], ID="cB")
    c_d = m.construct_circle(D, C, classes=["primary"], ID="cD")
    m.construct_segment(A, F, classes=["auxiliary"], ID="AF")
    m.construct_line(B, D, classes=["auxiliary"], ID="BD")

    ln_fd = m.construct_line(F, D, classes=["golden"], ID="FD")
    m.intersect(c_d, ln_fd, between=(F, D), classes=["golden"], ID="H")
    m.intersect(c_d, ln_fd, beyond=(F, D), classes=["golden"], ID="I")

    return make_result(m, ("H", "I"), ("F", "H"), ("F", "H", "I"))


def build_bui_four_golden_circles() -> ConstructionResult:
    """Bùi Quang Tuân's four congruent circles generating a vertical golden chain."""
    m = new_catalog_model("bui-four-golden-circles")
    s3 = sp.sqrt(3)
    s15 = sp.sqrt(15)

    A = m.set_point(-sp.Rational(1, 2), 0, classes=["given"], ID="A")
    B = m.set_point(sp.Rational(1, 2), 0, classes=["given"], ID="B")
    c_a = m.construct_circle(A, B, classes=["primary"], ID="cA")
    c_b = m.construct_circle(B, A, classes=["primary"], ID="cB")

    E = m.intersect(c_a, c_b, side_of=(A, B, 1), classes=["golden"], ID="E")
    N = m.intersect(c_a, c_b, side_of=(A, B, -1), classes=["golden"], ID="N")
    ln_axis = m.construct_line(N, E, classes=["golden"], ID="NE")
    _ = ln_axis

    # Congruent unit circles centered at D=(0, sqrt(15)/2) and C=(0, -sqrt(15)/2) tangent to cA, cB
    D = m.set_point(0, s15 / 2, classes=["golden"], ID="D")
    C = m.set_point(0, -s15 / 2, classes=["golden"], ID="C")
    T1 = m.set_point(-sp.Rational(1, 4), s15 / 4, guide=True, ID="T1")
    T2 = m.set_point(-sp.Rational(1, 4), -s15 / 4, guide=True, ID="T2")
    m.construct_circle(D, T1, classes=["golden"], ID="cD")
    m.construct_circle(C, T2, classes=["compass"], ID="cC")
    _ = s3

    return make_result(m, ("E", "N"), ("E", "D"), ("N", "E", "D"))


def build_tran_mcgucken_three_tangent_circles() -> ConstructionResult:
    """Tran Quang Hung & Elliot McGucken's three mutually tangent equal circles."""
    m = new_catalog_model("tran-mcgucken-three-tangent-circles")
    s3 = sp.sqrt(3)

    O = m.set_point(0, 0, classes=["given"], ID="O")
    A = m.set_point(0, 2 * s3 / 3, classes=["given"], ID="A")
    B = m.set_point(-1, -s3 / 3, ID="B")
    C = m.set_point(1, -s3 / 3, ID="C")

    D = m.set_point(0, -s3 / 3, classes=["golden"], ID="D")
    E = m.set_point(sp.Rational(1, 2), s3 / 6, ID="E")
    F = m.set_point(-sp.Rational(1, 2), s3 / 6, classes=["golden"], ID="F")
    _ = E

    m.construct_polygon([A, B, C], classes=["auxiliary"], ID="ABC")
    m.construct_circle(A, F, classes=["compass"], ID="cA")
    m.construct_circle(B, D, classes=["compass"], ID="cB")
    m.construct_circle(C, D, classes=["compass"], ID="cC")
    c_o = m.construct_circle(O, A, classes=["primary"], ID="cO")

    ln_df = m.construct_line(D, F, classes=["golden"], ID="DF")
    m.intersect(c_o, ln_df, beyond=(D, F), classes=["golden"], ID="G")
    J = m.intersect(c_o, ln_df, beyond=(F, D), classes=["golden"], ID="J")
    _ = J

    return make_result(m, ("D", "F"), ("F", "G"), ("D", "F", "G"))


def build_kocik_golden_window() -> ConstructionResult:
    """Jerzy Kocik's six-circle Golden Window Apollonian configuration (2010)."""
    m = new_catalog_model("kocik-golden-window")
    s5 = sp.sqrt(5)
    phi = sp.Rational(1, 2) + s5 / 2
    phi2 = phi + 1
    phi3 = 2 * phi + 1

    O = m.set_point(0, 0, classes=["given"], ID="O")
    P1 = m.set_point(-1, 0, ID="P1")
    P2 = m.set_point(1, 0, classes=["given"], ID="P2")
    C1 = m.set_point(-sp.Rational(1, 2), 0, guide=True, ID="C1")
    C2 = m.set_point(sp.Rational(1, 2), 0, guide=True, ID="C2")

    # Central unit-diameter circles
    m.construct_circle(C1, O, classes=["compass"], ID="cC1")
    m.construct_circle(C2, O, classes=["compass"], ID="cC2")

    # Flanking golden circles of radius phi centered at +-phi^2
    C3 = m.set_point(-phi2, 0, ID="C3")
    C4 = m.set_point(phi2, 0, classes=["golden"], ID="C4")
    A3 = m.set_point(-phi3, 0, ID="A3")
    A4 = m.set_point(phi3, 0, classes=["golden"], ID="A4")
    m.construct_circle(C3, P1, classes=["golden"], ID="cC3")
    m.construct_circle(C4, P2, classes=["golden"], ID="cC4")

    # Outer window circle of radius phi^3 = 2*phi + 1
    m.construct_circle(O, A4, classes=["primary"], ID="cO")
    m.construct_line(A3, A4, classes=["golden"], ID="A3A4")

    # Upper & lower circles tangent to all five circles: center (0, +-2*phi^2/sqrt(5)), top (0, +-phi^3)
    hu = (2 * phi2) / s5
    U1 = m.set_point(0, hu, ID="U1")
    U2 = m.set_point(0, -hu, ID="U2")
    T_top = m.set_point(0, phi3, ID="T1")
    T_bot = m.set_point(0, -phi3, ID="T2")
    m.construct_circle(U1, T_top, classes=["auxiliary"], ID="cU1")
    m.construct_circle(U2, T_bot, classes=["auxiliary"], ID="cU2")

    return make_result(m, ("O", "C4"), ("C4", "A4"), ("O", "C4", "A4"))


def build_arioni_yin_yang() -> ConstructionResult:
    """John Arioni's Golden Ratio secant in the Yin-Yang twin-circle figure."""
    m = new_catalog_model("arioni-yin-yang")
    O = m.set_point(0, 0, classes=["given"], ID="O")
    B = m.set_point(0, 1, classes=["given"], ID="B")
    PL = m.set_point(-1, 0, ID="PL")
    PR = m.set_point(1, 0, ID="PR")
    A = m.set_point(-sp.Rational(1, 2), 0, ID="A")
    C = m.set_point(sp.Rational(1, 2), 0, ID="C")

    m.construct_circle(O, B, classes=["primary"], ID="cO")
    c_a = m.construct_circle(A, O, classes=["golden"], ID="cA")
    m.construct_circle(C, O, classes=["compass"], ID="cC")
    m.construct_segment(PL, PR, classes=["auxiliary"], ID="PLPR")
    m.construct_segment(O, B, classes=["auxiliary"], ID="OB")

    ln_ba = m.construct_line(B, A, classes=["golden"], ID="BA")
    m.intersect(c_a, ln_ba, between=(B, A), classes=["golden"], ID="H")
    m.intersect(c_a, ln_ba, beyond=(B, A), classes=["golden"], ID="I")

    return make_result(m, ("H", "I"), ("B", "H"), ("B", "H", "I"))


def build_three_circles_in_semicircle() -> ConstructionResult:
    """Three tangent unit circles inscribed in a semicircle of radius 2*phi."""
    m = new_catalog_model("three-circles-in-semicircle")
    phi = sp.Rational(1, 2) + sp.sqrt(5) / 2

    O = m.set_point(0, 0, classes=["given"], ID="O")
    T1 = m.set_point(-2, 0, ID="T1")
    T2 = m.set_point(2, 0, classes=["given"], ID="T2")
    C1 = m.set_point(-2, 1, ID="C1")
    C0 = m.set_point(0, 1, ID="C0")
    C2 = m.set_point(2, 1, ID="C2")

    A = m.set_point(-2 * phi, 0, ID="A")
    B = m.set_point(2 * phi, 0, classes=["golden"], ID="B")

    c_o = m.construct_circle(O, B, classes=["primary"], ID="cO")
    m.construct_line(A, B, classes=["golden"], ID="AB")
    m.construct_circle(C1, T1, classes=["compass"], ID="cC1")
    m.construct_circle(C0, O, classes=["compass"], ID="cC0")
    c_c2 = m.construct_circle(C2, T2, classes=["golden"], ID="cC2")

    ln_oc2 = m.construct_line(O, C2, classes=["auxiliary"], ID="OC2")
    S = m.intersect(c_c2, ln_oc2, between=(O, C2), classes=["golden"], ID="S")
    K = m.intersect(c_o, ln_oc2, side_of=(B, A, 1), classes=["golden"], ID="K")
    _ = (S, K)

    return make_result(m, ("O", "T2"), ("T2", "B"), ("O", "T2", "B"))


CIRCLES_SANGAKU_SPECS: tuple[ConstructionSpec, ...] = (
    ConstructionSpec(
        slug="01-bui-circle-droves",
        catalog_code="GC-06.01",
        family_slug="06-circles-sangaku",
        order=1,
        title="Bùi Quang Tuân's Infinite Family of Golden Circle Secants",
        short_title="Golden Circle Secants in Droves",
        discoverers=("bui-quang-tuan",),
        year="2014",
        citations=("bogomolny-bui-general", "bogomolny-bui-1", "bogomolny-golden-ratio"),
        ctk_url="https://www.cut-the-knot.org/do_you_know/BuiGoldenRatioGeneral.shtml",
        ctk_title="Golden Ratio in Circle — in Droves",
        number_field=r"\mathbb{Q}(\sqrt{3}, \phi)",
        number_field_text="Q(√3, φ)",
        enunciation=(
            "In unit circle :g:`cO` on diameter :g:`AB`, infinitely many rational-abscissa point pairs "
            "on opposite semicircles—including :g:`C1` :math:`= (0,1)`, :g:`D1` :math:`= (\\tfrac{2}{3}, -\\tfrac{\\sqrt{5}}{3})` "
            "and :g:`C2` :math:`= (-\\tfrac{1}{2}, \\tfrac{\\sqrt{3}}{2})`, :g:`D2` :math:`= (\\tfrac{7}{8}, -\\tfrac{\\sqrt{15}}{8})`—"
            "concur on radius :g:`OB` at the exact golden point :g:`M` :math:`= (1/\\phi^2, 0)` where :math:`|MB|/|OM| = \\phi`."
        ),
        given_prose=(
            "Unit circle :g:`cO` centered at :g:`O` :math:`= (0,0)` with diameter :g:`A` :math:`= (-1,0)` "
            "to :g:`B` :math:`= (1,0)`."
        ),
        steps_prose=(
            "Plot upper apex :g:`C1` :math:`= (0,1)` and lower chord point :g:`D1` at abscissa :math:`x = \\tfrac{2}{3}` on :g:`cO`.",
            "Plot a second rational-abscissa pair :g:`C2` at :math:`x = -\\tfrac{1}{2}` and :g:`D2` at :math:`x = \\tfrac{7}{8}` on opposite semicircles.",
            "Draw chords :g:`C1D1` and :g:`C2D2`, which concur on :g:`OB` at :g:`M` :math:`= (\\tfrac{3-\\sqrt{5}}{2}, 0)`.",
        ),
        proof_prose=(
            "For :math:`C(x, \\sqrt{1-x^2})` and :math:`D(y, -\\sqrt{1-y^2})`, chord :math:`CD` crosses "
            ":math:`AB` at :math:`x_M = \\frac{x\\sqrt{1-y^2} + y\\sqrt{1-x^2}}{\\sqrt{1-x^2} + \\sqrt{1-y^2}}`. "
            "Setting :math:`x_M = \\frac{3 - \\sqrt{5}}{2} = \\frac{1}{\\phi^2}` yields Bùi Quang Tuân's "
            "Diophantine condition :math:`\\frac{5(1 - x^2)}{1 - y^2} = \\left(\\frac{3 - 2y}{1 - 2x}\\right)^2`, "
            "satisfied simultaneously by :math:`(0, \\tfrac{2}{3})`, :math:`(-\\tfrac{1}{2}, \\tfrac{7}{8})`, "
            "and infinitely many rational pairs."
        ),
        notes_prose=(
            "At :g:`M`, :math:`|OM| = 1/\\phi^2` and :math:`|MB| = 1 - 1/\\phi^2 = 1/\\phi`, so "
            ":math:`|MB|/|OM| = |OB|/|MB| = \\phi`."
        ),
        terms=("golden-ratio", "golden-section"),
        builder=build_bui_circle_droves,
    ),
    ConstructionSpec(
        slug="02-mcgucken-kalogerakis-equal-circles",
        catalog_code="GC-06.02",
        family_slug="06-circles-sangaku",
        order=2,
        title="Elliot McGucken & Thanos Kalogerakis's Equal Tangent Circles",
        short_title="Two Equal Tangent Circles",
        discoverers=("elliot-mcgucken", "thanos-kalogerakis"),
        year="2016",
        citations=("bogomolny-mcgucken-1", "bogomolny-kalogerakis", "bogomolny-golden-ratio"),
        ctk_url="https://www.cut-the-knot.org/do_you_know/ElliotMcGucken1.shtml",
        ctk_title="Golden Ratio in Two Equal Circles",
        number_field=r"\mathbb{Q}(\phi)",
        number_field_text="Q(φ)",
        enunciation=(
            "Let equal unit circles :g:`cB` and :g:`cD` touch externally at :g:`C`, and let :g:`AF` "
            "be the diameter of :g:`cB` perpendicular to line of centers :g:`BD`. Secant :g:`FD` cuts "
            ":g:`cD` at :g:`H` and :g:`I` such that :math:`|HI|/|FH| = |FI|/|HI| = |FI|/|AF| = \\phi`."
        ),
        given_prose=(
            "Externally tangent unit circles :g:`cB` at :g:`B` :math:`= (0,0)` and :g:`cD` at "
            ":g:`D` :math:`= (2,0)`, touching at :g:`C` :math:`= (1,0)`."
        ),
        steps_prose=(
            "Erect perpendicular diameter :g:`AF` of :g:`cB` with :g:`F` :math:`= (0,1)` and :g:`A` :math:`= (0,-1)`.",
            "Draw secant line :g:`FD` through center :g:`D` of circle :g:`cD`.",
            "Mark intersections :g:`H` (near) and :g:`I` (far) of :g:`FD` with :g:`cD`.",
        ),
        proof_prose=(
            "Right triangle :math:`\\triangle FBD` has legs :math:`|BF| = 1` and :math:`|BD| = 2`, "
            "giving :math:`|FD| = \\sqrt{5}`. Subtracting and adding radius :math:`1` of :g:`cD` yields "
            ":math:`|FH| = \\sqrt{5} - 1 = 2/\\phi`, diameter :math:`|HI| = 2`, and :math:`|FI| = \\sqrt{5} + 1 = 2\\phi`. "
            "Hence :math:`|HI|/|FH| = \\phi` (McGucken) and :math:`|FI|/|AF| = \\phi` (Kalogerakis)."
        ),
        notes_prose=(
            "This construction geometricizes the Heron-Ptolemy :math:`1\\text{-}2\\text{-}\\sqrt{5}` "
            "right triangle purely through two tangent unit circles."
        ),
        terms=("golden-ratio", "golden-section", "power-of-a-point"),
        builder=build_mcgucken_kalogerakis_equal_circles,
    ),
    ConstructionSpec(
        slug="03-bui-four-golden-circles",
        catalog_code="GC-06.03",
        family_slug="06-circles-sangaku",
        order=3,
        title="Bùi Quang Tuân's Four Congruent Golden Circles",
        short_title="Four Congruent Circles",
        discoverers=("bui-quang-tuan",),
        year="2015",
        citations=("bogomolny-four-circles", "bogomolny-golden-ratio"),
        ctk_url="https://www.cut-the-knot.org/do_you_know/FourGoldenCircles.shtml",
        ctk_title="Four Golden Circles",
        number_field=r"\mathbb{Q}(\sqrt{3}, \phi)",
        number_field_text="Q(√3, φ)",
        enunciation=(
            "Let unit circles :g:`cA` and :g:`cB` pass through each other's centers, intersecting at "
            ":g:`E` and :g:`N`, and let congruent unit circles :g:`cD` and :g:`cC` be externally tangent "
            "to both :g:`cA` and :g:`cB`. Then :math:`(C, N, E, D)` is a 4-point golden chain with "
            ":math:`|EN|/|ED| = |ND|/|EN| = \\phi`."
        ),
        given_prose=(
            "Unit vesica piscis circles :g:`cA` and :g:`cB` centered at :g:`A` :math:`= (-\\tfrac{1}{2}, 0)` "
            "and :g:`B` :math:`= (\\tfrac{1}{2}, 0)`."
        ),
        steps_prose=(
            "Mark lens vertices :g:`E` :math:`= (0, \\tfrac{\\sqrt{3}}{2})` and :g:`N` :math:`= (0, -\\tfrac{\\sqrt{3}}{2})` on symmetry axis :g:`NE`.",
            "Locate centers :g:`D` :math:`= (0, \\tfrac{\\sqrt{15}}{2})` and :g:`C` :math:`= (0, -\\tfrac{\\sqrt{15}}{2})` at distance :math:`2` from both :g:`A` and :g:`B`.",
            "Draw congruent unit circles :g:`cD` and :g:`cC` externally tangent to :g:`cA` and :g:`cB`.",
        ),
        proof_prose=(
            "External tangency of unit circle :g:`cD` to :g:`cA` and :g:`cB` requires :math:`|AD| = |BD| = 2`. "
            "Since :math:`|AM| = 1/2`, :math:`y_D = \\sqrt{2^2 - (1/2)^2} = \\frac{\\sqrt{15}}{2}`, whereas "
            ":math:`y_E = \\frac{\\sqrt{3}}{2}`. Consequently :math:`|EN| = \\sqrt{3}` and "
            ":math:`|ED| = \\frac{\\sqrt{15} - \\sqrt{3}}{2} = \\frac{\\sqrt{3}}{\\phi}`, giving "
            ":math:`|EN|/|ED| = \\phi`."
        ),
        notes_prose=(
            "Compare this four-circle packing directly with Hofstetter's Mascheroni compass-only "
            "construction (:doc:`../../01-minimal-compass/05-hofstetter-compass-only/index`), which uses "
            "the same :math:`\\sqrt{15}/2` vs. :math:`\\sqrt{3}/2` radical ratio."
        ),
        terms=("golden-ratio", "golden-section", "golden-chain", "vesica-piscis"),
        builder=build_bui_four_golden_circles,
    ),
    ConstructionSpec(
        slug="04-tran-mcgucken-three-tangent-circles",
        catalog_code="GC-06.04",
        family_slug="06-circles-sangaku",
        order=4,
        title="Tran Quang Hung & Elliot McGucken's Three Tangent Circles",
        short_title="Three Tangent Circles",
        discoverers=("tran-quang-hung", "elliot-mcgucken"),
        year="2016",
        citations=("bogomolny-3-tangent", "bogomolny-golden-ratio"),
        ctk_url="https://www.cut-the-knot.org/do_you_know/3TangentCirclesGoldenRatio.shtml",
        ctk_title="Golden Ratio in Three Tangent Circles",
        number_field=r"\mathbb{Q}(\sqrt{3}, \phi)",
        number_field_text="Q(√3, φ)",
        enunciation=(
            "Let congruent unit circles :g:`cA`, :g:`cB`, :g:`cC` be mutually externally tangent at "
            ":g:`D`, :g:`E`, :g:`F`, and let circle :g:`cO` pass through their centers :g:`A`, :g:`B`, :g:`C`. "
            "Line :g:`DF` intersects :g:`cO` at :g:`J` and :g:`G` to form a 4-point golden chain "
            ":math:`|DF|/|FG| = |DG|/|DF| = \\phi`."
        ),
        given_prose=(
            "Equilateral center triangle :g:`ABC` of side :math:`2` centered at :g:`O` :math:`= (0,0)` "
            "with :g:`A` :math:`= (0, \\tfrac{2\\sqrt{3}}{3})`."
        ),
        steps_prose=(
            "Draw mutually tangent unit circles :g:`cA`, :g:`cB`, :g:`cC` touching at midpoints :g:`D`, :g:`E`, :g:`F` of :g:`ABC`.",
            "Draw circumcircle :g:`cO` of radius :math:`\\tfrac{2\\sqrt{3}}{3}` through centers :g:`A`, :g:`B`, :g:`C`.",
            "Extend midline :g:`DF` across :g:`cO` to obtain intersections :g:`G` and :g:`J`.",
        ),
        proof_prose=(
            "Because :g:`D`, :g:`E`, :g:`F` are the midpoints of equilateral :g:`ABC` inscribed in :g:`cO`, "
            "chord :g:`JG` along midline :g:`DF` reproduces George Odom's configuration (:doc:`../../02-equilateral-hexagon/01-odom-equilateral/index`) "
            "inside the three-circle packing: :math:`|DF| = 1` and :math:`|FG| = |DJ| = \\frac{\\sqrt{5}-1}{2} = 1/\\phi`, "
            "hence :math:`|DF|/|FG| = \\phi`."
        ),
        notes_prose=(
            "Furthermore, extending :g:`DF` across :g:`cC` adds another unit chord segment beyond :g:`D`, "
            "weaving six circle intersections along a single line."
        ),
        terms=("golden-ratio", "golden-section", "golden-chain", "intersecting-chords-theorem"),
        builder=build_tran_mcgucken_three_tangent_circles,
    ),
    ConstructionSpec(
        slug="05-kocik-golden-window",
        catalog_code="GC-06.05",
        family_slug="06-circles-sangaku",
        order=5,
        title="Jerzy Kocik's Six-Circle Apollonian Golden Window (2010)",
        short_title="Kocik's Golden Window",
        discoverers=("jerzy-kocik",),
        year="2010",
        citations=("kocik-2010", "bogomolny-golden-window"),
        ctk_url="https://www.cut-the-knot.org/do_you_know/GoldenWindow.shtml",
        ctk_title="Golden Window",
        number_field=r"\mathbb{Q}(\phi)",
        number_field_text="Q(φ)",
        enunciation=(
            "Place two unit-diameter circles :g:`cC1`, :g:`cC2` tangent at :g:`O` and two flanking "
            "congruent circles :g:`cC3`, :g:`cC4` inside outer circle :g:`cO`. Requiring symmetric "
            "upper and lower circles :g:`cU1`, :g:`cU2` to be simultaneously tangent to all five circles "
            "uniquely forces the flanking circles to have exact radius :math:`\\phi`, outer radius "
            ":math:`\\phi^3`, and :math:`|OC4|/|C4A4| = \\phi`."
        ),
        given_prose=(
            "Origin :g:`O` :math:`= (0,0)` and tangency point :g:`P2` :math:`= (1,0)` defining central "
            "unit-diameter circles :g:`cC1` and :g:`cC2`."
        ),
        steps_prose=(
            "Construct central circles :g:`cC1` and :g:`cC2` of radius :math:`\\tfrac{1}{2}` touching at :g:`O` and reaching :g:`P1`, :g:`P2` :math:`= (\\pm 1, 0)`.",
            "Construct flanking circles :g:`cC3` and :g:`cC4` of radius :math:`\\phi` centered at :g:`C3`, :g:`C4` :math:`= (\\pm \\phi^2, 0)` inside outer circle :g:`cO` of radius :math:`\\phi^3`.",
            "Inscribe symmetric circles :g:`cU1` and :g:`cU2` of radius :math:`\\phi^3/\\sqrt{5}` centered at :math:`(0, \\pm 2\\phi^2/\\sqrt{5})`, tangent to all five circles.",
        ),
        proof_prose=(
            "Let flanking circles have unknown radius :math:`R`, so outer circle :g:`cO` has radius "
            ":math:`1 + 2R`. For upper circle :g:`cU1` of radius :math:`r_u` at :math:`(0, 1 + 2R - r_u)`, "
            "tangency to :g:`cC2` gives :math:`(1/2)^2 + (1 + 2R - r_u)^2 = (r_u + 1/2)^2`, while "
            "tangency to :g:`cC4` gives :math:`(1 + R)^2 + (1 + 2R - r_u)^2 = (r_u + R)^2`. Eliminating "
            ":math:`r_u` yields :math:`R^2 - R - 1 = 0`, uniquely forcing :math:`R = \\phi`!"
        ),
        notes_prose=(
            "Published by Jerzy Kocik in *Mathematics Magazine* (2010), the Golden Window embeds "
            "powers :math:`1, \\phi, \\phi^2, \\phi^3`, golden rectangles, and Kepler's right triangle "
            "in a single rigid Apollonian circle gasket."
        ),
        terms=("golden-ratio", "golden-section", "golden-chain", "kepler-triangle", "golden-rectangle"),
        builder=build_kocik_golden_window,
    ),
    ConstructionSpec(
        slug="06-arioni-yin-yang",
        catalog_code="GC-06.06",
        family_slug="06-circles-sangaku",
        order=6,
        title="John Arioni's Golden Secant in the Yin-Yang Circle",
        short_title="Yin-Yang Twin Circles",
        discoverers=("john-arioni",),
        year="2016",
        citations=("bogomolny-yin-yang", "bogomolny-golden-ratio"),
        ctk_url="https://www.cut-the-knot.org/do_you_know/GoldenRatioInYinYang.shtml",
        ctk_title="Golden Ratio in Yin-Yang",
        number_field=r"\mathbb{Q}(\phi)",
        number_field_text="Q(φ)",
        enunciation=(
            "Inscribe twin tangent circles :g:`cA` and :g:`cC` of radius :math:`\\tfrac{1}{2}` along "
            "horizontal diameter :g:`PLPR` of unit circle :g:`cO`, and let :g:`B` be the apex of "
            "perpendicular radius :g:`OB`. Secant :g:`BA` cuts :g:`cA` at :g:`H` and :g:`I` such that "
            ":math:`|HI|/|BH| = |BI|/|HI| = \\phi`."
        ),
        given_prose=(
            "Unit circle :g:`cO` centered at :g:`O` :math:`= (0,0)` with apex :g:`B` :math:`= (0,1)`."
        ),
        steps_prose=(
            "Bisect radii :g:`OPL` and :g:`OPR` at :g:`A` :math:`= (-\\tfrac{1}{2}, 0)` and :g:`C` :math:`= (\\tfrac{1}{2}, 0)` and draw inner circles :g:`cA` and :g:`cC` through :g:`O`.",
            "Join apex :g:`B` to center :g:`A` of circle :g:`cA`.",
            "Mark intersections :g:`H` and :g:`I` of secant :g:`BA` with :g:`cA`.",
        ),
        proof_prose=(
            "Right triangle :math:`\\triangle AOB` has legs :math:`|OA| = 1/2` and :math:`|OB| = 1`, "
            "so :math:`|BA| = \\sqrt{5}/2`. Since circle :g:`cA` has radius :math:`1/2` and diameter "
            ":math:`|HI| = 1`, we obtain :math:`|BH| = \\frac{\\sqrt{5}-1}{2} = 1/\\phi` and "
            ":math:`|BI| = \\frac{\\sqrt{5}+1}{2} = \\phi`, proving :math:`|HI|/|BH| = |BI|/|HI| = \\phi`."
        ),
        notes_prose=(
            "Notice that :g:`BO` is tangent to both inner circles :g:`cA` and :g:`cC` at :g:`O`, "
            "making :math:`|BO|^2 = |BH|\\cdot|BI| = 1` an immediate instance of Euclid III.36."
        ),
        terms=("golden-ratio", "golden-section", "power-of-a-point"),
        builder=build_arioni_yin_yang,
    ),
    ConstructionSpec(
        slug="07-three-circles-in-semicircle",
        catalog_code="GC-06.07",
        family_slug="06-circles-sangaku",
        order=7,
        title="Three Tangent Equal Circles Inscribed in a Semicircle",
        short_title="Three Circles in a Semicircle",
        discoverers=("alexander-bogomolny",),
        year="2010",
        citations=("bogomolny-golden-ratio",),
        ctk_url="https://www.cut-the-knot.org/do_you_know/GoldenRatio.shtml",
        ctk_title="Golden Ratio in Three Tangent Circles in a Semicircle",
        number_field=r"\mathbb{Q}(\phi)",
        number_field_text="Q(φ)",
        enunciation=(
            "Three congruent unit circles :g:`cC1`, :g:`cC0`, :g:`cC2` stand in a tangent row on "
            "diameter :g:`AB` of enclosing circle :g:`cO` centered at :g:`O`, touching :g:`AB` at "
            ":g:`T1`, :g:`O`, :g:`T2` and touching :g:`cO` internally. Then :g:`cO` has radius "
            ":math:`2\\phi` and :g:`T2` divides :g:`OB` in the golden ratio: :math:`|OT2|/|T2B| = \\phi`."
        ),
        given_prose=(
            "Origin :g:`O` :math:`= (0,0)` and outer circle base tangency :g:`T2` :math:`= (2,0)`."
        ),
        steps_prose=(
            "Erect three tangent unit circles :g:`cC1`, :g:`cC0`, :g:`cC2` centered at :math:`(-2,1), (0,1), (2,1)` resting on :g:`AB`.",
            "Join :g:`O` to outer center :g:`C2` :math:`= (2,1)` (:math:`|OC2| = \\sqrt{5}`) and extend by unit radius :math:`1` to outer tangency :g:`K`.",
            "Draw enclosing circle :g:`cO` of radius :math:`|OK| = \\sqrt{5} + 1 = 2\\phi`, cutting base line :g:`AB` at :g:`A` and :g:`B`.",
        ),
        proof_prose=(
            "Center :g:`C2` :math:`= (2,1)` lies at distance :math:`\\sqrt{2^2 + 1^2} = \\sqrt{5}` from "
            ":g:`O`, so internal tangency of unit circle :g:`cC2` to :g:`cO` gives enclosing radius "
            ":math:`R = \\sqrt{5} + 1 = 2\\phi`. Along radius :g:`OB`, :math:`|OT2| = 2` and "
            ":math:`|T2B| = 2\\phi - 2 = 2/\\phi`, hence :math:`|OT2|/|T2B| = \\phi` (and simultaneously "
            "along :g:`OK`, :math:`|SK|/|OS| = 2 / (\\sqrt{5}-1) = \\phi`)."
        ),
        notes_prose=(
            "In the Japanese *Sangaku* temple-tablet tradition, packing three equal circles inside a "
            "semicircle yields :math:`R / r = 2\\phi` as the fundamental enclosing ratio."
        ),
        terms=("golden-ratio", "golden-section"),
        builder=build_three_circles_in_semicircle,
    ),
)
