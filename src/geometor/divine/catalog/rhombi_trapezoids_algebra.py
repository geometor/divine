"""Family 07: Rhombi, Trapezoids, Mixtilinear Circles & Dissection Paradoxes.

Catalogs Tran Quang Hung's 1:2 rhombus incircle, 60-degree isosceles trapezoid,
and equilateral mixtilinear circle theorems, John Molokach's golden rhombus
from shifted 1x3 rectangles, Jingcheng Tong's area-bisecting trapezoid chord,
and the exact phi-limit resolution of the Hooper-Curry Fibonacci dissection.
"""

from __future__ import annotations

import sympy as sp

from .helpers import make_result, new_catalog_model
from .schema import ConstructionResult, ConstructionSpec


def build_tran_rhombus_incircle() -> ConstructionResult:
    """Tran Quang Hung's rhombus with diagonal ratio 2:1 and its incircle (Buratino 8)."""
    m = new_catalog_model("tran-rhombus-incircle")
    s5 = sp.sqrt(5)

    O = m.set_point(0, 0, classes=["given"], ID="O")
    A = m.set_point(0, s5, ID="A")
    C = m.set_point(0, -s5, ID="C")
    B = m.set_point(2 * s5, 0, classes=["given"], ID="B")
    D = m.set_point(-2 * s5, 0, ID="D")

    m.construct_polygon([A, B, C, D], ID="ABCD")
    m.construct_segment(A, C, classes=["auxiliary"], ID="AC")
    ln_bd = m.construct_line(D, B, classes=["golden"], ID="DB")

    # Inradius r = (2*sqrt(5) * sqrt(5)) / 5 = 2; tangency on AB at H = (2/sqrt(5), 4/sqrt(5))
    F = m.set_point(2, 0, classes=["golden"], ID="F")
    c_o = m.construct_circle(O, F, classes=["golden"], ID="cO")
    m.intersect(c_o, ln_bd, other_than=F, classes=["golden"], ID="E")

    return make_result(m, ("E", "F"), ("F", "B"), ("E", "F", "B"))


def build_molokach_golden_rhombus() -> ConstructionResult:
    """John Molokach's golden rhombus from two shifted 1x3 rectangles and a unit circle."""
    m = new_catalog_model("molokach-golden-rhombus")
    phi = sp.Rational(1, 2) + sp.sqrt(5) / 2
    inv_phi = phi - 1

    O = m.set_point(0, 0, classes=["given"], ID="O")
    T1 = m.set_point(0, 1, classes=["golden"], ID="T1")
    T2 = m.set_point(0, -1, ID="T2")
    _ = T2

    # Two shifted 3x1 rectangles [-2, 1] x [0, 1] and [-1, 2] x [-1, 0]
    R1 = m.set_point(-2, 1, ID="R1")
    K = m.set_point(1, 1, classes=["given"], ID="K")
    R2 = m.set_point(1, 0, guide=True, ID="R2")
    R3 = m.set_point(-2, 0, guide=True, ID="R3")
    m.construct_polygon([R1, K, R2, R3], classes=["auxiliary"], ID="RECT1")

    R4 = m.set_point(-1, 0, guide=True, ID="R4")
    R5 = m.set_point(2, 0, guide=True, ID="R5")
    R6 = m.set_point(2, -1, ID="R6")
    R7 = m.set_point(-1, -1, ID="R7")
    m.construct_polygon([R4, R5, R6, R7], classes=["auxiliary"], ID="RECT2")

    # Long diagonal R1 R6 and unit incircle cO
    m.construct_segment(R1, R6, classes=["auxiliary"], ID="R1R6")
    m.construct_circle(O, T1, classes=["primary"], ID="cO")

    # Golden rhombus ABCD circumscribed about cO via tangents at y=+-1 and 2x - y = +-sqrt(5)
    A = m.set_point(phi, 1, classes=["golden"], ID="A")
    B = m.set_point(-inv_phi, 1, classes=["golden"], ID="B")
    C = m.set_point(-phi, -1, ID="C")
    D = m.set_point(inv_phi, -1, ID="D")
    m.construct_polygon([A, B, C, D], classes=["golden"], ID="ABCD")
    m.construct_line(B, A, classes=["golden"], ID="BA")
    m.construct_segment(A, C, classes=["auxiliary"], ID="AC")
    m.construct_segment(B, D, classes=["auxiliary"], ID="BD")

    return make_result(m, ("T1", "K"), ("K", "A"), ("T1", "K", "A"))


