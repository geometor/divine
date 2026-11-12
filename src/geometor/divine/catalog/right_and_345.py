"""Family 04: Right Triangles, Egyptian 3-4-5 & Kepler Proportions.

Catalogs H. E. Huntley's unexpected Golden Ratio in the 3-4-5 right triangle,
Johannes Kepler's geometric-progression right triangle, Jo Niemeyer's three
equal segments, and Bùi Quang Tuân's Van Obel right-isosceles configuration.
"""

from __future__ import annotations

import sympy as sp

from .helpers import make_result, new_catalog_model
from .schema import ConstructionResult, ConstructionSpec


def build_huntley_egyptian_345() -> ConstructionResult:
    """H. E. Huntley's unexpected appearance of phi in a 3-4-5 right triangle."""
    m = new_catalog_model("huntley-egyptian-345")
    C = m.set_point(0, 0, classes=["given"], ID="C")
    B = m.set_point(3, 0, classes=["given"], ID="B")
    A = m.set_point(0, 4, ID="A")

    m.construct_polygon([A, B, C], ID="ABC")

    # Angle bisector of <ABC meets AC at O=(0, 3/2); circle O(C) is tangent to AB at T=(6/5, 12/5)
    O = m.set_point(0, sp.Rational(3, 2), ID="O")
    T = m.set_point(sp.Rational(6, 5), sp.Rational(12, 5), ID="T")
    _ = T

    ln_bo = m.construct_line(B, O, classes=["golden"], ID="BO")
    c_oc = m.construct_circle(O, C, classes=["golden"], ID="cOC")

    m.intersect(c_oc, ln_bo, between=(B, O), classes=["golden"], ID="P")
    m.intersect(c_oc, ln_bo, beyond=(B, O), classes=["golden"], ID="Q")

    return make_result(m, ("P", "Q"), ("B", "P"), ("B", "P", "Q"))


def build_kepler_geometric_triangle() -> ConstructionResult:
    """Johannes Kepler's right triangle with sides in geometric progression (1597)."""
    m = new_catalog_model("kepler-geometric-triangle")
    phi = sp.Rational(1, 2) + sp.sqrt(5) / 2
    phi2 = phi + 1

    A = m.set_point(0, 0, classes=["given"], ID="A")
    H = m.set_point(phi, 0, classes=["golden"], ID="H")
    B = m.set_point(phi2, 0, classes=["given"], ID="B")
    O = m.set_point(phi2 / 2, 0, ID="O")

    ln_ab = m.construct_line(A, B, classes=["golden"], ID="AB")
    _ = ln_ab
    m.construct_circle(O, B, classes=["primary"], ID="cOB")

    # Geometric mean altitude |HC| = sqrt(|AH| * |HB|) = sqrt(phi)
    C = m.set_point(phi, sp.sqrt(phi), classes=["golden"], ID="C")
    m.construct_polygon([A, B, C], classes=["golden"], ID="ABC")
    m.construct_segment(H, C, classes=["auxiliary"], ID="HC")

    return make_result(m, ("A", "H"), ("H", "B"), ("A", "H", "B"))


def build_niemeyer_three_segments() -> ConstructionResult:
    """Jo Niemeyer's three equal segments leaning on a perpendicular line."""
    m = new_catalog_model("niemeyer-three-segments")
    s3 = sp.sqrt(3)

    A1 = m.set_point(0, 0, classes=["given"], ID="A1")
    B1 = m.set_point(2, 0, classes=["given"], ID="B1")
    B2 = m.set_point(1, 0, ID="B2")
    G0 = m.set_point(0, 1, guide=True, ID="G0")

    ln_l = m.construct_line(A1, G0, classes=["golden"], ID="L")
    m.construct_segment(A1, B1, ID="A1B1")

    # Second segment B2 A2 of length 2 with A2 on L
    R2 = m.set_point(3, 0, guide=True, ID="R2")
    c_b2 = m.construct_circle(B2, R2, classes=["compass"], ID="cB2")
    A2 = m.intersect(c_b2, ln_l, side_of=(A1, B1, 1), classes=["golden"], ID="A2")
    m.construct_segment(B2, A2, ID="B2A2")

    # Midpoint B3 of B2 A2 and third segment B3 A3 of length 2 with A3 on L
    B3 = m.set_point(sp.Rational(1, 2), s3 / 2, ID="B3")
    R3 = m.set_point(sp.Rational(5, 2), s3 / 2, guide=True, ID="R3")
    c_b3 = m.construct_circle(B3, R3, classes=["golden"], ID="cB3")
    A3 = m.intersect(c_b3, ln_l, beyond=(A1, A2), classes=["golden"], ID="A3")
    m.construct_segment(B3, A3, classes=["golden"], ID="B3A3")

    return make_result(m, ("A1", "A2"), ("A2", "A3"), ("A1", "A2", "A3"))


