"""Family 01: Classical & Minimal-Step Compass-and-Straightedge Constructions.

Catalogs Euclid's foundational *Elements* II.11 division, the right-triangle
hypotenuse transfer, Émile Lemoine and Kurt Hofstetter's minimal 5-step
constructions, Mascheroni 5-circle compass-only division, rusty-compass
division, and Bùi Quang Tuân's 5-step circle secant construction.
"""

from __future__ import annotations

import sympy as sp

from .helpers import make_result, new_catalog_model
from .schema import ConstructionResult, ConstructionSpec


def build_euclid_ii_11() -> ConstructionResult:
    """Euclid's Elements II.11 & VI.30 square-and-midpoint division of AB."""
    m = new_catalog_model("euclid-ii-11")
    A = m.set_point(0, 0, classes=["given"], ID="A")
    B = m.set_point(2, 0, classes=["given"], ID="B")
    D = m.set_point(0, 2, ID="D")
    C = m.set_point(2, 2, ID="C")

    m.construct_polygon([A, B, C, D], ID="ABCD")
    ln_ad = m.construct_line(A, D, classes=["auxiliary"], ID="AD")
    seg_ab = m.construct_segment(A, B, ID="segAB")

    # Midpoint M of side AD and compass transfer M(B) onto ray DA
    M = m.set_point(0, 1, ID="M")
    m.construct_segment(M, B, classes=["auxiliary"], ID="MB")
    c_mb = m.construct_circle(M, B, classes=["compass"], ID="cMB")
    E = m.intersect(c_mb, ln_ad, beyond=(D, A), ID="E")

    # Transfer AE onto AB at G (and erect golden gnomon square AEFH)
    c_ae = m.construct_circle(A, E, classes=["golden"], ID="cAE")
    G = m.intersect(c_ae, seg_ab, between=(A, B), classes=["golden"], ID="G")
    F = m.set_point(G.x, E.y, ID="F")
    m.construct_polygon([A, G, F, E], classes=["golden"], ID="AGFE")

    return make_result(m, ("A", "G"), ("G", "B"), ("A", "G", "B"))


def build_pythagorean_transfer() -> ConstructionResult:
    """Heron-Ptolemy right-triangle hypotenuse transfer on a 1:2 right triangle."""
    m = new_catalog_model("pythagorean-transfer")
    A = m.set_point(0, 0, classes=["given"], ID="A")
    B = m.set_point(2, 0, classes=["given"], ID="B")
    M = m.set_point(1, 0, ID="M")
    C = m.set_point(2, 1, ID="C")

    seg_ab = m.construct_segment(A, B, ID="AB")
    m.construct_segment(B, C, ID="BC")
    ln_ac = m.construct_line(A, C, classes=["auxiliary"], ID="AC")
    m.construct_polygon([A, B, C], ID="ABC")

    c_bm = m.construct_circle(B, M, classes=["auxiliary"], ID="cBM")
    _ = c_bm
    c_cb = m.construct_circle(C, B, classes=["compass"], ID="cCB")
    D = m.intersect(c_cb, ln_ac, between=(A, C), ID="D")
    E = m.intersect(c_cb, ln_ac, beyond=(A, C), ID="E")

    c_ad = m.construct_circle(A, D, classes=["golden"], ID="cAD")
    m.intersect(c_ad, seg_ab, between=(A, B), classes=["golden"], ID="G")
    _ = E

    return make_result(m, ("A", "G"), ("G", "B"), ("A", "G", "B"))


def build_lemoine_hofstetter_5step() -> ConstructionResult:
    """Lemoine (1902), Reusch (1904) & Hofstetter (2003) 5-step segment division."""
    m = new_catalog_model("lemoine-hofstetter-5step")
    A = m.set_point(0, 0, classes=["given"], ID="A")
    B = m.set_point(1, 0, classes=["given"], ID="B")

    ln_ab = m.construct_line(A, B, ID="AB")
    c_ab = m.construct_circle(A, B, classes=["compass"], ID="cAB")
    c_ba = m.construct_circle(B, A, classes=["compass"], ID="cBA")
    C = m.intersect(c_ab, c_ba, side_of=(A, B, 1), ID="C")
    D = m.intersect(c_ab, c_ba, side_of=(A, B, -1), ID="D")

    ln_cd = m.construct_line(C, D, classes=["auxiliary"], ID="CD")
    c_ca = m.construct_circle(C, A, classes=["compass"], ID="cCA")
    E = m.intersect(c_ca, c_ab, other_than=B, ID="E")
    F = m.intersect(c_ca, ln_cd, between=(C, D), ID="F")

    c_ef = m.construct_circle(E, F, classes=["golden"], ID="cEF")
    m.intersect(c_ef, ln_ab, between=(A, B), classes=["golden"], ID="G")
    G1 = m.intersect(c_ef, ln_ab, beyond=(B, A), ID="G1")
    _ = G1

    return make_result(m, ("A", "G"), ("G", "B"), ("A", "G", "B"))


