"""Family 02: Equilateral Triangles & Regular Hexagons — The Odom Lineage.

Catalogs George Odom's celebrated 1983 equilateral midline construction and six
modern descendants by Michel Bataille, Bùi Quang Tuân, Tran Quang Hung, and
Nguyen Thanh Dung.
"""

from __future__ import annotations

import sympy as sp

from .helpers import make_result, new_catalog_model
from .schema import ConstructionResult, ConstructionSpec


def build_odom_equilateral() -> ConstructionResult:
    """George Odom's 1983 equilateral triangle midline & circumcircle secant."""
    m = new_catalog_model("odom-equilateral")
    s3 = sp.sqrt(3)
    A = m.set_point(0, 2, classes=["given"], ID="A")
    B = m.set_point(-s3, -1, classes=["given"], ID="B")
    C = m.set_point(s3, -1, classes=["given"], ID="C")
    O = m.set_point(0, 0, ID="O")

    m.construct_polygon([A, B, C], ID="ABC")
    c_o = m.construct_circle(O, A, classes=["primary"], ID="cO")

    L = m.set_point(-s3 / 2, sp.Rational(1, 2), ID="L")
    M = m.set_point(s3 / 2, sp.Rational(1, 2), ID="M")
    ln_lm = m.construct_line(L, M, classes=["golden"], ID="LM")

    X = m.intersect(ln_lm, c_o, beyond=(M, L), classes=["golden"], ID="X")
    m.intersect(ln_lm, c_o, beyond=(L, M), classes=["golden"], ID="Y")
    _ = X

    return make_result(m, ("L", "M"), ("M", "Y"), ("L", "M", "Y"))


def build_bataille_triangle_square() -> ConstructionResult:
    """Michel Bataille's 2011 equilateral triangle and external square sweep."""
    m = new_catalog_model("bataille-triangle-square")
    s3 = sp.sqrt(3)
    B = m.set_point(0, 0, classes=["given"], ID="B")
    C = m.set_point(2, 0, classes=["given"], ID="C")
    A = m.set_point(1, s3, ID="A")
    D = m.set_point(2, -2, ID="D")
    E = m.set_point(0, -2, ID="E")

    m.construct_polygon([A, B, C], ID="ABC")
    m.construct_polygon([B, C, D, E], ID="BCDE")
    ln_ab = m.construct_line(A, B, ID="AB")
    m.construct_segment(C, E, classes=["auxiliary"], ID="CE")

    c_ce = m.construct_circle(C, E, classes=["golden"], ID="cCE")
    m.intersect(c_ce, ln_ab, beyond=(A, B), classes=["golden"], ID="F")

    return make_result(m, ("A", "B"), ("B", "F"), ("A", "B", "F"))


def build_bui_two_equilaterals() -> ConstructionResult:
    """Bùi Quang Tuân's coupled equilateral triangles on side and altitude."""
    m = new_catalog_model("bui-two-equilaterals")
    s3 = sp.sqrt(3)
    B = m.set_point(-1, 0, classes=["given"], ID="B")
    C = m.set_point(1, 0, classes=["given"], ID="C")
    M = m.set_point(0, 0, ID="M")
    A = m.set_point(0, s3, ID="A")
    N = m.set_point(sp.Rational(3, 2), s3 / 2, ID="N")

    m.construct_polygon([A, B, C], ID="ABC")
    m.construct_polygon([A, M, N], ID="AMN")
    ln_mn = m.construct_line(M, N, classes=["golden"], ID="MN")

    c_ba = m.construct_circle(B, A, classes=["golden"], ID="cBA")
    m.intersect(c_ba, ln_mn, between=(M, N), classes=["golden"], ID="P")

    return make_result(m, ("M", "P"), ("P", "N"), ("M", "P", "N"))


def build_tran_reflected_equilaterals() -> ConstructionResult:
    """Tran Quang Hung's reflected equilateral triangles & midline secant."""
    m = new_catalog_model("tran-reflected-equilaterals")
    s3 = sp.sqrt(3)
    A = m.set_point(-1, 0, classes=["given"], ID="A")
    B = m.set_point(1, 0, classes=["given"], ID="B")
    C = m.set_point(0, s3, ID="C")
    C1 = m.set_point(0, -s3, ID="C1")
    O1 = m.set_point(0, -s3 / 3, ID="O1")

    m.construct_polygon([A, B, C], ID="ABC")
    m.construct_polygon([A, B, C1], ID="ABC1")
    c_abc1 = m.construct_circle(O1, A, classes=["primary"], ID="cO1")

    N = m.set_point(0, 0, ID="N")
    M = m.set_point(sp.Rational(1, 2), s3 / 2, ID="M")
    ln_mn = m.construct_line(M, N, classes=["auxiliary"], ID="MN")
    P = m.intersect(ln_mn, c_abc1, side_of=(A, B, 1), ID="P")

    ln_ap = m.construct_line(A, P, classes=["golden"], ID="AP")
    ln_bc = m.construct_line(B, C, ID="BC")
    m.intersect(ln_ap, ln_bc, classes=["golden"], ID="D")

    return make_result(m, ("C", "D"), ("D", "B"), ("C", "D", "B"))