def build_bui_van_obel_isosceles() -> ConstructionResult:
    """Bùi Quang Tuân's Van Obel cevian division in a right isosceles triangle."""
    m = new_catalog_model("bui-van-obel-isosceles")
    B = m.set_point(-2, 0, classes=["given"], ID="B")
    C = m.set_point(2, 0, classes=["given"], ID="C")
    A = m.set_point(0, 2, ID="A")
    M = m.set_point(0, 0, ID="M")
    O = m.set_point(0, 1, ID="O")

    m.construct_polygon([A, B, C], ID="ABC")
    ln_am = m.construct_line(A, M, classes=["golden"], ID="AM")
    c_om = m.construct_circle(O, M, classes=["primary"], ID="cOM")

    ln_oc = m.construct_line(O, C, classes=["auxiliary"], ID="OC")
    ln_ob = m.construct_line(O, B, classes=["auxiliary"], ID="OB")
    D = m.intersect(c_om, ln_oc, between=(O, C), ID="D")
    F = m.intersect(c_om, ln_ob, between=(O, B), ID="F")

    ln_bd = m.construct_line(B, D, classes=["golden"], ID="BD")
    ln_cf = m.construct_line(C, F, classes=["golden"], ID="CF")
    _ = ln_cf
    m.intersect(ln_bd, ln_am, classes=["golden"], ID="E")

    return make_result(m, ("O", "E"), ("E", "M"), ("O", "E", "M"))