def build_hofstetter_5step_2004() -> ConstructionResult:
    """Kurt Hofstetter's 2004 5-step straightedge-and-compass division."""
    m = new_catalog_model("hofstetter-5step-2004")
    A = m.set_point(0, 0, classes=["given"], ID="A")
    B = m.set_point(1, 0, classes=["given"], ID="B")

    # 5 elementary Euclidean steps: line AB, circles A(B), B(A), E(B), line DF
    ln_ab = m.construct_line(A, B, ID="AB")
    c_ab = m.construct_circle(A, B, classes=["compass"], ID="cAB")
    E = m.intersect(c_ab, ln_ab, beyond=(B, A), ID="E")
    c_ba = m.construct_circle(B, A, classes=["compass"], ID="cBA")
    C = m.intersect(c_ab, c_ba, side_of=(A, B, 1), ID="C")
    D = m.intersect(c_ab, c_ba, side_of=(A, B, -1), ID="D")
    _ = C

    c_eb = m.construct_circle(E, B, classes=["compass"], ID="cEB")
    F = m.intersect(c_eb, c_ba, side_of=(A, B, 1), ID="F")
    ln_df = m.construct_line(D, F, classes=["golden"], ID="DF")
    m.intersect(ln_df, ln_ab, classes=["golden"], ID="G")

    return make_result(m, ("A", "G"), ("G", "B"), ("A", "G", "B"))


def build_hofstetter_compass_only() -> ConstructionResult:
    """Kurt Hofstetter's 2002 Mascheroni 5-circle compass-only construction."""
    m = new_catalog_model("hofstetter-compass-only")
    A = m.set_point(0, 0, classes=["given"], ID="A")
    B = m.set_point(1, 0, classes=["given"], ID="B")

    # Strictly 5 circles and 0 lines
    c1 = m.construct_circle(A, B, classes=["compass"], ID="c1")
    c2 = m.construct_circle(B, A, classes=["compass"], ID="c2")
    C = m.intersect(c1, c2, side_of=(A, B, 1), ID="C")
    D = m.intersect(c1, c2, side_of=(A, B, -1), ID="D")

    c3 = m.construct_circle(C, D, classes=["compass"], ID="c3")
    E = m.intersect(c3, c1, other_than=D, ID="E")
    F = m.intersect(c3, c2, other_than=D, ID="F")

    c4 = m.construct_circle(B, E, classes=["golden"], ID="c4")
    c5 = m.construct_circle(A, F, classes=["golden"], ID="c5")
    m.intersect(c4, c5, side_of=(A, B, -1), classes=["golden"], ID="X")
    Y = m.intersect(c4, c5, side_of=(A, B, 1), classes=["golden"], ID="Y")
    _ = Y

    return make_result(m, ("C", "D"), ("D", "X"), ("C", "D", "X"))


def build_hofstetter_rusty_compass() -> ConstructionResult:
    """Kurt Hofstetter's 2005 fixed-opening rusty-compass golden division."""
    m = new_catalog_model("hofstetter-rusty-compass")
    A = m.set_point(0, 0, classes=["given"], ID="A")
    B = m.set_point(1, 0, classes=["given"], ID="B")

    ln_ab = m.construct_line(A, B, ID="AB")
    c_ab = m.construct_circle(A, B, classes=["compass"], ID="cAB")
    c_ba = m.construct_circle(B, A, classes=["compass"], ID="cBA")
    C = m.intersect(c_ab, c_ba, side_of=(A, B, 1), ID="C")
    D = m.intersect(c_ab, c_ba, side_of=(A, B, -1), ID="D")

    ln_cd = m.construct_line(C, D, classes=["auxiliary"], ID="CD")
    M = m.intersect(ln_ab, ln_cd, ID="M")

    # Rusty compass opening fixed at |AB| = 1 placed at midpoint M
    R1 = m.set_point(sp.Rational(3, 2), 0, guide=True, ID="R1")
    c_m = m.construct_circle(M, R1, classes=["compass"], ID="cM")
    F = m.intersect(c_m, c_ba, side_of=(A, B, 1), ID="F")

    ln_df = m.construct_line(D, F, classes=["golden"], ID="DF")
    m.intersect(ln_df, ln_ab, classes=["golden"], ID="G")

    return make_result(m, ("A", "G"), ("G", "B"), ("A", "G", "B"))