def build_tran_incircle_equilateral() -> ConstructionResult:
    """Tran Quang Hung's nested equilateral triangles inscribed in the incircle."""
    m = new_catalog_model("tran-incircle-equilateral")
    s3 = sp.sqrt(3)
    phi = sp.Rational(1, 2) + sp.sqrt(5) / 2

    # Outer equilateral triangle ABC of circumradius 2 (incircle radius 1 at O = (0,0))
    O = m.set_point(0, 0, ID="O")
    A = m.set_point(0, 2, classes=["given"], ID="A")
    B = m.set_point(-s3, -1, classes=["given"], ID="B")
    C = m.set_point(s3, -1, classes=["given"], ID="C")
    m.construct_polygon([A, B, C], ID="ABC")

    P_top = m.set_point(0, 1, guide=True, ID="Ptop")
    c_in = m.construct_circle(O, P_top, classes=["primary"], ID="cIn")

    # Inner equilateral triangle FGH on unit circle x^2 + y^2 = 1 such that
    # F lies on AH, G lies on CF, H lies on BG.
    # For F = (cos t, sin t) with 3-fold rotational symmetry:
    # Collinearity of A=(0,2), F=(x,y), H=(-x/2 - sqrt(3)y/2, sqrt(3)x/2 - y/2)
    # gives 3y + sqrt(3)x = 3*(x^2 + y^2)... exact solution:
    # y_F = (3 + sqrt(15))/8? Let's construct via exact algebraic coordinates!
    # Wait: if |AF| = a and |FH| = s = sqrt(3) (side of inscribed equilateral in unit circle!):
    # Power of A=(0,2) wrt unit circle x^2+y^2=1 is OA^2 - 1 = 4 - 1 = 3!
    # Secant AFH satisfies |AF| * |AH| = |AF| * (|AF| + |FH|) = 3!
    # Since |FH| = sqrt(3), |AF|*(|AF| + sqrt(3)) = 3 => (|AF|/sqrt(3))*((|AF|/sqrt(3)) + 1) = 1
    # => |AF| = sqrt(3)/phi !! And |FH| / |AF| = sqrt(3) / (sqrt(3)/phi) = phi !!
    # Let's compute exact coordinates of F on x^2+y^2=1 with |AF|^2 = 3/phi^2 = 3*(2 - phi):
    # x_F^2 + (y_F - 2)^2 = 3*(2 - phi) => 1 + 4 - 4*y_F = 6 - 3*phi => y_F = (3*phi - 1)/4 = (1 + 3*sqrt(5))/8!
    # And x_F^2 = 1 - y_F^2 = 1 - (46 + 6*sqrt(5))/64 = (18 - 6*sqrt(5))/64 = 3*(3 - sqrt(5))/32 = 3/(16*phi^2)!
    #Wait: 1^2 + (3*sqrt(5))^2 = 1 + 45 = 46! 64 - 46 = 18! 18 - 6*sqrt(5) = 3*(6 - 2*sqrt(5)) = 3*(sqrt(5)-1)^2!
    # SO x_F = sqrt(3)*(sqrt(5) - 1)/8 = sqrt(3)/(4*phi) (rational in sqrt(3) and phi, ZERO nested radicals!!)!
    xf = s3 / (4 * phi)
    yf = (3 * phi - 1) / 4

    F = m.set_point(-xf, yf, classes=["golden"], ID="F")
    H = m.set_point(xf / 2 - s3 * yf / 2, -s3 * xf / 2 - yf / 2, classes=["golden"], ID="H")
    G = m.set_point(xf / 2 + s3 * yf / 2, s3 * xf / 2 - yf / 2, classes=["golden"], ID="G")

    m.construct_polygon([F, G, H], classes=["golden"], ID="FGH")
    m.construct_line(A, H, classes=["golden"], ID="AH")
    m.construct_line(B, G, classes=["auxiliary"], ID="BG")
    m.construct_line(C, F, classes=["auxiliary"], ID="CF")
    _ = c_in

    return make_result(m, ("F", "H"), ("A", "F"), ("A", "F", "H"))