RIGHT_AND_345_SPECS: tuple[ConstructionSpec, ...] = (
    ConstructionSpec(
        slug="01-huntley-egyptian-345",
        catalog_code="GC-04.01",
        family_slug="04-right-and-345",
        order=1,
        title="H. E. Huntley's Golden Ratio in the 3-4-5 Right Triangle (1970)",
        short_title="Egyptian 3-4-5 Triangle",
        discoverers=("h-e-huntley", "tran-quang-hung"),
        year="1970",
        citations=("huntley-1970", "bogomolny-345", "bogomolny-345-tqh"),
        ctk_url="https://www.cut-the-knot.org/do_you_know/GoldenRatio345.shtml",
        ctk_title="Golden Ratio in the 3-4-5 Triangle",
        number_field=r"\mathbb{Q}(\phi)",
        number_field_text="Q(φ)",
        enunciation=(
            "In a :math:`3\\text{-}4\\text{-}5` right triangle :g:`ABC` (:math:`|BC|=3, |AC|=4, |AB|=5`), "
            "let the internal bisector of :math:`\\angle ABC` meet leg :g:`AC` at :g:`O`. Circle :g:`cOC` "
            "centered at :g:`O` through :g:`C` intersects line :g:`BO` at :g:`P` and :g:`Q` such that "
            ":math:`|PQ|/|BP| = |BQ|/|PQ| = \\phi`."
        ),
        given_prose=(
            "Right triangle :g:`ABC` with right angle at :g:`C` :math:`= (0,0)`, :g:`B` :math:`= (3,0)`, "
            "and :g:`A` :math:`= (0,4)`."
        ),
        steps_prose=(
            "Bisect :math:`\\angle ABC` to meet leg :g:`AC` at :g:`O` :math:`= (0, \\tfrac{3}{2})`.",
            "Draw circle :g:`cOC` of radius :math:`\\tfrac{3}{2}` centered at :g:`O` through :g:`C` (tangent to both :g:`BC` at :g:`C` and hypotenuse :g:`AB` at :g:`T`).",
            "Extend bisector :g:`BO` across :g:`cOC` to obtain secant intersections :g:`P` and :g:`Q`.",
        ),
        proof_prose=(
            "By the angle-bisector theorem, :math:`|CO|/|OA| = |BC|/|AB| = 3/5`, giving :math:`|CO| = 3/2` "
            "and diameter :math:`|PQ| = 3 = |BC|`. By Euclid III.36 (tangent-secant power from :g:`B` to "
            ":g:`cOC`), :math:`|BC|^2 = |BP| \\cdot |BQ| = |BP|(|BP| + |PQ|)`. Substituting :math:`|BC| = |PQ|` "
            "gives :math:`|PQ|^2 = |BP|^2 + |BP|\\cdot|PQ|`, whence :math:`|PQ|/|BP| = \\phi`."
        ),
        notes_prose=(
            "Featured in H. E. Huntley's *The Divine Proportion* (1970), this theorem links the oldest "
            "Pythagorean triple :math:`(3,4,5)` directly to extreme and mean ratio."
        ),
        terms=("golden-ratio", "golden-section", "power-of-a-point"),
        builder=build_huntley_egyptian_345,
    ),
    ConstructionSpec(
        slug="02-kepler-geometric-triangle",
        catalog_code="GC-04.02",
        family_slug="04-right-and-345",
        order=2,
        title="Johannes Kepler's Geometric-Progression Right Triangle (1597)",
        short_title="Kepler's Right Triangle",
        discoverers=("johannes-kepler",),
        year="1597",
        citations=("kepler-1597", "bogomolny-golden-ratio"),
        ctk_url="https://www.cut-the-knot.org/do_you_know/GoldenRatio.shtml",
        ctk_title="Golden Ratio in Geometry — Kepler's Triangle",
        number_field=r"\mathbb{Q}(\sqrt{\phi})",
        number_field_text="Q(√φ)",
        enunciation=(
            "Divide hypotenuse :g:`AB` at :g:`H` in the golden ratio (:math:`|AH|/|HB| = \\phi`), "
            "and erect perpendicular :g:`HC` to semicircle :g:`cOB` on diameter :g:`AB`. Right triangle "
            ":g:`ABC` has side lengths in geometric progression :math:`1 : \\sqrt{\\phi} : \\phi` and "
            "side quadrances in progression :math:`1 : \\phi : \\phi^2`."
        ),
        given_prose=(
            "Golden-sectioned hypotenuse :g:`A` :math:`= (0,0)`, :g:`H` :math:`= (\\phi, 0)`, "
            ":g:`B` :math:`= (\\phi^2, 0)` with midpoint :g:`O` :math:`= (\\tfrac{\\phi^2}{2}, 0)`."
        ),
        steps_prose=(
            "Draw circle :g:`cOB` on diameter :g:`AB` of length :math:`\\phi^2 = \\phi + 1`.",
            "Erect altitude :g:`HC` perpendicular to :g:`AB` at golden division point :g:`H` to meet :g:`cOB` at :g:`C` :math:`= (\\phi, \\sqrt{\\phi})`.",
            "Join :g:`AC` and :g:`BC` to complete right triangle :g:`ABC`.",
        ),
        proof_prose=(
            "By Euclid VI.8 and VI.13, altitude :g:`HC` is the geometric mean :math:`|HC|^2 = |AH|\\cdot|HB| = \\phi \\cdot 1 = \\phi`. "
            "Thus :math:`Q(B, C) = 1 + \\phi = \\phi^2`, :math:`Q(A, C) = \\phi^2 + \\phi = \\phi^3`, and "
            ":math:`Q(A, B) = \\phi^4`. Because :math:`\\phi^2 + \\phi^3 = \\phi^2(1 + \\phi) = \\phi^4`, "
            "Kepler's two 'treasures of geometry'—the Pythagorean theorem and the golden section—unite "
            "uniquely in :math:`\\triangle ABC`."
        ),
        notes_prose=(
            "Kepler's triangle is the canonical entry point in the catalog whose coordinates genuinely "
            "require the quadratic extension :math:`\\mathbb{Q}(\\sqrt{\\phi})` of degree :math:`4` over :math:`\\mathbb{Q}`."
        ),
        terms=("golden-ratio", "golden-section", "kepler-triangle", "quadrance"),
        builder=build_kepler_geometric_triangle,
    ),
    ConstructionSpec(
        slug="03-niemeyer-three-segments",
        catalog_code="GC-04.03",
        family_slug="04-right-and-345",
        order=3,
        title="Jo Niemeyer's Three Equal Leaning Segments",
        short_title="Niemeyer's Three Segments",
        discoverers=("jo-niemeyer",),
        year="2011",
        citations=("bogomolny-niemeyer", "bogomolny-golden-ratio"),
        ctk_url="https://www.cut-the-knot.org/do_you_know/GoldenJo.shtml",
        ctk_title="Golden Ratio in Three Equal Segments",
        number_field=r"\mathbb{Q}(\sqrt{3}, \phi)",
        number_field_text="Q(√3, φ)",
        enunciation=(
            "Place segment :g:`A1B1` perpendicular to line :g:`L` at :g:`A1`, lean equal segment "
            ":g:`B2A2` from midpoint :g:`B2` of :g:`A1B1` onto :g:`L`, and lean a third equal segment "
            ":g:`B3A3` from midpoint :g:`B3` of :g:`B2A2` onto :g:`L`. Then :g:`A2` divides :g:`A1A3` "
            "in the golden ratio: :math:`|A1A2|/|A2A3| = \\phi`."
        ),
        given_prose=(
            "Segment :g:`A1B1` of length :math:`2` from :g:`A1` :math:`= (0,0)` to :g:`B1` :math:`= (2,0)` "
            "perpendicular to vertical line :g:`L` (:math:`x = 0`)."
        ),
        steps_prose=(
            "Bisect :g:`A1B1` at :g:`B2` :math:`= (1,0)` and swing circle :g:`cB2` of radius :math:`2` to meet :g:`L` at :g:`A2` :math:`= (0, \\sqrt{3})`.",
            "Bisect :g:`B2A2` at :g:`B3` :math:`= (\\tfrac{1}{2}, \\tfrac{\\sqrt{3}}{2})`.",
            "Swing circle :g:`cB3` of radius :math:`2` centered at :g:`B3` to meet :g:`L` above :g:`A2` at :g:`A3`.",
        ),
        proof_prose=(
            "Right triangle :math:`\\triangle A1B2A2` has hypotenuse :math:`2` and leg :math:`1`, so "
            ":math:`|A1A2| = \\sqrt{3}` and :g:`B3` :math:`= (\\tfrac{1}{2}, \\tfrac{\\sqrt{3}}{2})`. "
            "Circle :g:`cB3` satisfies :math:`(x - \\tfrac{1}{2})^2 + (y - \\tfrac{\\sqrt{3}}{2})^2 = 4`; "
            "at :math:`x = 0`, :math:`(y - \\tfrac{\\sqrt{3}}{2})^2 = \\frac{15}{4}`, giving "
            ":math:`y_{A3} = \\frac{\\sqrt{3} + \\sqrt{15}}{2} = \\sqrt{3}\\,\\phi`. Hence "
            ":math:`|A1A2| = \\sqrt{3}` and :math:`|A2A3| = \\sqrt{3}(\\phi - 1) = \\sqrt{3}/\\phi`, "
            "proving :math:`|A1A2|/|A2A3| = \\phi`."
        ),
        notes_prose=(
            "Concrete artist Jo Niemeyer designed minimal sculptures and reliefs built from this "
            "three-bar linkage, realizing :math:`\\phi` mechanically with three identical rods."
        ),
        terms=("golden-ratio", "golden-section", "quadrance"),
        builder=build_niemeyer_three_segments,
    ),
    ConstructionSpec(
        slug="04-bui-van-obel-isosceles",
        catalog_code="GC-04.04",
        family_slug="04-right-and-345",
        order=4,
        title="Bùi Quang Tuân's Van Obel Division in a Right Isosceles Triangle",
        short_title="Van Obel Right Isosceles",
        discoverers=("bui-quang-tuan",),
        year="2014",
        citations=("bogomolny-bui-3", "bogomolny-golden-ratio"),
        ctk_url="https://www.cut-the-knot.org/do_you_know/BuiGoldenRatio3.shtml",
        ctk_title="Golden Ratio in Right Isosceles Triangle",
        number_field=r"\mathbb{Q}(\phi)",
        number_field_text="Q(φ)",
        enunciation=(
            "In right isosceles triangle :g:`ABC` with hypotenuse midpoint :g:`M` and midpoint :g:`O` "
            "of altitude :g:`AM`, circle :g:`cOM` cuts :g:`OC` and :g:`OB` at :g:`D` and :g:`F`. "
            "Cevians :g:`BD` and :g:`CF` concur on :g:`OM` at :g:`E`, dividing :g:`OM` in the golden "
            "ratio: :math:`|OE|/|EM| = \\phi`."
        ),
        given_prose=(
            "Right isosceles triangle :g:`ABC` with :g:`B` :math:`= (-2,0)`, :g:`C` :math:`= (2,0)`, "
            ":g:`A` :math:`= (0,2)`, midpoint :g:`M` :math:`= (0,0)`, and :g:`O` :math:`= (0,1)`."
        ),
        steps_prose=(
            "Draw circle :g:`cOM` centered at :g:`O` of radius :math:`1` (passing through :g:`A` and :g:`M`).",
            "Join :g:`OC` and :g:`OB` to meet :g:`cOM` internally at :g:`D` and :g:`F`.",
            "Draw cevians :g:`BD` and :g:`CF` meeting on symmetry axis :g:`AM` at :g:`E`.",
        ),
        proof_prose=(
            "In triangle :math:`\\triangle OBC`, :math:`|OB| = |OC| = \\sqrt{5}` and :math:`|OD| = |OF| = 1`, "
            "so :g:`D` divides :g:`OC` in ratio :math:`|OD|/|DC| = 1/(\\sqrt{5}-1) = \\phi/2`, and "
            "symmetrically :math:`|OF|/|FB| = \\phi/2`. By Van Obel's theorem on :math:`\\triangle OBC` "
            "with cevians :g:`OM`, :g:`BD`, :g:`CF` concurring at :g:`E`, "
            ":math:`|OE|/|EM| = |OD|/|DC| + |OF|/|FB| = \\phi/2 + \\phi/2 = \\phi`."
        ),
        notes_prose=(
            "Notice the elegance of the Van Obel proof: each symmetric side contributes half of "
            ":math:`\\phi`, summing immediately to :math:`\\phi` at the concurrence point :g:`E`."
        ),
        terms=("golden-ratio", "golden-section"),
        builder=build_bui_van_obel_isosceles,
    ),
)