def build_bui_5step() -> ConstructionResult:
    """Bùi Quang Tuân's 5-step collinear three-circle secant construction."""
    m = new_catalog_model("bui-5step")
    O = m.set_point(0, 0, classes=["given"], ID="O")
    B = m.set_point(-1, 0, classes=["given"], ID="B")

    # 1. Line L, 2. Circle O(B), 3. Circle B(A), 4. Circle C(O), 5. Line MN
    ln_l = m.construct_line(O, B, ID="L")
    c_o = m.construct_circle(O, B, classes=["primary"], ID="cO")
    A = m.intersect(c_o, ln_l, other_than=B, ID="A")

    c_ba = m.construct_circle(B, A, classes=["compass"], ID="cBA")
    C = m.intersect(c_ba, ln_l, other_than=A, ID="C")

    c_co = m.construct_circle(C, O, classes=["compass"], ID="cCO")
    M = m.intersect(c_co, c_o, side_of=(O, A, 1), ID="M")
    N = m.intersect(c_co, c_ba, side_of=(O, A, -1), ID="N")

    ln_mn = m.construct_line(M, N, classes=["golden"], ID="MN")
    m.intersect(ln_mn, c_o, other_than=M, classes=["golden"], ID="P")

    return make_result(m, ("M", "P"), ("P", "N"), ("M", "P", "N"))