def build_tran_hexagon_square() -> ConstructionResult:
    """Tran Quang Hung's regular hexagon & external square compass sweep."""
    m = new_catalog_model("tran-hexagon-square")
    s3 = sp.sqrt(3)
    A = m.set_point(0, 0, classes=["given"], ID="A")
    B = m.set_point(2, 0, classes=["given"], ID="B")
    C = m.set_point(3, s3, ID="C")
    D = m.set_point(2, 2 * s3, ID="D")
    E = m.set_point(0, 2 * s3, ID="E")
    F = m.set_point(-1, s3, ID="F")

    G = m.set_point(0, -2, ID="G")
    H = m.set_point(2, -2, ID="H")

    m.construct_polygon([A, B, C, D, E, F], ID="ABCDEF")
    m.construct_polygon([A, B, H, G], ID="ABHG")
    m.construct_segment(A, H, classes=["auxiliary"], ID="AH")

    ln_ef = m.construct_line(E, F, ID="EF")
    ln_bc = m.construct_line(B, C, ID="BC")
    c_ah = m.construct_circle(A, H, classes=["golden"], ID="cAH")

    m.intersect(c_ah, ln_ef, between=(E, F), classes=["golden"], ID="I")
    L = m.intersect(c_ah, ln_bc, between=(B, C), classes=["golden"], ID="L")
    _ = L

    return make_result(m, ("F", "I"), ("I", "E"), ("F", "I", "E"))


def build_nguyen_butterfly_equilateral() -> ConstructionResult:
    """Nguyen Thanh Dung's butterfly chords astride an equilateral triangle."""
    m = new_catalog_model("nguyen-butterfly-equilateral")
    s3 = sp.sqrt(3)

    O = m.set_point(0, 0, classes=["given"], ID="O")
    J = m.set_point(0, 2, classes=["given"], ID="J")
    I = m.set_point(0, 1, ID="I")

    c_o = m.construct_circle(O, J, classes=["primary"], ID="cO")
    m.construct_segment(O, J, classes=["auxiliary"], ID="OJ")

    # Chord XT perpendicular to OJ through I=(0,1): x^2 + 1 = 4 => x = +-sqrt(3)
    X = m.set_point(-s3, 1, ID="X")
    T = m.set_point(s3, 1, ID="T")
    ln_xt = m.construct_line(X, T, classes=["golden"], ID="XT")

    # Equilateral triangle ICD with apex I=(0,1) and C, D on circle x^2 + y^2 = 4 below I:
    # Let side of equilateral ICD be s, symmetric about y-axis: C = (-s/2, 1 - s*sqrt(3)/2), D = (s/2, 1 - s*sqrt(3)/2)
    # On x^2 + y^2 = 4: s^2/4 + 1 - s*sqrt(3) + 3*s^2/4 = 4 => s^2 - s*sqrt(3) - 3 = 0
    # => s = (sqrt(3) + sqrt(15))/2 = sqrt(3)*phi !!
    phi = sp.Rational(1, 2) + sp.sqrt(5) / 2
    s_eq = s3 * phi
    C = m.set_point(-s_eq / 2, 1 - s_eq * s3 / 2, ID="C")
    D = m.set_point(s_eq / 2, 1 - s_eq * s3 / 2, ID="D")
    m.construct_polygon([I, C, D], ID="ICD")

    ln_ic = m.construct_line(I, C, classes=["auxiliary"], ID="IC")
    ln_id = m.construct_line(I, D, classes=["auxiliary"], ID="ID")
    A = m.intersect(ln_ic, c_o, other_than=C, ID="A")
    B = m.intersect(ln_id, c_o, other_than=D, ID="B")

    ln_ad = m.construct_line(A, D, classes=["auxiliary"], ID="AD")
    ln_bc = m.construct_line(B, C, classes=["auxiliary"], ID="BC")
    m.intersect(ln_bc, ln_xt, classes=["golden"], ID="Y")
    m.intersect(ln_ad, ln_xt, classes=["golden"], ID="Z")

    return make_result(m, ("Y", "Z"), ("Z", "T"), ("Y", "Z", "T"))