def build_tong_trapezoid_rms() -> ConstructionResult:
    """Jingcheng Tong's area-bisecting chord in a trapezoid of base ratio 1:3."""
    m = new_catalog_model("tong-trapezoid-rms")
    s5 = sp.sqrt(5)

    A = m.set_point(-1, 2, classes=["given"], ID="A")
    D = m.set_point(1, 2, ID="D")
    B = m.set_point(-3, 0, classes=["given"], ID="B")
    C = m.set_point(3, 0, ID="C")

    m.construct_polygon([A, B, C, D], ID="ABCD")
    ln_ab = m.construct_line(A, B, classes=["golden"], ID="AB")
    ln_cd = m.construct_line(D, C, classes=["auxiliary"], ID="DC")

    # Area-bisecting parallel chord MN of RMS length sqrt((2^2 + 6^2)/2) = 2*sqrt(5) at y = 3 - sqrt(5)
    M = m.set_point(-s5, 3 - s5, classes=["golden"], ID="M")
    N = m.set_point(s5, 3 - s5, classes=["golden"], ID="N")
    _ = (ln_ab, ln_cd)
    m.construct_line(M, N, classes=["golden"], ID="MN")

    return make_result(m, ("A", "M"), ("M", "B"), ("A", "M", "B"))


def build_tran_isosceles_trapezoid_60() -> ConstructionResult:
    """Tran Quang Hung's 60-degree half-hexagon trapezoid & reflected compass arc."""
    m = new_catalog_model("tran-isosceles-trapezoid-60")
    s3 = sp.sqrt(3)

    D = m.set_point(-2, 0, classes=["given"], ID="D")
    C = m.set_point(2, 0, classes=["given"], ID="C")
    B = m.set_point(1, s3, ID="B")
    A = m.set_point(-1, s3, ID="A")
    K = m.set_point(3, -s3, ID="K")

    m.construct_polygon([A, B, C, D], ID="ABCD")
    m.construct_line(B, K, classes=["auxiliary"], ID="BK")
    ln_ac = m.construct_line(A, C, classes=["golden"], ID="AC")

    c_kb = m.construct_circle(K, B, classes=["golden"], ID="cKB")
    m.intersect(c_kb, ln_ac, between=(A, C), classes=["golden"], ID="M")

    return make_result(m, ("C", "M"), ("M", "A"), ("A", "M", "C"))


def build_tran_mixtilinear_equilateral() -> ConstructionResult:
    """Tran Quang Hung's Golden Ratio in a mixtilinear circle of an equilateral triangle."""
    m = new_catalog_model("tran-mixtilinear-equilateral")
    s3 = sp.sqrt(3)

    # Side 18 equilateral triangle ABC => all key points have exact integer * radical coordinates
    A = m.set_point(-9, 0, classes=["given"], ID="A")
    B = m.set_point(9, 0, classes=["given"], ID="B")
    C = m.set_point(0, 9 * s3, ID="C")
    K = m.set_point(0, 3 * s3, ID="K")

    m.construct_polygon([A, B, C], ID="ABC")
    m.construct_circle(K, C, classes=["primary"], ID="cK")

    # A-mixtilinear incircle centered at F=(3, 4*sqrt(3)), tangent to AB at D=(3,0) and (ABC) at T=(9, 6*sqrt(3))
    D = m.set_point(3, 0, ID="D")
    F = m.set_point(3, 4 * s3, ID="F")
    c_f = m.construct_circle(F, D, classes=["golden"], ID="cF")

    # Horizontal line through circumcenter K=(0, 3*sqrt(3)) meets BC at O=(6, 3*sqrt(3))
    O = m.set_point(6, 3 * s3, classes=["golden"], ID="O")
    ln_ko = m.construct_line(K, O, classes=["golden"], ID="KO")

    I = m.intersect(c_f, ln_ko, beyond=(O, K), classes=["golden"], ID="I")
    m.intersect(c_f, ln_ko, beyond=(K, O), classes=["golden"], ID="J")
    _ = I

    return make_result(m, ("K", "O"), ("O", "J"), ("K", "O", "J"))