MINIMAL_COMPASS_SPECS: tuple[ConstructionSpec, ...] = (
    ConstructionSpec(
        slug="01-euclid-ii-11",
        catalog_code="GC-01.01",
        family_slug="01-minimal-compass",
        order=1,
        title="Euclid's Classical Golden Section (Elements II.11 & VI.30)",
        short_title="Euclid II.11 & VI.30",
        discoverers=("euclid",),
        year="c. 300 BCE",
        citations=("euclid-elements", "bogomolny-golden-ratio", "huntley-1970"),
        ctk_url="https://www.cut-the-knot.org/do_you_know/GoldenRatio.shtml",
        ctk_title="Golden Ratio in Geometry",
        number_field=r"\mathbb{Q}(\phi)",
        number_field_text="Q(φ)",
        enunciation=(
            "Given a straight segment :g:`AB`, erect the square :g:`ABCD`, bisect side "
            ":g:`AD` at :g:`M`, and transfer :g:`MB` along ray :g:`DA` beyond :g:`A` to "
            ":g:`E`. Swinging :g:`AE` onto :g:`AB` at :g:`G` cuts :g:`AB` in :term:`extreme "
            "and mean ratio <extreme-and-mean-ratio>`, so that :math:`|AB|/|AG| = |AG|/|GB| = \\phi`."
        ),
        given_prose=(
            "Endpoints :g:`A` at :math:`(0, 0)` and :g:`B` at :math:`(2, 0)` defining a "
            "base segment :g:`AB` of length :math:`2`."
        ),
        steps_prose=(
            "Erect square :g:`ABCD` on base :g:`AB` with :g:`D` at :math:`(0, 2)` and :g:`C` at :math:`(2, 2)`.",
            "Bisect vertical side :g:`AD` at midpoint :g:`M` :math:`= (0, 1)` and join diagonal-radius :g:`MB` of length :math:`\\sqrt{5}`.",
            "Draw compass circle :g:`cMB` centered at :g:`M` through :g:`B`, cutting line :g:`AD` extended below :g:`A` at :g:`E` :math:`= (0, 1 - \\sqrt{5})`.",
            "Draw circle :g:`cAE` centered at :g:`A` through :g:`E`, cutting :g:`AB` internally at :g:`G` :math:`= (\\sqrt{5} - 1, 0)` and completing the golden square :g:`AGFE`.",
        ),
        proof_prose=(
            "In right triangle :math:`\\triangle MAB`, :math:`Q(M, A) = 1` and :math:`Q(A, B) = 4`, "
            "so :term:`quadrance <quadrance>` :math:`Q(M, B) = 5` and :math:`|ME| = |MB| = \\sqrt{5}`. "
            "Subtracting :math:`|MA| = 1` gives :math:`|AG| = |AE| = \\sqrt{5} - 1 = 2/\\phi`, while "
            "the remainder on :g:`AB` has length :math:`|GB| = 2 - (\\sqrt{5} - 1) = 3 - \\sqrt{5} = 2/\\phi^2`. "
            "Hence :math:`Q(A, G) = 6 - 2\\sqrt{5}` and :math:`Q(G, B) = 14 - 6\\sqrt{5}`, satisfying "
            ":math:`Q(A, G) = (\\phi + 1)\\,Q(G, B)` and :math:`|AG|/|GB| = \\phi`."
        ),
        notes_prose=(
            "In Book II Proposition 11 of the *Elements*, :person:`Euclid <euclid>` formulates this "
            "construction purely in the language of geometric algebra—requiring that rectangle "
            ":math:`AB \\cdot GB` equal square :g:`AGFE`—and returns to it in Book VI Proposition 30 "
            "using theory of proportions (:cite:`Euclid <euclid-elements>`). In :person:`Alexander "
            "Bogomolny <alexander-bogomolny>`'s survey (:cite:`Cut-the-Knot <bogomolny-golden-ratio>`), "
            "this construction anchors all subsequent minimal-step refinements."
        ),
        terms=("extreme-and-mean-ratio", "golden-section", "quadrance"),
        builder=build_euclid_ii_11,
    ),
    ConstructionSpec(
        slug="02-pythagorean-transfer",
        catalog_code="GC-01.02",
        family_slug="01-minimal-compass",
        order=2,
        title="Right-Triangle Hypotenuse Transfer (1 : 2 : √5)",
        short_title="Hypotenuse Transfer",
        discoverers=("euclid",),
        year="Classical",
        citations=("bogomolny-golden-ratio", "huntley-1970"),
        ctk_url="https://www.cut-the-knot.org/do_you_know/GoldenRatio.shtml#construct",
        ctk_title="Golden Ratio in Geometry — Classical Right-Triangle Division",
        number_field=r"\mathbb{Q}(\phi)",
        number_field_text="Q(φ)",
        enunciation=(
            "On segment :g:`AB` of length :math:`2`, erect perpendicular leg :g:`BC` of length "
            ":math:`1 = \\tfrac{1}{2}|AB|`. Circle :g:`cCB` cuts hypotenuse :g:`AC` at :g:`D` "
            "(and ray :g:`AC` at :g:`E`), and circle :g:`cAD` transfers :g:`AD` onto :g:`AB` at "
            ":g:`G`, dividing :g:`AB` in the golden ratio :math:`|AG|/|GB| = \\phi`."
        ),
        given_prose=(
            "Segment :g:`AB` from :g:`A` :math:`= (0, 0)` to :g:`B` :math:`= (2, 0)` with midpoint "
            ":g:`M` :math:`= (1, 0)` and perpendicular leg endpoint :g:`C` :math:`= (2, 1)`."
        ),
        steps_prose=(
            "Form the :math:`1 : 2 : \\sqrt{5}` right triangle :g:`ABC` with right angle at :g:`B` and line :g:`AC`.",
            "Draw circle :g:`cCB` centered at :g:`C` through :g:`B` (radius :math:`1`), intersecting :g:`AC` internally at :g:`D` and externally at :g:`E`.",
            "Draw circle :g:`cAD` centered at :g:`A` through :g:`D`, meeting segment :g:`AB` at :g:`G`.",
        ),
        proof_prose=(
            "Since :math:`|AB| = 2` and :math:`|BC| = 1`, hypotenuse :g:`AC` has length :math:`\\sqrt{5}`. "
            "Circle :g:`cCB` subtracts and adds unit radius :math:`1` along line :g:`AC`, yielding "
            ":math:`|AD| = \\sqrt{5} - 1 = 2/\\phi` and :math:`|AE| = \\sqrt{5} + 1 = 2\\phi`. "
            "Along :g:`AC`, :math:`|AE|/|DE| = (2\\phi)/2 = \\phi`, while transferring :math:`|AD|` to "
            ":g:`AG` on :g:`AB` produces :math:`|AG|/|GB| = (\\sqrt{5} - 1)/(3 - \\sqrt{5}) = \\phi`."
        ),
        notes_prose=(
            "Cataloged at the opening of :cite:`Bogomolny's Golden Ratio overview <bogomolny-golden-ratio>` "
            "and popularized by :person:`H. E. Huntley <h-e-huntley>` (:cite:`Huntley 1970 <huntley-1970>`), "
            "this streamlined distillation of Euclid II.11 simultaneously exhibits both :math:`2/\\phi` (at :g:`D`) "
            "and :math:`2\\phi` (at :g:`E`) along a single secant line :g:`AC`."
        ),
        terms=("golden-section", "quadrance", "golden-chain"),
        builder=build_pythagorean_transfer,
    ),
    ConstructionSpec(
        slug="03-lemoine-hofstetter-5step",
        catalog_code="GC-01.03",
        family_slug="01-minimal-compass",
        order=3,
        title="Lemoine–Reusch–Hofstetter 5-Step Division",
        short_title="Lemoine–Hofstetter 5-Step",
        discoverers=("emile-lemoine", "kurt-hofstetter"),
        year="1902 / 2003",
        citations=("lemoine-1902", "hofstetter-2003", "bogomolny-golden-ratio"),
        ctk_url="https://www.cut-the-knot.org/do_you_know/GoldenRatio.shtml#5step",
        ctk_title="Golden Ratio in Geometry — 5-Step Construction",
        number_field=r"\mathbb{Q}(\sqrt{3}, \phi)",
        number_field_text="Q(√3, φ)",
        enunciation=(
            "Given points :g:`A` and :g:`B` on line :g:`AB`, let unit vesica circles :g:`cAB` and "
            ":g:`cBA` meet at :g:`C` and :g:`D`. Circle :g:`cCA` cuts :g:`cAB` at :g:`E` and chord "
            ":g:`CD` at :g:`F`; then circle :g:`cEF` cuts :g:`AB` internally at :g:`G` and externally "
            "at :g:`G_1 <G1>` so that :math:`|AG|/|GB| = |G_1A|/|AB| = \\phi`."
        ),
        given_prose=(
            "Unit base points :g:`A` :math:`= (0, 0)` and :g:`B` :math:`= (1, 0)` on carrier line :g:`AB`."
        ),
        steps_prose=(
            "Draw circles :g:`cAB` and :g:`cBA` of unit radius, intersecting at :g:`C` :math:`= (\\tfrac{1}{2}, \\tfrac{\\sqrt{3}}{2})` and :g:`D` :math:`= (\\tfrac{1}{2}, -\\tfrac{\\sqrt{3}}{2})`.",
            "Join perpendicular bisector line :g:`CD`.",
            "Draw circle :g:`cCA` centered at :g:`C` through :g:`A`, intersecting :g:`cAB` at :g:`E` :math:`= (-\\tfrac{1}{2}, \\tfrac{\\sqrt{3}}{2})` and segment :g:`CD` at :g:`F` :math:`= (\\tfrac{1}{2}, \\tfrac{\\sqrt{3}}{2} - 1)`.",
            "Draw circle :g:`cEF` centered at :g:`E` through :g:`F`, cutting :g:`AB` internally at :g:`G` and externally at :g:`G_1 <G1>`.",
        ),
        proof_prose=(
            "Because :g:`E` and :g:`C` share ordinate :math:`\\tfrac{\\sqrt{3}}{2}` at horizontal separation "
            ":math:`1`, while :g:`F` lies :math:`1` unit directly below :g:`C`, triangle :math:`\\triangle ECF` "
            "is right isosceles with :math:`Q(E, F) = 1^2 + 1^2 = 2`. Circle :g:`cEF` therefore satisfies "
            ":math:`(x + \\tfrac{1}{2})^2 + y^2 = 2`; setting :math:`y = 0` yields :math:`(x + \\tfrac{1}{2})^2 = 2 - \\tfrac{3}{4} = \\tfrac{5}{4}`, "
            "giving :g:`G` :math:`= (1/\\phi, 0)` and :g:`G_1 <G1>` :math:`= (-\\phi, 0)`. Thus :math:`|AG|/|GB| = \\phi` "
            "and :math:`(G_1, A, G, B)` forms a connected golden chain along :g:`AB`."
        ),
        notes_prose=(
            "Rediscovered independently by :person:`Kurt Hofstetter <kurt-hofstetter>` (:cite:`Hofstetter 2003 <hofstetter-2003>`), "
            "this five-locus division of a pre-drawn line segment had appeared a century earlier in "
            ":person:`Émile Lemoine <emile-lemoine>`'s *Géométrographie* (:cite:`Lemoine 1902 <lemoine-1902>`) "
            "and J. Reusch's *Planymetrische Konstruktionen in geometrographischer Ausführung* (1904)."
        ),
        terms=("geometrographie", "golden-section", "golden-chain", "vesica-piscis"),
        builder=build_lemoine_hofstetter_5step,
        svg_bbox=(-1.85, 2.15, -1.65, 2.05),
    ),
    ConstructionSpec(
        slug="04-hofstetter-5step-2004",
        catalog_code="GC-01.04",
        family_slug="01-minimal-compass",
        order=4,
        title="Hofstetter's 2004 Five-Step Secant Division",
        short_title="Hofstetter 5-Step (2004)",
        discoverers=("kurt-hofstetter",),
        year="2004",
        citations=("hofstetter-2004", "ctk-hofstetter3"),
        ctk_url="https://www.cut-the-knot.org/do_you_know/Hofstetter3.shtml",
        ctk_title="5-Step Construction of the Golden Ratio, One of Many",
        number_field=r"\mathbb{Q}(\sqrt{3}, \phi)",
        number_field_text="Q(√3, φ)",
        enunciation=(
            "Given points :g:`A` and :g:`B`, draw line :g:`AB` and unit circles :g:`cAB`, :g:`cBA` "
            "meeting at :g:`C` and :g:`D`, with :g:`cAB` meeting ray :g:`BA` beyond :g:`A` at :g:`E`. "
            "Circle :g:`cEB` cuts :g:`cBA` above :g:`AB` at :g:`F`, and secant :g:`DF` divides :g:`AB` "
            "at :g:`G` in the golden ratio :math:`|AG|/|GB| = \\phi` in exactly five Euclidean loci."
        ),
        given_prose=(
            "Points :g:`A` :math:`= (0, 0)` and :g:`B` :math:`= (1, 0)` in the Euclidean plane."
        ),
        steps_prose=(
            "Draw carrier line :g:`AB` (Locus 1).",
            "Draw circle :g:`cAB` centered at :g:`A` through :g:`B` (Locus 2), meeting line :g:`AB` beyond :g:`A` at :g:`E` :math:`= (-1, 0)`.",
            "Draw circle :g:`cBA` centered at :g:`B` through :g:`A` (Locus 3), intersecting :g:`cAB` at :g:`C` and :g:`D` :math:`= (\\tfrac{1}{2}, -\\tfrac{\\sqrt{3}}{2})`.",
            "Draw circle :g:`cEB` centered at :g:`E` through :g:`B` of radius :math:`2` (Locus 4), meeting :g:`cBA` above :g:`AB` at :g:`F` :math:`= (\\tfrac{3}{4}, \\tfrac{\\sqrt{15}}{4})`.",
            "Draw line :g:`DF` (Locus 5), cutting :g:`AB` at :g:`G` :math:`= (1/\\phi, 0)`.",
        ),
        proof_prose=(
            "Subtracting :math:`(x - 1)^2 + y^2 = 1` from :math:`(x + 1)^2 + y^2 = 4` gives :math:`4x = 3`, "
            "so :g:`F` has exact coordinates :math:`(\\tfrac{3}{4}, \\tfrac{\\sqrt{15}}{4})`. Along secant "
            ":g:`DF` joining :math:`(\\tfrac{1}{2}, -\\tfrac{\\sqrt{3}}{2})` to :math:`(\\tfrac{3}{4}, \\tfrac{\\sqrt{15}}{4})`, "
            "the :math:`x`-intercept :g:`G` is :math:`x_G = \\tfrac{1}{2} + \\tfrac{1}{4} \\cdot \\frac{\\sqrt{3}/2}{\\sqrt{3}/2 + \\sqrt{15}/4} "
            "= \\tfrac{1}{2} + \\frac{1}{2(\\sqrt{5} + 2)} = \\frac{\\sqrt{5} - 1}{2} = \\frac{1}{\\phi}`. "
            "Therefore :math:`|AG| = 1/\\phi`, :math:`|GB| = 1/\\phi^2`, and :math:`|AG|/|GB| = \\phi`."
        ),
        notes_prose=(
            "Published in *Forum Geometricorum* (:cite:`Hofstetter 2004 <hofstetter-2004>`), this "
            "construction requires only **two lines and three circles** even when the line through :g:`A` "
            "and :g:`B` is not drawn in advance. Notice that its abscissae :math:`x_D = \\tfrac{1}{2}` and "
            ":math:`x_F = \\tfrac{3}{4}` (or under reflection :math:`\\tfrac{1}{4}, \\tfrac{1}{2}`) are a "
            "special case of :person:`Bùi Quang Tuân <bui-quang-tuan>`'s general bilinear circle theorem (:cite:`Cut-the-Knot <ctk-hofstetter3>`)."
        ),
        terms=("geometrographie", "golden-section", "vesica-piscis"),
        builder=build_hofstetter_5step_2004,
        svg_bbox=(-3.15, 2.15, -2.15, 2.15),
    ),
    ConstructionSpec(
        slug="05-hofstetter-compass-only",
        catalog_code="GC-01.05",
        family_slug="01-minimal-compass",
        order=5,
        title="Mascheroni Five-Circle Compass-Only Construction",
        short_title="Compass-Only (5 Circles)",
        discoverers=("kurt-hofstetter",),
        year="2002",
        citations=("hofstetter-2002", "ctk-compass-only"),
        ctk_url="https://www.cut-the-knot.org/do_you_know/GoldenRatioByCompass.shtml",
        ctk_title="Golden Ratio by Compass Only",
        number_field=r"\mathbb{Q}(\sqrt{3}, \phi)",
        number_field_text="Q(√3, φ)",
        enunciation=(
            "Using a compass alone and **zero straightedge lines**, five circles constructed from "
            "given points :g:`A` and :g:`B` generate four collinear points :g:`Y`, :g:`C`, :g:`D`, :g:`X` "
            "such that :math:`|CX|/|CD| = |CD|/|DX| = \\phi`."
        ),
        given_prose=(
            "Two distinct points :g:`A` :math:`= (0, 0)` and :g:`B` :math:`= (1, 0)` with no lines drawn."
        ),
        steps_prose=(
            "Draw unit circles :g:`c1` :math:`= A(B)` and :g:`c2` :math:`= B(A)`, intersecting at :g:`C` and :g:`D`.",
            "Draw circle :g:`c3` :math:`= C(D)` of radius :math:`\\sqrt{3}`; without a ruler, :g:`c3` meets :g:`c1` again at :g:`E` :math:`= (-1, 0)` and :g:`c2` again at :g:`F` :math:`= (2, 0)`.",
            "Draw radius-:math:`2` circles :g:`c4` :math:`= B(E)` and :g:`c5` :math:`= A(F)`, intersecting at :g:`X` :math:`= (\\tfrac{1}{2}, -\\tfrac{\\sqrt{15}}{2})` and :g:`Y` :math:`= (\\tfrac{1}{2}, \\tfrac{\\sqrt{15}}{2})`.",
        ),
        proof_prose=(
            "For :g:`C` :math:`= (\\tfrac{1}{2}, \\tfrac{\\sqrt{3}}{2})`, the quadrance to :math:`(-1, 0)` is "
            ":math:`(-\\tfrac{3}{2})^2 + (\\tfrac{\\sqrt{3}}{2})^2 = 3 = Q(C, D)`, confirming that :g:`E` and "
            "symmetrically :g:`F` lie on :g:`c3` without drawing line :math:`AB`. Circles :g:`c4` and :g:`c5` "
            "both have radius :math:`2` centered at :g:`B` and :g:`A`, so their intersections :g:`X` and :g:`Y` "
            "lie on the perpendicular bisector :math:`x = \\tfrac{1}{2}` alongside :g:`C` and :g:`D`, with "
            "ordinates :math:`\\pm\\tfrac{\\sqrt{15}}{2}`. Thus :math:`|CD| = \\sqrt{3}` and "
            ":math:`|DX| = \\tfrac{\\sqrt{15} - \\sqrt{3}}{2} = \\sqrt{3}/\\phi`, proving :math:`|CD|/|DX| = \\phi`."
        ),
        notes_prose=(
            "In accordance with the Mohr–Mascheroni theorem, every ruler-and-compass point construction "
            "can be executed by compass alone. :person:`Kurt Hofstetter <kurt-hofstetter>`'s five-circle "
            "construction (:cite:`Hofstetter 2002 <hofstetter-2002>`, :cite:`Cut-the-Knot <ctk-compass-only>`) "
            "achieves the golden section in just five arcs—and our :mod:`geometor.divine.golden` collinear "
            "point scanner detects the entire :math:`(Y, C, D, X)` golden chain automatically despite zero lines in the model."
        ),
        terms=("mascheroni-construction", "golden-chain", "vesica-piscis"),
        builder=build_hofstetter_compass_only,
        svg_bbox=(-2.25, 3.25, -2.35, 2.35),
    ),
    ConstructionSpec(
        slug="06-hofstetter-rusty-compass",
        catalog_code="GC-01.06",
        family_slug="01-minimal-compass",
        order=6,
        title="Hofstetter's Fixed-Aperture Rusty-Compass Division",
        short_title="Rusty Compass (2005)",
        discoverers=("kurt-hofstetter",),
        year="2005",
        citations=("hofstetter-2005", "ctk-rusty-compass"),
        ctk_url="https://www.cut-the-knot.org/do_you_know/GoldenRatioByRustyCompass.shtml",
        ctk_title="Golden Ratio with a Rusty Compass",
        number_field=r"\mathbb{Q}(\sqrt{3}, \phi)",
        number_field_text="Q(√3, φ)",
        enunciation=(
            "With a **rusty compass** locked permanently to aperture :math:`r = |AB|`, circles "
            ":g:`cAB` and :g:`cBA` determine midpoint :g:`M` via :g:`CD`; a third unit circle :g:`cM` "
            "centered at :g:`M` meets :g:`cBA` above :g:`AB` at :g:`F`, and line :g:`DF` cuts :g:`AB` "
            "at :g:`G` in the golden ratio :math:`|AG|/|GB| = \\phi`."
        ),
        given_prose=(
            "Unit segment endpoints :g:`A` :math:`= (0, 0)` and :g:`B` :math:`= (1, 0)` and a fixed compass radius :math:`r = 1`."
        ),
        steps_prose=(
            "Draw line :g:`AB` and unit circles :g:`cAB`, :g:`cBA` meeting at :g:`C` and :g:`D`.",
            "Join :g:`CD` to bisect :g:`AB` at :g:`M` :math:`= (\\tfrac{1}{2}, 0)`.",
            "With the unchanged compass opening :math:`r = 1`, draw circle :g:`cM` centered at :g:`M`, meeting :g:`cBA` farthest from :g:`D` at :g:`F` :math:`= (\\tfrac{3}{4}, \\tfrac{\\sqrt{15}}{4})`.",
            "Join :g:`DF` to intersect :g:`AB` at :g:`G` :math:`= (1/\\phi, 0)`.",
        ),
        proof_prose=(
            "Unit circles :g:`cM` :math:`((x - \\tfrac{1}{2})^2 + y^2 = 1)` and :g:`cBA` "
            ":math:`((x - 1)^2 + y^2 = 1)` intersect along their radical axis :math:`x = \\tfrac{3}{4}`, "
            "giving :g:`F` :math:`= (\\tfrac{3}{4}, \\tfrac{\\sqrt{15}}{4})`—the exact same upper intersection "
            "point achieved by radius-:math:`2` circle :math:`E(B)` in Hofstetter's 2004 construction! "
            "Hence line :g:`DF` meets :g:`AB` at :g:`G` :math:`= (1/\\phi, 0)`, so :math:`|AG|/|GB| = \\phi`."
        ),
        notes_prose=(
            "Poncelet–Steiner and Abū al-Wafāʾ tradition prizes constructions executed with a single "
            "fixed compass opening (*compas rouillé*). :person:`Kurt Hofstetter <kurt-hofstetter>` "
            "(:cite:`Hofstetter 2005 <hofstetter-2005>`, :cite:`Cut-the-Knot <ctk-rusty-compass>`) "
            "requires only **three unit circles** and **three lines**."
        ),
        terms=("rusty-compass", "golden-section", "vesica-piscis"),
        builder=build_hofstetter_rusty_compass,
        svg_bbox=(-1.25, 2.25, -1.25, 1.35),
    ),
    ConstructionSpec(
        slug="07-bui-5step",
        catalog_code="GC-01.07",
        family_slug="01-minimal-compass",
        order=7,
        title="Bùi Quang Tuân's Five-Step Three-Circle Secant",
        short_title="Bùi 5-Step Secant",
        discoverers=("bui-quang-tuan",),
        year="2014",
        citations=("ctk-bui-5step", "bogomolny-golden-ratio"),
        ctk_url="https://www.cut-the-knot.org/do_you_know/BuiGoldenRatio5Step.shtml",
        ctk_title="Golden Ratio in Five Steps",
        number_field=r"\mathbb{Q}(\sqrt{5}, \sqrt{7})",
        number_field_text="Q(√5, √7)",
        enunciation=(
            "On line :g:`L` through :g:`O`, draw circle :g:`cO` meeting :g:`L` at :g:`A` and :g:`B`, "
            "circle :g:`cBA` meeting :g:`L` at :g:`C`, and circle :g:`cCO` meeting :g:`cO` above :g:`L` "
            "at :g:`M` and :g:`cBA` below :g:`L` at :g:`N`. Then chord :g:`MN` cuts :g:`cO` at :g:`P` "
            "with :math:`|MN|/|MP| = |MP|/|PN| = \\phi`."
        ),
        given_prose=(
            "Center :g:`O` :math:`= (0, 0)` and unit point :g:`B` :math:`= (-1, 0)` defining carrier line :g:`L`."
        ),
        steps_prose=(
            "Draw line :g:`L` through :g:`O` and :g:`B`, and unit circle :g:`cO` meeting :g:`L` again at :g:`A` :math:`= (1, 0)`.",
            "Draw circle :g:`cBA` of radius :math:`2` centered at :g:`B` through :g:`A`, meeting :g:`L` beyond :g:`B` at :g:`C` :math:`= (-3, 0)`.",
            "Draw circle :g:`cCO` of radius :math:`3` centered at :g:`C` through :g:`O`, cutting :g:`cO` above :g:`L` at :g:`M` :math:`= (-\\tfrac{1}{6}, \\tfrac{\\sqrt{35}}{6})` and :g:`cBA` below :g:`L` at :g:`N` :math:`= (-\\tfrac{3}{4}, -\\tfrac{3\\sqrt{7}}{4})`.",
            "Join :g:`MN`, intersecting unit circle :g:`cO` a second time at :g:`P`.",
        ),
        proof_prose=(
            "Direct quadrance computation between :g:`M` and :g:`N` yields "
            ":math:`Q(M, N) = (\\tfrac{7}{12})^2 + (\\tfrac{\\sqrt{35}}{6} + \\tfrac{3\\sqrt{7}}{4})^2 "
            "= \\tfrac{21}{4} + \\tfrac{7\\sqrt{5}}{4} = \\tfrac{7}{2}\\phi^2`. Because :g:`O`, :g:`M`, "
            "and :g:`N` all lie on radius-:math:`3` circle :g:`cCO` while :g:`M` and :g:`P` lie on unit "
            "circle :g:`cO`, inscribed-angle similarity with diameter endpoint :math:`(-6, 0)` of :g:`cCO` "
            "gives :math:`Q(M, P) = \\tfrac{7}{2}` and :math:`Q(P, N) = \\tfrac{7}{2}\\phi^{-2}`. "
            "Hence :math:`Q(M, P) / Q(P, N) = \\phi^2` and :math:`|MP|/|PN| = \\phi`."
        ),
        notes_prose=(
            "Devised by :person:`Bùi Quang Tuân <bui-quang-tuan>` (:cite:`Cut-the-Knot <ctk-bui-5step>`), "
            "this five-step construction starts from an arbitrary radius on line :g:`L` rather than a "
            "pre-specified unit segment, generating :math:`\\phi` inside the biquadratic field "
            ":math:`\\mathbb{Q}(\\sqrt{5}, \\sqrt{7})`."
        ),
        terms=("geometrographie", "golden-section", "quadrance"),
        builder=build_bui_5step,
        svg_bbox=(-3.4, 1.5, -2.5, 2.2),
    ),
)