EQUILATERAL_HEXAGON_SPECS: tuple[ConstructionSpec, ...] = (
    ConstructionSpec(
        slug="01-odom-equilateral",
        catalog_code="GC-02.01",
        family_slug="02-equilateral-hexagon",
        order=1,
        title="George Odom's Equilateral Midline & Circumcircle Chord (1983)",
        short_title="Odom's Equilateral Midline",
        discoverers=("george-odom", "h-s-m-coxeter"),
        year="1983",
        citations=("odom-coxeter-1983", "bogomolny-golden-ratio"),
        ctk_url="https://www.cut-the-knot.org/do_you_know/GoldenRatio.shtml#Odom",
        ctk_title="Golden Ratio in Geometry — George Odom's Construction",
        number_field=r"\mathbb{Q}(\sqrt{3}, \phi)",
        number_field_text="Q(√3, φ)",
        enunciation=(
            "Let :g:`ABC` be an equilateral triangle inscribed in circle :g:`cO`, and let "
            ":g:`L` and :g:`M` be the midpoints of sides :g:`AB` and :g:`AC`. Extending midline "
            ":g:`LM` to meet circumcircle :g:`cO` at :g:`X` and :g:`Y` divides the chord in the "
            "golden ratio: :math:`|LM|/|MY| = |LY|/|LM| = \\phi`."
        ),
        given_prose=(
            "Equilateral triangle :g:`ABC` with vertices :g:`A` :math:`= (0, 2)`, "
            ":g:`B` :math:`= (-\\sqrt{3}, -1)`, :g:`C` :math:`= (\\sqrt{3}, -1)` on circumcircle :g:`cO` of radius :math:`2`."
        ),
        steps_prose=(
            "Inscribe equilateral triangle :g:`ABC` of side :math:`2\\sqrt{3}` in circle :g:`cO`.",
            "Mark midpoints :g:`L` :math:`= (-\\tfrac{\\sqrt{3}}{2}, \\tfrac{1}{2})` of :g:`AB` and :g:`M` :math:`= (\\tfrac{\\sqrt{3}}{2}, \\tfrac{1}{2})` of :g:`AC`.",
            "Draw line :g:`LM` parallel to :g:`BC`, intersecting circumcircle :g:`cO` at :g:`X` :math:`= (-\\tfrac{\\sqrt{15}}{2}, \\tfrac{1}{2})` and :g:`Y` :math:`= (\\tfrac{\\sqrt{15}}{2}, \\tfrac{1}{2})`.",
        ),
        proof_prose=(
            "Let :math:`a = |LM| = |AM| = |MC| = \\sqrt{3}` and :math:`b = |XL| = |MY|`. "
            "By Euclid's Intersecting Chords Theorem (III.35) applied to chords :g:`XY` and :g:`AC` "
            "at :g:`M`, :math:`|XM| \\cdot |MY| = |AM| \\cdot |MC|`, hence :math:`(a + b)b = a^2`. "
            "Dividing by :math:`b^2` yields :math:`(a/b)^2 - (a/b) - 1 = 0`, proving "
            ":math:`|LM|/|MY| = a/b = \\phi` and forming a symmetric 4-point golden chain :math:`(X, L, M, Y)`."
        ),
        notes_prose=(
            "Discovered in the early 1980s by artist and amateur geometer :person:`George Odom <george-odom>` "
            "at the Hudson River Psychiatric Center and communicated to :person:`H. S. M. Coxeter <h-s-m-coxeter>`, "
            "who posed it as Problem E3007 in the *American Mathematical Monthly* (:cite:`Odom & Coxeter 1983 <odom-coxeter-1983>`), "
            "Odom's construction sparked an entire modern genre of equilateral-triangle golden sections."
        ),
        terms=("intersecting-chords-theorem", "golden-section", "golden-chain"),
        builder=build_odom_equilateral,
    ),
    ConstructionSpec(
        slug="02-bataille-triangle-square",
        catalog_code="GC-02.02",
        family_slug="02-equilateral-hexagon",
        order=2,
        title="Michel Bataille's Equilateral Triangle & External Square",
        short_title="Bataille Triangle & Square",
        discoverers=("michel-bataille",),
        year="2011",
        citations=("bataille-2011", "ctk-bataille"),
        ctk_url="https://www.cut-the-knot.org/do_you_know/MBatailleGoldenRatio.shtml",
        ctk_title="From Equilateral Triangle and Square to Golden Ratio",
        number_field=r"\mathbb{Q}(\sqrt{3}, \phi)",
        number_field_text="Q(√3, φ)",
        enunciation=(
            "Erect equilateral triangle :g:`ABC` and external square :g:`BCDE` on opposite sides "
            "of shared base :g:`BC`. Circle :g:`cCE` centered at :g:`C` through opposite square "
            "vertex :g:`E` cuts ray :g:`AB` beyond :g:`B` at :g:`F` so that :math:`|AF|/|AB| = |AB|/|BF| = \\phi`."
        ),
        given_prose=(
            "Shared base :g:`BC` from :g:`B` :math:`= (0, 0)` to :g:`C` :math:`= (2, 0)` of length :math:`2`."
        ),
        steps_prose=(
            "Construct equilateral triangle :g:`ABC` above :g:`BC` with apex :g:`A` :math:`= (1, \\sqrt{3})`.",
            "Construct square :g:`BCDE` below :g:`BC` with :g:`D` :math:`= (2, -2)` and :g:`E` :math:`= (0, -2)`.",
            "Draw circle :g:`cCE` centered at :g:`C` through :g:`E` (radius :math:`2\\sqrt{2}`), intersecting line :g:`AB` beyond :g:`B` at :g:`F`.",
        ),
        proof_prose=(
            "Diagonal :g:`CE` of square :g:`BCDE` has quadrance :math:`Q(C, E) = 2^2 + 2^2 = 8`. "
            "Along ray :g:`AB` extended beyond :g:`B` by distance :math:`s = |BF|`, :math:`\\angle CBF = 120^\\circ`, "
            "so the Law of Cosines in :math:`\\triangle CBF` gives :math:`s^2 + 2s + 4 = 8`, or :math:`s^2 + 2s - 4 = 0`. "
            "Thus :math:`|BF| = \\sqrt{5} - 1 = 2/\\phi` and :math:`|AF| = 2 + (\\sqrt{5} - 1) = \\sqrt{5} + 1 = 2\\phi`, "
            "proving :math:`|AF|/|AB| = |AB|/|BF| = \\phi`."
        ),
        notes_prose=(
            "Published by :person:`Michel Bataille <michel-bataille>` (:cite:`Bataille 2011 <bataille-2011>`, "
            ":cite:`Cut-the-Knot <ctk-bataille>`), this construction bridges the regular :math:`3`-gon and :math:`4`-gon directly to :math:`\\phi`."
        ),
        terms=("golden-section", "quadrance"),
        builder=build_bataille_triangle_square,
    ),
    ConstructionSpec(
        slug="03-bui-two-equilaterals",
        catalog_code="GC-02.03",
        family_slug="02-equilateral-hexagon",
        order=3,
        title="Bùi Quang Tuân's Side-and-Altitude Equilateral Triangles",
        short_title="Coupled Equilateral Triangles",
        discoverers=("bui-quang-tuan",),
        year="2011",
        citations=("ctk-bui-qtb", "ctk-bui-qtb2"),
        ctk_url="https://www.cut-the-knot.org/do_you_know/GoldenQTB.shtml",
        ctk_title="Golden Section in Two Equilateral Triangles",
        number_field=r"\mathbb{Q}(\sqrt{3}, \phi)",
        number_field_text="Q(√3, φ)",
        enunciation=(
            "Let :g:`M` be the midpoint of base :g:`BC` of equilateral triangle :g:`ABC`, and "
            "erect a second equilateral triangle :g:`AMN` on altitude :g:`AM`. Then circle "
            ":g:`cBA` centered at :g:`B` through :g:`A` cuts side :g:`MN` at :g:`P` in the golden "
            "ratio :math:`|MN|/|MP| = |MP|/|PN| = \\phi`."
        ),
        given_prose=(
            "Equilateral triangle :g:`ABC` with :g:`B` :math:`= (-1, 0)`, :g:`C` :math:`= (1, 0)`, "
            "midpoint :g:`M` :math:`= (0, 0)`, and apex :g:`A` :math:`= (0, \\sqrt{3})`."
        ),
        steps_prose=(
            "Construct equilateral triangle :g:`ABC` of side :math:`2` and bisect :g:`BC` at :g:`M`.",
            "On altitude :g:`AM` of length :math:`\\sqrt{3}`, construct equilateral triangle :g:`AMN` with :g:`N` :math:`= (\\tfrac{3}{2}, \\tfrac{\\sqrt{3}}{2})`.",
            "Draw circle :g:`cBA` centered at :g:`B` through :g:`A` (radius :math:`2`), cutting :g:`MN` at :g:`P`.",
        ),
        proof_prose=(
            "Ray :g:`MN` makes angle :math:`30^\\circ` with :math:`MC`, so :math:`\\angle BMP = 150^\\circ`. "
            "Setting :math:`t = |MP|` in :math:`\\triangle BMP` with :math:`|BM| = 1` and :math:`|BP| = |BA| = 2` "
            "yields :math:`t^2 - 2t\\cos 150^\\circ + 1 = 4 \\implies t^2 + \\sqrt{3}\\,t - 3 = 0`, whose positive "
            "root is :math:`t = \\frac{\\sqrt{15} - \\sqrt{3}}{2} = \\frac{\\sqrt{3}}{\\phi}`. Since :math:`|MN| = \\sqrt{3}`, "
            "we obtain :math:`|PN| = \\sqrt{3} - \\sqrt{3}/\\phi = \\sqrt{3}/\\phi^2` and :math:`|MP|/|PN| = \\phi`."
        ),
        notes_prose=(
            "Contributed by :person:`Bùi Quang Tuân <bui-quang-tuan>` (:cite:`Cut-the-Knot <ctk-bui-qtb>`), "
            "along with a companion variant (:cite:`Cut-the-Knot II <ctk-bui-qtb2>`), this figure exploits "
            "the :math:`150^\\circ` cosine identity :math:`x^2 + \\sqrt{3}\\,x - 3 = 0`."
        ),
        terms=("golden-section", "quadrance"),
        builder=build_bui_two_equilaterals,
    ),
    ConstructionSpec(
        slug="04-tran-reflected-equilaterals",
        catalog_code="GC-02.04",
        family_slug="02-equilateral-hexagon",
        order=4,
        title="Tran Quang Hung's Reflected Equilateral Triangles",
        short_title="Reflected Equilaterals",
        discoverers=("tran-quang-hung",),
        year="2014",
        citations=("ctk-buratino5", "bogomolny-golden-ratio"),
        ctk_url="https://www.cut-the-knot.org/do_you_know/Buratino5.shtml",
        ctk_title="Golden Ratio in Two Equilateral Triangles",
        number_field=r"\mathbb{Q}(\sqrt{3}, \phi)",
        number_field_text="Q(√3, φ)",
        enunciation=(
            "Reflect equilateral triangle :g:`ABC` across base :g:`AB` to :g:`ABC_1 <ABC1>` with "
            "circumcircle :g:`cO1`. If midpoints :g:`M` of :g:`BC` and :g:`N` of :g:`AB` are joined "
            "to meet :g:`cO1` at :g:`P`, then line :g:`AP` divides side :g:`BC` at :g:`D` in the "
            "golden ratio :math:`|CD|/|DB| = \\phi`."
        ),
        given_prose=(
            "Shared base :g:`AB` from :g:`A` :math:`= (-1, 0)` to :g:`B` :math:`= (1, 0)` with reflected "
            "equilateral apices :g:`C` :math:`= (0, \\sqrt{3})` and :g:`C_1 <C1>` :math:`= (0, -\\sqrt{3})`."
        ),
        steps_prose=(
            "Construct equilateral triangles :g:`ABC` and :g:`ABC_1 <ABC1>`, and circumcircle :g:`cO1` of :g:`ABC_1 <ABC1>` centered at :g:`O_1 <O1>` :math:`= (0, -\\tfrac{\\sqrt{3}}{3})`.",
            "Join midpoint :g:`M` :math:`= (\\tfrac{1}{2}, \\tfrac{\\sqrt{3}}{2})` of :g:`BC` and midpoint :g:`N` :math:`= (0, 0)` of :g:`AB`, extending ray :g:`MN` to meet :g:`cO1` at :g:`P`.",
            "Draw line :g:`AP` to intersect side :g:`BC` at :g:`D`.",
        ),
        proof_prose=(
            "Line :g:`MN` passes through the origin with slope :math:`\\sqrt{3}` (:math:`y = \\sqrt{3}\\,x`). "
            "Intersecting with :g:`cO1` :math:`(x^2 + (y + \\tfrac{\\sqrt{3}}{3})^2 = \\tfrac{4}{3})` gives "
            ":math:`4x^2 + 2x - 1 = 0`, whose positive root is :math:`x_P = \\frac{\\sqrt{5} - 1}{4} = \\frac{1}{2\\phi}` "
            "and :math:`y_P = \\frac{\\sqrt{3}}{2\\phi}`, so :math:`|NP| = 1/\\phi` along :g:`NM` (of length :math:`1`). "
            "Because :g:`MN` is the midline parallel to :g:`AC` and :g:`N` bisects :g:`AB`, projecting :g:`P` "
            "from :g:`A` onto :g:`BC` yields :math:`|CD|/|DB| = \\phi`."
        ),
        notes_prose=(
            "Contributed by :person:`Tran Quang Hung <tran-quang-hung>` (:cite:`Cut-the-Knot <ctk-buratino5>`), "
            "this construction produces golden divisions simultaneously along midline :g:`MN` (:math:`|NP|/|MN| = \\phi`) "
            "and along side :g:`BC` (:math:`|CD|/|DB| = \\phi`)."
        ),
        terms=("golden-section", "quadrance"),
        builder=build_tran_reflected_equilaterals,
    ),
    ConstructionSpec(
        slug="05-tran-incircle-equilateral",
        catalog_code="GC-02.05",
        family_slug="02-equilateral-hexagon",
        order=5,
        title="Nested Equilateral Triangles on the Incircle",
        short_title="Incircle Nested Equilaterals",
        discoverers=("tran-quang-hung",),
        year="2014",
        citations=("ctk-buratino2", "bogomolny-golden-ratio"),
        ctk_url="https://www.cut-the-knot.org/do_you_know/Buratino2.shtml",
        ctk_title="Golden Ratio in Equilateral Triangles",
        number_field=r"\mathbb{Q}(\sqrt{3}, \phi)",
        number_field_text="Q(√3, φ)",
        enunciation=(
            "Inscribe equilateral triangle :g:`FGH` in the incircle :g:`cIn` of equilateral "
            "triangle :g:`ABC` so that extended sides :g:`HF`, :g:`FG`, :g:`GH` pass through "
            "vertices :g:`A`, :g:`C`, :g:`B` respectively. Then :math:`|FH|/|AF| = |FG|/|CF_1|` "
            "divides each secant in the golden ratio :math:`|FH|/|AF| = \\phi`."
        ),
        given_prose=(
            "Equilateral triangle :g:`ABC` of circumradius :math:`2` centered at :g:`O` :math:`= (0, 0)` "
            "with unit incircle :g:`cIn`."
        ),
        steps_prose=(
            "Construct equilateral triangle :g:`ABC` and its unit incircle :g:`cIn` centered at :g:`O`.",
            "Inscribe equilateral triangle :g:`FGH` of side :math:`\\sqrt{3}` in :g:`cIn` such that :g:`F` lies on segment :g:`AH`, :g:`G` on :g:`CF`, and :g:`H` on :g:`BG`.",
            "Draw the three three-fold symmetric secants :g:`AH`, :g:`BG`, and :g:`CF`.",
        ),
        proof_prose=(
            "For vertex :g:`A` :math:`= (0, 2)` and unit circle :g:`cIn`, the power of :g:`A` with "
            "respect to :g:`cIn` is :math:`|OA|^2 - 1^2 = 4 - 1 = 3`. Along secant :g:`AFH`, any "
            "equilateral triangle :g:`FGH` inscribed in :g:`cIn` has side :math:`|FH| = \\sqrt{3}`. "
            "By the Tangent-Secant / Power-of-a-Point theorem, :math:`|AF| \\cdot |AH| = |AF|(|AF| + \\sqrt{3}) = 3`. "
            "Dividing by :math:`3` gives :math:`(|AF|/\\sqrt{3})^2 + (|AF|/\\sqrt{3}) - 1 = 0`, so "
            ":math:`|AF| = \\sqrt{3}/\\phi` and :math:`|FH|/|AF| = \\phi`."
        ),
        notes_prose=(
            "Discovered by :person:`Tran Quang Hung <tran-quang-hung>` (:cite:`Cut-the-Knot <ctk-buratino2>`), "
            "this rotational-pinwheel configuration embeds three simultaneous golden sections with :math:`C_3` "
            "symmetry inside :math:`\\mathbb{Q}(\\sqrt{3}, \\phi)`."
        ),
        terms=("power-of-a-point", "golden-section"),
        builder=build_tran_incircle_equilateral,
    ),
    ConstructionSpec(
        slug="06-tran-hexagon-square",
        catalog_code="GC-02.06",
        family_slug="02-equilateral-hexagon",
        order=6,
        title="Regular Hexagon & External Square Compass Sweep",
        short_title="Hexagon & Square Sweep",
        discoverers=("tran-quang-hung",),
        year="2014",
        citations=("ctk-buratino3", "bogomolny-golden-ratio"),
        ctk_url="https://www.cut-the-knot.org/do_you_know/Buratino3.shtml",
        ctk_title="Golden Ratio in Hexagon",
        number_field=r"\mathbb{Q}(\sqrt{3}, \phi)",
        number_field_text="Q(√3, φ)",
        enunciation=(
            "Given regular hexagon :g:`ABCDEF` and external square :g:`ABHG` on side :g:`AB`, "
            "circle :g:`cAH` centered at :g:`A` through opposite square corner :g:`H` cuts "
            "hexagon sides :g:`EF` at :g:`I` and :g:`BC` at :g:`L` in the golden ratio: "
            ":math:`|FI|/|IE| = |BL|/|LC| = \\phi`."
        ),
        given_prose=(
            "Regular hexagon :g:`ABCDEF` on side :g:`AB` from :g:`A` :math:`= (0, 0)` to :g:`B` :math:`= (2, 0)`."
        ),
        steps_prose=(
            "Construct regular hexagon :g:`ABCDEF` of side :math:`2` above :g:`AB`.",
            "Construct external square :g:`ABHG` of side :math:`2` below :g:`AB` and diagonal :g:`AH` of length :math:`2\\sqrt{2}`.",
            "Draw circle :g:`cAH` centered at :g:`A` through :g:`H`, intersecting side :g:`EF` at :g:`I` and side :g:`BC` at :g:`L`.",
        ),
        proof_prose=(
            "In :math:`\\triangle AFI`, :math:`|AF| = 2`, :math:`\\angle AFI = 120^\\circ`, and radius "
            ":math:`|AI| = |AH| = 2\\sqrt{2}`. Letting :math:`t = |FI|`, the Law of Cosines gives "
            ":math:`8 = 4 + t^2 - 2(2)t\\cos 120^\\circ = t^2 + 2t + 4`, so :math:`t^2 + 2t - 4 = 0` "
            "and :math:`t = \\sqrt{5} - 1 = 2/\\phi`. Since side :math:`|FE| = 2`, the remaining segment "
            "is :math:`|IE| = 2 - (\\sqrt{5} - 1) = 3 - \\sqrt{5} = 2/\\phi^2`, proving :math:`|FI|/|IE| = \\phi`."
        ),
        notes_prose=(
            "Notice the structural duality between :person:`Tran Quang Hung <tran-quang-hung>`'s hexagon "
            "construction (:cite:`Cut-the-Knot <ctk-buratino3>`) and :person:`Michel Bataille <michel-bataille>`'s "
            "equilateral triangle construction: replacing the :math:`60^\\circ` interior angle with the "
            "hexagon's :math:`120^\\circ` angle flips :math:`t^2 - 2t - 4 = 0` to :math:`t^2 + 2t - 4 = 0`, "
            "bringing the intersection **inside** side :g:`EF`."
        ),
        terms=("golden-section", "quadrance"),
        builder=build_tran_hexagon_square,
    ),
    ConstructionSpec(
        slug="07-nguyen-butterfly-equilateral",
        catalog_code="GC-02.07",
        family_slug="02-equilateral-hexagon",
        order=7,
        title="Butterfly Chords Astride an Equilateral Triangle",
        short_title="Butterfly Equilateral",
        discoverers=("nguyen-thanh-dung",),
        year="2016",
        citations=("ctk-butterfly-equilateral", "bogomolny-golden-ratio"),
        ctk_url="https://www.cut-the-knot.org/do_you_know/GoldenRatioAstrideEquilateralTriangle.shtml",
        ctk_title="Golden Ratio in a Butterfly Astride an Equilateral Triangle",
        number_field=r"\mathbb{Q}(\sqrt{3}, \phi)",
        number_field_text="Q(√3, φ)",
        enunciation=(
            "Let :g:`I` be the midpoint of radius :g:`OJ` of circle :g:`cO`, :g:`XT` the chord "
            "perpendicular to :g:`OJ` through :g:`I`, and :g:`ICD` an equilateral triangle symmetric "
            "about :g:`OJ` with :g:`C` and :g:`D` on :g:`cO`. If rays :g:`CI` and :g:`DI` meet :g:`cO` "
            "again at :g:`A` and :g:`B`, then chords :g:`BC` and :g:`AD` cut :g:`XT` at :g:`Y` and :g:`Z` "
            "with :math:`|YZ|/|ZT| = |YT|/|YZ| = |YZ|/|XY| = \\phi`."
        ),
        given_prose=(
            "Circle :g:`cO` centered at :g:`O` :math:`= (0, 0)` through :g:`J` :math:`= (0, 2)` with "
            "radius midpoint :g:`I` :math:`= (0, 1)`."
        ),
        steps_prose=(
            "Draw chord :g:`XT` through :g:`I` perpendicular to :g:`OJ`, meeting :g:`cO` at :g:`X` :math:`= (-\\sqrt{3}, 1)` and :g:`T` :math:`= (\\sqrt{3}, 1)`.",
            "Inscribe equilateral triangle :g:`ICD` with apex :g:`I` and base vertices :g:`C`, :g:`D` on :g:`cO`.",
            "Extend :g:`CI` and :g:`DI` to meet :g:`cO` at :g:`A` and :g:`B`, then draw butterfly chords :g:`BC` and :g:`AD` cutting :g:`XT` at :g:`Y` and :g:`Z`.",
        ),
        proof_prose=(
            "For :g:`C` and :g:`D` on :math:`x^2 + y^2 = 4` forming equilateral :g:`ICD` of side :math:`s` "
            "below :g:`I` :math:`= (0, 1)`, :math:`(s/2)^2 + (1 - s\\sqrt{3}/2)^2 = 4 \\implies s^2 - \\sqrt{3}\\,s - 3 = 0`, "
            "giving :math:`s = \\sqrt{3}\\,\\phi` directly. By the Butterfly Theorem and symmetry across "
            ":g:`OJ`, :math:`|IY| = |IZ| = \\sqrt{3}/(2\\phi)`, while :math:`|IT| = \\sqrt{3}`. "
            "Hence :math:`|YZ| = \\sqrt{3}/\\phi` and :math:`|ZT| = \\sqrt{3}(1 - 1/(2\\phi))`—moreover "
            ":math:`|YZ|/|ZT| = |YT|/|YZ| = |YZ|/|XY| = \\phi`, forming the 4-point golden chain :math:`(X, Y, Z, T)`."
        ),
        notes_prose=(
            "Discovered by :person:`Nguyen Thanh Dung <nguyen-thanh-dung>` (:cite:`Cut-the-Knot <ctk-butterfly-equilateral>`), "
            "this synthesis of Odom's equilateral chord and the classical **Butterfly Theorem** creates "
            "four collinear points :math:`(X, Y, Z, T)` with three overlapping golden sections on :g:`XT`."
        ),
        terms=("butterfly-theorem", "golden-chain", "golden-section"),
        builder=build_nguyen_butterfly_equilateral,
    ),
)