def build_curry_hooper_dissection() -> ConstructionResult:
    """Exact phi-limit resolution of the Hooper (1794) / Curry Fibonacci dissection."""
    m = new_catalog_model("curry-hooper-dissection")
    phi = sp.Rational(1, 2) + sp.sqrt(5) / 2
    inv_phi = phi - 1
    phi2 = phi + 1
    phi3 = 2 * phi + 1

    # Golden rectangle ABCD of width phi^3 and height phi (area = phi^4 = (phi^2)^2, zero gap!)
    A = m.set_point(0, 0, classes=["given"], ID="A")
    B = m.set_point(phi3, 0, classes=["given"], ID="B")
    C = m.set_point(phi3, phi, ID="C")
    D = m.set_point(0, phi, ID="D")
    m.construct_polygon([A, B, C, D], ID="ABCD")

    # Four-piece exact dissection cuts: E=(phi^2, 0), F=(phi, phi), P=(phi^2, 1), Q=(phi, 1/phi)
    E = m.set_point(phi2, 0, ID="E")
    F = m.set_point(phi, phi, ID="F")
    P = m.set_point(phi2, 1, classes=["golden"], ID="P")
    Q = m.set_point(phi, inv_phi, classes=["golden"], ID="Q")

    m.construct_line(A, C, classes=["golden"], ID="AC")
    m.construct_segment(E, P, classes=["auxiliary"], ID="EP")
    m.construct_segment(F, Q, classes=["auxiliary"], ID="FQ")
    m.construct_polygon([A, E, P], classes=["auxiliary"], ID="AEP")
    m.construct_polygon([C, F, Q], classes=["auxiliary"], ID="CFQ")

    return make_result(m, ("A", "Q"), ("Q", "P"), ("A", "Q", "P"))


RHOMBI_TRAPEZOIDS_ALGEBRA_SPECS: tuple[ConstructionSpec, ...] = (
    ConstructionSpec(
        slug="01-tran-rhombus-incircle",
        catalog_code="GC-07.01",
        family_slug="07-rhombi-trapezoids-algebra",
        order=1,
        title="Tran Quang Hung's 2:1 Rhombus & Incircle Diagonal Division",
        short_title="2:1 Rhombus Incircle",
        discoverers=("tran-quang-hung",),
        year="2015",
        citations=("bogomolny-buratino8", "bogomolny-golden-ratio"),
        ctk_url="https://www.cut-the-knot.org/do_you_know/Buratino8.shtml",
        ctk_title="Golden Ratio in Rhombus",
        number_field=r"\mathbb{Q}(\phi)",
        number_field_text="Q(φ)",
        enunciation=(
            "Let :g:`ABCD` be a rhombus whose diagonals satisfy :math:`|DB| = 2|AC|`, and let :g:`cO` "
            "be its inscribed circle. Circle :g:`cO` intersects long diagonal :g:`DB` at :g:`E` and "
            ":g:`F` to form a 4-point golden chain: :math:`|EF|/|FB| = |EB|/|EF| = \\phi`."
        ),
        given_prose=(
            "Rhombus :g:`ABCD` centered at :g:`O` :math:`= (0,0)` with :g:`B` :math:`= (2\\sqrt{5}, 0)` "
            "and :g:`A` :math:`= (0, \\sqrt{5})`."
        ),
        steps_prose=(
            "Construct rhombus :g:`ABCD` of side :math:`5` with semi-diagonals :math:`|OB| = 2\\sqrt{5}` and :math:`|OA| = \\sqrt{5}`.",
            "Inscribe circle :g:`cO` of radius :math:`r = 2` tangent to all four sides of :g:`ABCD`.",
            "Mark intersections :g:`E` :math:`= (-2,0)` and :g:`F` :math:`= (2,0)` of :g:`cO` with diagonal :g:`DB`.",
        ),
        proof_prose=(
            "Right triangle :math:`\\triangle AOB` has legs :math:`\\sqrt{5}` and :math:`2\\sqrt{5}`, "
            "hypotenuse :math:`|AB| = 5`, and altitude (inradius) :math:`r = \\frac{\\sqrt{5}\\cdot 2\\sqrt{5}}{5} = 2`. "
            "Thus diameter :math:`|EF| = 4`, while :math:`|FB| = 2\\sqrt{5} - 2 = 2(\\sqrt{5}-1) = 4/\\phi`, "
            "giving :math:`|EF|/|FB| = \\phi`."
        ),
        notes_prose=(
            "Scaling the semi-diagonals by :math:`\\sqrt{5}` makes both the rhombus side (:math:`5`) "
            "and the inradius (:math:`2`) pure rational integers."
        ),
        terms=("golden-ratio", "golden-section", "golden-chain"),
        builder=build_tran_rhombus_incircle,
    ),
    ConstructionSpec(
        slug="02-molokach-golden-rhombus",
        catalog_code="GC-07.02",
        family_slug="07-rhombi-trapezoids-algebra",
        order=2,
        title="John Molokach's Golden Rhombus from Shifted 1×3 Rectangles",
        short_title="Molokach's Golden Rhombus",
        discoverers=("john-molokach",),
        year="2014",
        citations=("bogomolny-molokach", "bogomolny-golden-ratio"),
        ctk_url="https://www.cut-the-knot.org/do_you_know/GoldenRatioMolokach.shtml",
        ctk_title="Golden Ratio via Golden Rhombus",
        number_field=r"\mathbb{Q}(\phi)",
        number_field_text="Q(φ)",
        enunciation=(
            "Stack two :math:`3 \\times 1` rectangles :g:`RECT1` and :g:`RECT2` shifted by one unit "
            "around center :g:`O`, draw unit circle :g:`cO`, and draw the two tangents to :g:`cO` "
            "perpendicular to outer diagonal :g:`R1R6`. Together with the horizontal outer edges, they "
            "bound a :term:`golden rhombus <golden-rhombus>` :g:`ABCD` (:math:`|AC|/|BD| = \\phi`) "
            "with :math:`|T1K|/|KA| = \\phi`."
        ),
        given_prose=(
            "Center :g:`O` :math:`= (0,0)` and rectangle corner :g:`K` :math:`= (1,1)` of shifted "
            ":math:`3 \\times 1` rectangles :g:`RECT1` and :g:`RECT2`."
        ),
        steps_prose=(
            "Place :math:`3 \\times 1` rectangles :math:`[-2,1]\\times[0,1]` and :math:`[-1,2]\\times[-1,0]` and draw unit circle :g:`cO` tangent to :math:`y = \\pm 1` at :g:`T1` and :g:`T2`.",
            "Draw long diagonal :g:`R1R6` from :math:`(-2,1)` to :math:`(2,-1)` and erect tangents to :g:`cO` where :g:`R1R6` crosses :g:`cO`.",
            "Intersect the four tangents to obtain golden rhombus :g:`ABCD` with top vertices :g:`B` :math:`= (-1/\\phi, 1)` and :g:`A` :math:`= (\\phi, 1)`.",
        ),
        proof_prose=(
            "Diagonal :g:`R1R6` has direction :math:`(2, -1)`, meeting unit circle :g:`cO` at "
            ":math:`\\pm(\\tfrac{2}{\\sqrt{5}}, -\\tfrac{1}{\\sqrt{5}})`. The tangents there are "
            ":math:`2x - y = \\pm\\sqrt{5}`, which intersect :math:`y = 1` at :math:`x_A = \\frac{\\sqrt{5}+1}{2} = \\phi` "
            "and :math:`x_B = -\\frac{\\sqrt{5}-1}{2} = -1/\\phi`. Along :math:`y = 1`, points "
            ":math:`B(-1/\\phi,1), T1(0,1), K(1,1), A(\\phi,1)` form a 4-point golden chain, while "
            ":math:`Q(A,C)/Q(B,D) = (4\\phi^2 + 4)/(4\\phi^{-2} + 4) = \\phi^2`."
        ),
        notes_prose=(
            "A golden rhombus is the planar cross-section of Kepler's rhombic triacontahedron; "
            "Molokach's construction produces both :math:`\\phi`, :math:`1/\\phi`, :math:`1/\\phi^2`, "
            "and the golden rhombus itself in a single stroke."
        ),
        terms=("golden-ratio", "golden-section", "golden-chain", "golden-rhombus", "quadrance"),
        builder=build_molokach_golden_rhombus,
    ),
    ConstructionSpec(
        slug="03-tong-trapezoid-rms",
        catalog_code="GC-07.03",
        family_slug="07-rhombi-trapezoids-algebra",
        order=3,
        title="Jingcheng Tong's Area-Bisecting Chord in a 1:3 Trapezoid",
        short_title="1:3 Trapezoid Area Bisector",
        discoverers=("jingcheng-tong",),
        year="2005",
        citations=("bogomolny-golden-ratio",),
        ctk_url="https://www.cut-the-knot.org/do_you_know/GoldenRatio.shtml",
        ctk_title="Golden Ratio in Geometry — Trapezoid Area Bisector",
        number_field=r"\mathbb{Q}(\phi)",
        number_field_text="Q(φ)",
        enunciation=(
            "Let :g:`ABCD` be a trapezoid with parallel bases :g:`AD` and :g:`BC` satisfying "
            ":math:`|BC| = 3|AD|`. The chord :g:`MN` parallel to the bases that bisects the area of "
            ":g:`ABCD` divides both non-parallel legs :g:`AB` and :g:`DC` in the golden ratio: "
            ":math:`|AM|/|MB| = |DN|/|NC| = \\phi`."
        ),
        given_prose=(
            "Trapezoid :g:`ABCD` with top base :g:`A` :math:`= (-1,2)` to :g:`D` :math:`= (1,2)` "
            "(:math:`a = 2`) and bottom base :g:`B` :math:`= (-3,0)` to :g:`C` :math:`= (3,0)` (:math:`b = 6`)."
        ),
        steps_prose=(
            "Construct trapezoid :g:`ABCD` with parallel bases of lengths :math:`a = 2` and :math:`b = 6`.",
            "Compute the root-mean-square chord length :math:`c = \\sqrt{(a^2 + b^2)/2} = 2\\sqrt{5}`.",
            "Draw parallel chord :g:`MN` at height :math:`y = 3 - \\sqrt{5}` where horizontal width equals :math:`2\\sqrt{5}`.",
        ),
        proof_prose=(
            "Any parallel chord of length :math:`c` divides legs :g:`AB` and :g:`DC` in the ratio "
            ":math:`|AM|/|MB| = (c - a)/(b - c)`, and bisects the trapezoid's area precisely when "
            ":math:`c^2 = (a^2 + b^2)/2`. For :math:`b = 3a`, :math:`c = \\sqrt{5}\\,a`, giving "
            ":math:`|AM|/|MB| = (\\sqrt{5} - 1)/(3 - \\sqrt{5}) = \\phi`—independent of leg slopes or height!"
        ),
        notes_prose=(
            "Because area bisection depends only on the base ratio :math:`b/a = 3`, this theorem holds "
            "for *every* trapezoid (isosceles or scalene) whose parallel bases stand in ratio :math:`1 : 3`."
        ),
        terms=("golden-ratio", "golden-section"),
        builder=build_tong_trapezoid_rms,
    ),
    ConstructionSpec(
        slug="04-tran-isosceles-trapezoid-60",
        catalog_code="GC-07.04",
        family_slug="07-rhombi-trapezoids-algebra",
        order=4,
        title="Tran Quang Hung's 60° Isosceles Trapezoid Diagonal Division",
        short_title="60° Isosceles Trapezoid",
        discoverers=("tran-quang-hung",),
        year="2015",
        citations=("bogomolny-tqh-trapezoid", "bogomolny-golden-ratio"),
        ctk_url="https://www.cut-the-knot.org/do_you_know/TQHGoldenRatio.shtml",
        ctk_title="Golden Ratio in Isosceles Trapezoid",
        number_field=r"\mathbb{Q}(\sqrt{3}, \phi)",
        number_field_text="Q(√3, φ)",
        enunciation=(
            "In half-hexagon isosceles trapezoid :g:`ABCD` (:math:`|DA| = |AB| = |BC|` and "
            ":math:`\\angle C = \\angle D = 60^\\circ`), reflect :g:`B` across :g:`C` to :g:`K`. "
            "Circle :g:`cKB` centered at :g:`K` through :g:`B` cuts diagonal :g:`AC` internally at "
            ":g:`M` such that :math:`|CM|/|MA| = |CA|/|CM| = \\phi`."
        ),
        given_prose=(
            "Half-hexagon trapezoid :g:`ABCD` with base :g:`D` :math:`= (-2,0)` to :g:`C` :math:`= (2,0)` "
            "and top :g:`A` :math:`= (-1,\\sqrt{3})` to :g:`B` :math:`= (1,\\sqrt{3})`."
        ),
        steps_prose=(
            "Extend leg :g:`BC` past :g:`C` by :math:`|CK| = |BC| = 2` to :g:`K` :math:`= (3, -\\sqrt{3})`.",
            "Draw diagonal :g:`AC` (of length :math:`2\\sqrt{3}`, perpendicular to :g:`DA`).",
            "Draw circle :g:`cKB` of radius :math:`4` centered at :g:`K`, cutting :g:`AC` at :g:`M`.",
        ),
        proof_prose=(
            "Vectors :math:`\\vec{CA} = (-3, \\sqrt{3})` (:math:`|CA| = 2\\sqrt{3}`) and "
            ":math:`\\vec{CK} = (1, -\\sqrt{3})` (:math:`|CK| = 2`) satisfy "
            ":math:`\\vec{CA}\\cdot\\vec{CK} = -6`, so :math:`\\angle ACK = 120^\\circ`. "
            "Parameterizing :g:`M` on :g:`CA` by :math:`x = |CM|/|CA|`, the Law of Cosines on "
            ":math:`\\triangle KCM` with :math:`|KM| = 4` gives :math:`12x^2 + 12x + 4 = 16`, "
            "i.e. :math:`x^2 + x - 1 = 0`, whence :math:`x = 1/\\phi` and :math:`|CM|/|MA| = \\phi`."
        ),
        notes_prose=(
            "Parallel lines through :g:`M` transfer this golden section simultaneously onto top base "
            ":g:`AB` and leg :g:`BC`, inscribing a golden parallelogram inside the half-hexagon."
        ),
        terms=("golden-ratio", "golden-section", "quadrance"),
        builder=build_tran_isosceles_trapezoid_60,
    ),
    ConstructionSpec(
        slug="05-tran-mixtilinear-equilateral",
        catalog_code="GC-07.05",
        family_slug="07-rhombi-trapezoids-algebra",
        order=5,
        title="Tran Quang Hung's Mixtilinear Circle in an Equilateral Triangle",
        short_title="Equilateral Mixtilinear Circle",
        discoverers=("tran-quang-hung", "alexander-bogomolny", "leo-giugiuc"),
        year="2016",
        citations=("bogomolny-mixtilinear", "bogomolny-golden-ratio"),
        ctk_url="https://www.cut-the-knot.org/do_you_know/GoldenMixtilinear.shtml",
        ctk_title="Golden Ratio in Mixtilinear Circles",
        number_field=r"\mathbb{Q}(\sqrt{3}, \phi)",
        number_field_text="Q(√3, φ)",
        enunciation=(
            "In equilateral triangle :g:`ABC` with circumcenter :g:`K` and circumcircle :g:`cK`, "
            "inscribe the :g:`A`-mixtilinear circle :g:`cF` tangent to sides :g:`AB`, :g:`AC` and "
            "internally to :g:`cK`. The line through :g:`K` parallel to :g:`AB` meets :g:`BC` at :g:`O` "
            "and :g:`cF` at :g:`I` and :g:`J` such that :math:`|KO|/|OJ| = \\phi`."
        ),
        given_prose=(
            "Equilateral triangle :g:`ABC` of side :math:`18` with :g:`A` :math:`= (-9,0)`, "
            ":g:`B` :math:`= (9,0)`, :g:`C` :math:`= (0, 9\\sqrt{3})`, and circumcenter :g:`K` :math:`= (0, 3\\sqrt{3})`."
        ),
        steps_prose=(
            "Draw circumcircle :g:`cK` of radius :math:`6\\sqrt{3}` around :g:`ABC`.",
            "Inscribe :g:`A`-mixtilinear circle :g:`cF` centered at :g:`F` :math:`= (3, 4\\sqrt{3})` of radius :math:`4\\sqrt{3}`, tangent to :g:`AB` at :g:`D` :math:`= (3,0)`.",
            "Draw horizontal line :g:`KO` (:math:`y = 3\\sqrt{3}`), cutting :g:`BC` at :g:`O` :math:`= (6, 3\\sqrt{3})` and :g:`cF` at :g:`I` and :g:`J`.",
        ),
        proof_prose=(
            "For side :math:`s = 18`, the :g:`A`-mixtilinear inradius is :math:`r_A = \\frac{2\\sqrt{3}}{9}s = 4\\sqrt{3}` "
            "with :math:`|AD| = \\frac{2}{3}s = 12`, placing :g:`F` at :math:`(3, 4\\sqrt{3})`. Along "
            ":math:`y = 3\\sqrt{3}`, :math:`(x - 3)^2 + (3\\sqrt{3} - 4\\sqrt{3})^2 = 48` yields "
            ":math:`(x - 3)^2 = 45`, so :math:`x_J = 3 + 3\\sqrt{5}`. Since :math:`x_K = 0` and :math:`x_O = 6`, "
            ":math:`|KO| = 6` and :math:`|OJ| = 3(\\sqrt{5} - 1) = 6/\\phi`, proving :math:`|KO|/|OJ| = \\phi`."
        ),
        notes_prose=(
            "Alexander Bogomolny cataloged seven distinct golden ratios generated by a single "
            "mixtilinear circle inside an equilateral triangle."
        ),
        terms=("golden-ratio", "golden-section", "mixtilinear-incircle"),
        builder=build_tran_mixtilinear_equilateral,
    ),
    ConstructionSpec(
        slug="06-curry-hooper-dissection",
        catalog_code="GC-07.06",
        family_slug="07-rhombi-trapezoids-algebra",
        order=6,
        title="Exact φ-Limit Resolution of the Hooper–Curry Fibonacci Dissection",
        short_title="Hooper–Curry φ-Dissection",
        discoverers=("william-hooper", "paul-curry", "alexander-bogomolny"),
        year="1794",
        citations=("hooper-1794", "bogomolny-golden-ratio"),
        ctk_url="https://www.cut-the-knot.org/do_you_know/GoldenRatio.shtml",
        ctk_title="Golden Ratio and the Missing-Square Dissection",
        number_field=r"\mathbb{Q}(\phi)",
        number_field_text="Q(φ)",
        enunciation=(
            "Replace integer Fibonacci lengths :math:`(3, 5, 8, 13)` in the :math:`8 \\times 8 = 64` vs. "
            ":math:`5 \\times 13 = 65` dissection fallacy by exact powers :math:`(1, \\phi, \\phi^2, \\phi^3)`. "
            "In rectangle :g:`ABCD` of width :math:`\\phi^3` and height :math:`\\phi`, internal vertices "
            ":g:`Q` :math:`= (\\phi, 1/\\phi)` and :g:`P` :math:`= (\\phi^2, 1)` lie *identically* on "
            "diagonal :g:`AC`, forming the 4-point golden chain :math:`|AQ|/|QP| = |AP|/|AQ| = \\phi`."
        ),
        given_prose=(
            "Rectangle :g:`ABCD` with :g:`A` :math:`= (0,0)`, :g:`B` :math:`= (\\phi^3, 0)`, "
            ":g:`C` :math:`= (\\phi^3, \\phi)`, and :g:`D` :math:`= (0, \\phi)`."
        ),
        steps_prose=(
            "Mark golden cuts :g:`E` :math:`= (\\phi^2, 0)` on :g:`AB` and :g:`F` :math:`= (\\phi, \\phi)` on :g:`DC`.",
            "Erect vertical cuts :g:`EP` of height :math:`1` to :g:`P` :math:`= (\\phi^2, 1)` and :g:`FQ` of length :math:`1` to :g:`Q` :math:`= (\\phi, 1/\\phi)`.",
            "Draw diagonal :g:`AC`, which passes with zero area gap through both :g:`Q` and :g:`P`.",
        ),
        proof_prose=(
            "For Fibonacci numbers, Cassini's identity :math:`F_{n-1}F_{n+1} - F_n^2 = (-1)^n` produces "
            "a thin parallelogram of area :math:`\\pm 1` because slopes :math:`F_{n-2}/F_n` and "
            ":math:`F_{n-1}/F_{n+1}` differ slightly. Replacing :math:`F_k` by :math:`\\phi^k` gives "
            ":math:`\\phi \\cdot \\phi^3 - (\\phi^2)^2 = 0` and identical slopes "
            ":math:`\\text{slope}(A,Q) = (1/\\phi)/\\phi = 1/\\phi^2 = \\text{slope}(A,P) = \\text{slope}(A,C)`. "
            "Along :g:`AC`, abscissas :math:`(0, \\phi, \\phi^2, \\phi^3)` yield :math:`|AQ|/|QP| = \\phi / 1 = \\phi`."
        ),
        notes_prose=(
            "First published by William Hooper in *Rational Recreations* (1794) and generalized by "
            "magician Paul Curry (1953), the missing-square paradox vanishes solely at the irrational "
            "fixed point :math:`\\phi`."
        ),
        terms=("golden-ratio", "golden-section", "golden-chain", "golden-rectangle"),
        builder=build_curry_hooper_dissection,
    ),
)
