"""Scholarly apparatus registries for the Catalog of Golden Ratio Constructions.

Provides canonical biographical (:data:`PERSONS`), bibliographic
(:data:`CITATIONS`), and mathematical terminology (:data:`GLOSSARY`) entries
exported to ``resources/{persons,citations,glossary}.json`` and rendered into
``docsrc/constructions/{persons,bibliography,glossary}.rst``.
"""

from __future__ import annotations

from typing import Any

PERSONS: dict[str, dict[str, str]] = {
    "euclid": {
        "name": "Euclid of Alexandria",
        "dates": "fl. c. 300 BCE",
        "role": "Alexandrian Geometer; Author of the Elements",
        "bio": (
            "Formulated division in extreme and mean ratio in Elements Book II Proposition 11 "
            "and Book VI Proposition 30, applying it to construct the regular pentagon (IV.11) "
            "and the icosahedron and dodecahedron (Book XIII)."
        ),
    },
    "claudius-ptolemy": {
        "name": "Claudius Ptolemy",
        "dates": "c. 100 – c. 170 CE",
        "role": "Alexandrian Astronomer & Geometer",
        "bio": (
            "Introduced the streamlined circle-and-midpoint construction of the regular decagon "
            "and pentagon in Almagest Book I, Chapter 10 to compute his trigonometric table of chords."
        ),
    },
    "luca-pacioli": {
        "name": "Luca Pacioli",
        "dates": "c. 1447 – 1517",
        "role": "Franciscan Mathematician; Author of De Divina Proportione (1509)",
        "bio": (
            "Chronicled thirteen 'effects' of extreme and mean ratio in De Divina Proportione "
            "(1509, illustrated by Leonardo da Vinci), popularizing the Renaissance title "
            "Divina Proportione."
        ),
    },
    "johannes-kepler": {
        "name": "Johannes Kepler",
        "dates": "1571 – 1630",
        "role": "Astronomer & Geometer",
        "bio": (
            "Described the Pythagorean theorem and division in extreme and mean ratio as the "
            "'two great treasures of geometry' (1597 letter to Michael Mästlin) and studied the "
            "1 : √φ : φ right triangle and rhombic triacontahedron."
        ),
    },
    "william-hooper": {
        "name": "William Hooper",
        "dates": "fl. 1770 – 1794",
        "role": "Author of Rational Recreations",
        "bio": (
            "Published the earliest known geometric missing-area rectangle dissection fallacy in "
            "Rational Recreations (1774/1794), whose vanishing-gap limit is governed by φ."
        ),
    },
    "emile-lemoine": {
        "name": "Émile Michel Hyacinthe Lemoine",
        "dates": "1840 – 1912",
        "role": "French Geometer; Founder of Géométrographie",
        "bio": (
            "Founded Géométrographie (1902), a quantitative operational calculus measuring the "
            "simplicity and exactitude of ruler-and-compass constructions, and recorded early "
            "minimal divisions in extreme and mean ratio."
        ),
    },
    "paul-curry": {
        "name": "Paul Curry",
        "dates": "1917 – 1986",
        "role": "Magician & Recreational Geometer",
        "bio": (
            "Invented the Curry Paradox (1953) of area-discrepant triangle and rectangle "
            "rearrangements driven by Fibonacci slopes approaching 1/φ."
        ),
    },
    "h-e-huntley": {
        "name": "H. E. Huntley",
        "dates": "1892 – 1978",
        "role": "Physicist & Mathematical Expositor",
        "bio": (
            "Author of The Divine Proportion: A Study in Mathematical Beauty (Dover, 1970), "
            "highlighting unexpected appearances of φ such as the angle-bisector circle in the "
            "3-4-5 right triangle."
        ),
    },
    "h-s-m-coxeter": {
        "name": "H. S. M. Coxeter",
        "dates": "1907 – 2003",
        "role": "Geometer; University of Toronto",
        "bio": (
            "Communicated George Odom's equilateral midline golden-section problem in the "
            "American Mathematical Monthly (Problem E3007, 1983) and championed classical "
            "synthetic and projective geometry."
        ),
    },
    "george-odom": {
        "name": "George Odom",
        "dates": "1941 – 2010",
        "role": "Artist & Amateur Geometer",
        "bio": (
            "Discovered the celebrated two-line equilateral-triangle midline construction of φ "
            "(1982–1983) through visual exploration of polyhedra and three-dimensional models."
        ),
    },
    "alexander-bogomolny": {
        "name": "Alexander Bogomolny",
        "dates": "1948 – 2018",
        "role": "Mathematician, Educator & Creator of Cut-the-Knot",
        "bio": (
            "Founded Interactive Mathematics Miscellany and Puzzles (Cut-the-Knot, 1996–2018), "
            "curating, proving, and illustrating dozens of classical and contemporary Golden Ratio "
            "constructions contributed by geometers worldwide."
        ),
    },
    "ron-knott": {
        "name": "Ron Knott",
        "dates": "b. c. 1950",
        "role": "Mathematician & Educator; University of Surrey",
        "bio": (
            "Creator of the encyclopedic Fibonacci Numbers and the Golden Section resource "
            "(cataloged in sibling repository geometor/knott)."
        ),
    },
    "v-v-prasolov": {
        "name": "Viktor Vasil'evich Prasolov",
        "dates": "b. 1956",
        "role": "Russian Geometer & Author; Independent University of Moscow",
        "bio": (
            "Author of Problems in Plane and Solid Geometry, documenting affine equi-area "
            "characterizations of golden diagonal ratios in general convex pentagons."
        ),
    },
    "alexandre-borovik": {
        "name": "Alexandre Borovik",
        "dates": "b. 1956",
        "role": "Mathematician; University of Manchester",
        "bio": (
            "Observed the golden rectangle embedded inside Bùi Quang Tuân's concentric Greek "
            "cross and square configuration on Cut-the-Knot."
        ),
    },
    "jerzy-kocik": {
        "name": "Jerzy Kocik",
        "dates": "fl. 1990 – present",
        "role": "Mathematician & Physicist; Southern Illinois University",
        "bio": (
            "Discovered and analyzed the Apollonian 'Golden Window' circle packing (Mathematics "
            "Magazine, 2010), showing how simultaneous tangency forces powers of φ."
        ),
    },
    "jingcheng-tong": {
        "name": "Jingcheng Tong",
        "dates": "fl. 1985 – 2015",
        "role": "Mathematician; University of North Florida",
        "bio": (
            "Characterized area-bisecting chords in trapezoids whose parallel bases stand in "
            "ratio 1 : 3, dividing both legs in the golden ratio."
        ),
    },
    "jo-niemeyer": {
        "name": "Jo Niemeyer",
        "dates": "b. 1946",
        "role": "German Concrete Artist & Designer",
        "bio": (
            "Constructivist artist whose sculptures and geometric studies feature the golden "
            "division generated by three equal leaning segments."
        ),
    },
    "kurt-hofstetter": {
        "name": "Kurt Hofstetter",
        "dates": "b. 1959",
        "role": "Austrian Artist & Geometer",
        "bio": (
            "Published a remarkable series of minimal 5-step Euclidean, 5-circle Mascheroni "
            "compass-only, and fixed-opening rusty-compass Golden Ratio constructions in "
            "Forum Geometricorum (2002–2005)."
        ),
    },
    "michel-bataille": {
        "name": "Michel Bataille",
        "dates": "fl. 2000 – present",
        "role": "French Geometer & Problemist; Rouen",
        "bio": (
            "Prolific contributor to Crux Mathematicorum and Forum Geometricorum; devised the "
            "equilateral-triangle-and-square radical-axis construction of φ (2011)."
        ),
    },
    "bui-quang-tuan": {
        "name": "Bùi Quang Tuân",
        "dates": "fl. 2010 – present",
        "role": "Vietnamese Geometer",
        "bio": (
            "Discovered numerous synthetic Golden Ratio theorems curated on Cut-the-Knot, "
            "including a 5-step collinear circle construction, the Greek Cross & Square, "
            "Four Golden Circles, Van Obel isosceles division, and infinite circle-secant families."
        ),
    },
    "tran-quang-hung": {
        "name": "Tran Quang Hung",
        "dates": "fl. 2012 – present",
        "role": "Vietnamese Geometer; Hanoi University of Science High School",
        "bio": (
            "Contributed an extraordinary suite of synthetic Golden Ratio discoveries across "
            "equilateral triangles, squares, 3×3 grids, hexagons, pentagon stars, Wu Xing "
            "rotations, rhombi, trapezoids, and mixtilinear circles."
        ),
    },
    "dao-thanh-oai": {
        "name": "Dao Thanh Oai",
        "dates": "fl. 2013 – present",
        "role": "Vietnamese Geometer",
        "bio": (
            "Known for discoveries in Euclidean and projective triangle/polygon geometry, "
            "including the regular-pentagon edge-perpendicular division in φ."
        ),
    },
    "nguyen-thanh-dung": {
        "name": "Nguyen Thanh Dung",
        "dates": "fl. 2015 – present",
        "role": "Vietnamese Geometer",
        "bio": (
            "Contributed butterfly-chord equilateral constructions and 2×2 square lattice "
            "divisions in extreme and mean ratio on Cut-the-Knot."
        ),
    },
    "quang-duong": {
        "name": "Quang Duong",
        "dates": "fl. 2015",
        "role": "Geometer & Problem Solver",
        "bio": (
            "Contributed synthetic proofs for Tran Quang Hung's reflected equilateral and "
            "incircle Golden Ratio theorems."
        ),
    },
    "gregoire-nicollier": {
        "name": "Grégoire Nicollier",
        "dates": "fl. 2010 – present",
        "role": "Swiss Mathematician; University of Applied Sciences of Western Switzerland",
        "bio": (
            "Contributed analytic and synthetic proofs of polygonal and equilateral Golden Ratio "
            "configurations on Cut-the-Knot."
        ),
    },
    "leo-giugiuc": {
        "name": "Leonard Giugiuc",
        "dates": "fl. 2010 – present",
        "role": "Romanian Mathematician & Problemist",
        "bio": (
            "Co-solved and generalized several trigonometric, mixtilinear, and butterfly Golden "
            "Ratio problems curated by Alexander Bogomolny."
        ),
    },
    "ercole-suppa": {
        "name": "Ercole Suppa",
        "dates": "fl. 2005 – present",
        "role": "Italian Geometer; Teramo",
        "bio": (
            "Researcher in triangle centers and sangaku-style circle configurations; discovered "
            "the golden ratio of inradii in a midpoint-partitioned square (2015)."
        ),
    },
    "elliot-mcgucken": {
        "name": "Elliot McGucken",
        "dates": "fl. 2015 – present",
        "role": "Physicist & Recreational Geometer",
        "bio": (
            "Contributed golden-section constructions in two and three tangent equal circles "
            "and 3×3 square grids on Cut-the-Knot."
        ),
    },
    "thanos-kalogerakis": {
        "name": "Thanos Kalogerakis",
        "dates": "fl. 2016",
        "role": "Greek Geometer",
        "bio": (
            "Observed the diameter-to-secant golden ratio across two externally tangent equal "
            "circles."
        ),
    },
    "john-arioni": {
        "name": "John Arioni",
        "dates": "fl. 2016",
        "role": "Geometer",
        "bio": (
            "Contributed the Yin-Yang twin-circle secant construction and the 30°-rotated unit "
            "square diagonal-circle construction of φ on Cut-the-Knot."
        ),
    },
    "john-molokach": {
        "name": "John Molokach",
        "dates": "fl. 2013 – present",
        "role": "Recreational Geometer",
        "bio": (
            "Devised the construction of a golden rhombus and consecutive powers of φ from two "
            "unit-shifted 1×3 rectangles and an inscribed unit circle."
        ),
    },
}


def _ctk(slug_path: str, page_title: str, note: str = "") -> dict[str, str]:
    url = (
        slug_path
        if slug_path.startswith("http")
        else f"https://www.cut-the-knot.org/do_you_know/{slug_path}"
    )
    return {
        "author": "Alexander Bogomolny",
        "work": f"Cut-the-Knot: {page_title}",
        "locus": "© 1996–2018",
        "year": "1996–2018",
        "url": url,
        "note": note
        or "Interactive Mathematics Miscellany and Puzzles (cut-the-knot.org), © 1996–2018 Alexander Bogomolny.",
    }


CITATIONS: dict[str, dict[str, str]] = {
    # Classical & journal primary sources
    "euclid-elements": {
        "author": "Euclid",
        "work": "Elements (Heath Edition)",
        "locus": "Book II Prop. 11; Book IV Prop. 10–11; Book VI Def. 3 & Prop. 30; Book XIII Prop. 1–10",
        "year": "c. 300 BCE",
        "url": "https://geometor.github.io/euclid/",
        "note": "Sir Thomas L. Heath, The Thirteen Books of Euclid's Elements, Cambridge University Press, 1908 (GEOMETOR Digital Scriptorium edition).",
    },
    "ptolemy-almagest": {
        "author": "Claudius Ptolemy",
        "work": "Syntaxis Mathematica (Almagest)",
        "locus": "Book I, Chapter 10",
        "year": "c. 150 CE",
        "url": "",
        "note": "G. J. Toomer (trans.), Ptolemy's Almagest, Duckworth / Springer, 1984.",
    },
    "kepler-1597": {
        "author": "Johannes Kepler",
        "work": "Letter to Michael Mästlin (Tübingen, October 1597)",
        "locus": "Gesammelte Werke, Vol. 13, Nr. 75",
        "year": "1597",
        "url": "",
        "note": "First explicit derivation of the right triangle with sides in geometric progression 1 : √φ : φ.",
    },
    "hooper-1794": {
        "author": "William Hooper",
        "work": "Rational Recreations",
        "locus": "4th ed., Vol. 1, Problem XLIII",
        "year": "1794",
        "url": "",
        "note": "Early geometric missing-area rectangle dissection later generalized by Sam Loyd, Martin Gardner, and Paul Curry.",
    },
    "lemoine-1902": {
        "author": "Émile Lemoine",
        "work": "Géométrographie ou Art des constructions géométriques",
        "locus": "Scientia No. 18, C. Naud, Paris",
        "year": "1902",
        "url": "",
        "note": "Foundational treatise quantifying operational simplicity of straightedge-and-compass constructions; see also J. Reusch, Planimetrische Konstruktionen in geometrographischer Ausführung (1904).",
    },
    "huntley-1970": {
        "author": "H. E. Huntley",
        "work": "The Divine Proportion: A Study in Mathematical Beauty",
        "locus": "Dover Publications, New York",
        "year": "1970",
        "url": "",
        "note": "Classic exposition including the angle-bisector circle division in the 3-4-5 right triangle.",
    },
    "odom-coxeter-1983": {
        "author": "George Odom & H. S. M. Coxeter",
        "work": "Elementary Problem E3007",
        "locus": "American Mathematical Monthly 90(7), p. 482 (solution 93(7), 1986, p. 566)",
        "year": "1983",
        "url": "",
        "note": "Equilateral-triangle midline extended to the circumcircle yields the golden section.",
    },
    "hofstetter-2002": {
        "author": "Kurt Hofstetter",
        "work": "A Simple Construction of the Golden Section",
        "locus": "Forum Geometricorum 2, pp. 65–66",
        "year": "2002",
        "url": "",
        "note": "Five-circle Mascheroni compass-only construction of the golden section.",
    },
    "hofstetter-2003": {
        "author": "Kurt Hofstetter",
        "work": "5-Step Division of a Segment in the Golden Section",
        "locus": "Forum Geometricorum 3, pp. 205–206",
        "year": "2003",
        "url": "",
        "note": "Minimal 5-step straightedge-and-compass internal division of a given segment.",
    },
    "hofstetter-2004": {
        "author": "Kurt Hofstetter",
        "work": "Another 5-Step Division of a Segment in the Golden Section",
        "locus": "Forum Geometricorum 4, pp. 21–22",
        "year": "2004",
        "url": "",
        "note": "Alternative 5-step straightedge-and-compass division using three circles and two lines.",
    },
    "hofstetter-2005": {
        "author": "Kurt Hofstetter",
        "work": "Division of a Segment in the Golden Section with Ruler and Rusty Compass",
        "locus": "Forum Geometricorum 5, pp. 135–136",
        "year": "2005",
        "url": "",
        "note": "Fixed-opening (rusty) compass construction dividing a unit segment in φ.",
    },
    "prasolov-2006": {
        "author": "V. V. Prasolov",
        "work": "Problems in Plane Geometry",
        "locus": "MCCME, Moscow (5th ed.)",
        "year": "2006",
        "url": "",
        "note": "Affine equi-area characterization of golden diagonal ratios in irregular convex pentagons.",
    },
    "kocik-2010": {
        "author": "Jerzy Kocik",
        "work": "Golden Window",
        "locus": "Mathematics Magazine 83(5), pp. 384–390",
        "year": "2010",
        "url": "",
        "note": "Six-circle Apollonian window packing forcing powers of φ, golden rectangles, and Kepler's triangle.",
    },
    "bataille-2011": {
        "author": "Michel Bataille",
        "work": "Another Simple Construction of the Golden Section",
        "locus": "Forum Geometricorum 11, pp. 55–56",
        "year": "2011",
        "url": "",
        "note": "Constructs φ from an equilateral triangle and square erected on the same segment.",
    },
    "knott-golden-section": {
        "author": "Ron Knott",
        "work": "Fibonacci Numbers and the Golden Section",
        "locus": "University of Surrey Mathematical Archive",
        "year": "1996–2024",
        "url": "https://r-knott.surrey.ac.uk/Fibonacci/",
        "note": "Companion archive cataloged in sibling GEOMETOR repository geometor/knott.",
    },
    # Alexander Bogomolny — Cut-the-Knot curated pages (© 1996–2018)
    "bogomolny-golden-ratio": _ctk("GoldenRatio.shtml", "Golden Ratio in Geometry"),
    "ctk-compass-only": _ctk("GoldenRatioByCompass.shtml", "Golden Ratio by Compass Only"),
    "ctk-rusty-compass": _ctk("GoldenRatioByRustyCompass.shtml", "Golden Ratio with a Rusty Compass"),
    "ctk-hofstetter3": _ctk("Hofstetter3.shtml", "Kurt Hofstetter's 5-Step Construction of the Golden Section"),
    "ctk-bui-5step": _ctk("BuiGoldenRatio5Step.shtml", "Bùi Quang Tuân's 5-Step Construction of the Golden Ratio"),
    "ctk-bataille": _ctk("MBatailleGoldenRatio.shtml", "From Equilateral Triangle and Square to Golden Ratio"),
    "ctk-bui-qtb": _ctk("GoldenQTB.shtml", "Golden Section in Two Equilateral Triangles"),
    "ctk-bui-qtb2": _ctk("GoldenQTBAnother.shtml", "Golden Section in Two Equilateral Triangles, II"),
    "ctk-buratino2": _ctk("Buratino2.shtml", "Golden Ratio in Reflected Equilateral Triangles"),
    "ctk-buratino3": _ctk("Buratino3.shtml", "Golden Ratio in Regular Hexagon and Square"),
    "ctk-buratino5": _ctk("TranQuangHung2015.shtml", "Golden Ratio in Equilateral Triangle and Incircle"),
    "ctk-butterfly-equilateral": _ctk(
        "GoldenRatioAstrideEquilateralTriangle.shtml",
        "Golden Ratio Astride Equilateral Triangle",
    ),
    "bogomolny-rectangles": _ctk("GoldenRatioInRectangles.shtml", "Golden Ratio in Square and Circle"),
    "bogomolny-buratino1": _ctk("Buratino1.shtml", "Golden Ratio in Square"),
    "bogomolny-2x2": _ctk("2x2GoldenRatio.shtml", "Golden Ratio in 2×2 Square"),
    "bogomolny-3x3-1": _ctk("3x3GoldenRatio.shtml", "Golden Ratio in 3×3 Square"),
    "bogomolny-3x3-2": _ctk("3x3GoldenRatio2.shtml", "Another Golden Ratio in 3×3 Square"),
    "bogomolny-suppa-square": _ctk("GoldenRatioInSquare.shtml", "Golden Ratio via Two Incircles in a Square"),
    "bogomolny-golden-cross": _ctk("GoldenCross.shtml", "Golden Cross and Golden Square"),
    "bogomolny-arioni-square": _ctk("JohnArioni.shtml", "Golden Ratio by Rotating a Square"),
    "bogomolny-345": _ctk("GoldenRatio345.shtml", "Golden Ratio and the Egyptian 3-4-5 Triangle"),
    "bogomolny-345-tqh": _ctk("3-4-5-GoldenRatio.shtml", "Another Golden Ratio in the 3-4-5 Triangle"),
    "bogomolny-niemeyer": _ctk("GoldenJo.shtml", "Golden Ratio and Midpoints (Jo Niemeyer)"),
    "bogomolny-bui-3": _ctk("BuiGoldenRatio3.shtml", "Golden Ratio in Right Isosceles Triangle"),
    "bogomolny-pentagon": _ctk(
        "https://www.cut-the-knot.org/pythagoras/pentagon.shtml",
        "Regular Pentagon and Golden Ratio",
    ),
    "bogomolny-pentagon-dao": _ctk("GoldenRatioInRegularPentagon.shtml", "Golden Ratio in Regular Pentagon"),
    "bogomolny-pentagon-tqh": _ctk(
        "AnotherGoldenRatioInRegularPentagon.shtml",
        "Another Golden Ratio in Regular Pentagon",
    ),
    "bogomolny-irregular-pentagon": _ctk("NoRegularPentagon.shtml", "Golden Ratio in an Irregular Pentagon"),
    "bogomolny-5-6": _ctk("5-6-GoldenRatioIn.shtml", "Golden Ratio in Pentagon and Hexagon"),
    "bogomolny-six-pentagons": _ctk("StarSixPentagonsGoldenRatio.shtml", "Star, Six Pentagons and Golden Ratio"),
    "bogomolny-wu-xing": _ctk("GoldenRatioInWuXing.shtml", "Golden Ratio in Wu Xing"),
    "bogomolny-bui-general": _ctk("BuiGoldenRatioGeneral.shtml", "Golden Ratio in Circle — in Droves"),
    "bogomolny-bui-1": _ctk("BuiGoldenRatio.shtml", "Golden Ratio in Circle"),
    "bogomolny-mcgucken-1": _ctk("ElliotMcGucken1.shtml", "Golden Ratio in Two Equal Circles"),
    "bogomolny-kalogerakis": _ctk("GoldenRatioInCircles.shtml", "Golden Ratio in Two Tangent Circles"),
    "bogomolny-four-circles": _ctk("FourGoldenCircles.shtml", "Four Golden Circles"),
    "bogomolny-3-tangent": _ctk("3TangentCirclesGoldenRatio.shtml", "Golden Ratio in Three Tangent Circles"),
    "bogomolny-golden-window": _ctk("GoldenWindow.shtml", "Golden Window"),
    "bogomolny-yin-yang": _ctk("GoldenRatioInYinYang.shtml", "Golden Ratio in Yin-Yang"),
    "bogomolny-buratino8": _ctk("Buratino8.shtml", "Golden Ratio in Rhombus"),
    "bogomolny-molokach": _ctk("GoldenRatioMolokach.shtml", "Golden Ratio via Golden Rhombus"),
    "bogomolny-tqh-trapezoid": _ctk("TQHGoldenRatio.shtml", "Golden Ratio in Isosceles Trapezoid"),
    "bogomolny-mixtilinear": _ctk("GoldenMixtilinear.shtml", "Golden Ratio in Mixtilinear Circles"),
}

GLOSSARY: dict[str, dict[str, Any]] = {
    "golden-ratio": {
        "headword": "Golden Ratio (φ)",
        "translation": "Sectio Aurea / Divina Proportione",
        "definition": (
            "The positive root φ = (1 + √5)/2 ≈ 1.6180339887 of x² − x − 1 = 0, satisfying "
            "φ² = φ + 1 and 1/φ = φ − 1."
        ),
    },
    "golden-section": {
        "headword": "Golden Section",
        "translation": "Collinear Division in φ",
        "definition": (
            "A collinear point triple (A, G, B) whose consecutive segments stand in the golden "
            "ratio |AG|/|GB| = φ (so |AB|/|AG| = φ as well)."
        ),
    },
    "extreme-and-mean-ratio": {
        "headword": "Extreme and Mean Ratio",
        "translation": "ἄκρος καὶ μέσος λόγος (Euclid VI.Def.3)",
        "definition": (
            "Euclid's classical definition: a straight line is cut in extreme and mean ratio "
            "when, as the whole line is to the greater segment, so is the greater to the less."
        ),
    },
    "golden-chain": {
        "headword": "Golden Chain",
        "translation": "Connected Collinear φ-Progression",
        "definition": (
            "A sequence of four or more collinear points in which overlapping triples form "
            "consecutive golden sections (such as lengths 1/φ, 1, 1/φ or 1, φ, φ²)."
        ),
    },
    "quadrance": {
        "headword": "Quadrance",
        "translation": "Q(A, B) = (x₂ − x₁)² + (y₂ − y₁)²",
        "definition": (
            "Norman Wildberger's Rational Trigonometry invariant measuring squared separation "
            "without square roots; two segments stand in ratio φ iff Q_long / Q_short = φ + 1 = φ²."
        ),
    },
    "geometrographie": {
        "headword": "Géométrographie",
        "translation": "Lemoine Construction Complexity",
        "definition": (
            "Émile Lemoine's 1902 operational metric counting elementary straightedge (R₁, R₂) "
            "and compass (C₁, C₂, C₃) operations; drawing a line through two points or a circle "
            "centered at one point through another each contributes simplicity 3."
        ),
    },
    "vesica-piscis": {
        "headword": "Vesica Piscis",
        "translation": "Twin-Circle Lens (Euclid I.1)",
        "definition": (
            "The symmetric lens formed by two congruent circles each passing through the other's "
            "center, generating √3 altitudes and bisecting their common radius."
        ),
    },
    "mascheroni-construction": {
        "headword": "Mascheroni Construction",
        "translation": "Compass-Only Construction",
        "definition": (
            "A geometric construction using circles alone (0 straightedge lines), proved "
            "universal for all Euclidean constructible points by Georg Mohr (1672) and Lorenzo "
            "Mascheroni (1797)."
        ),
    },
    "rusty-compass": {
        "headword": "Rusty Compass",
        "translation": "Fixed-Aperture Compass",
        "definition": (
            "A compass locked to a single invariant radius throughout a construction, studied by "
            "Abu'l-Wafa, Leonardo da Vinci, Poncelet, and Steiner."
        ),
    },
    "power-of-a-point": {
        "headword": "Power of a Point",
        "translation": "Euclid III.35–37 / Radical Invariant",
        "definition": (
            "For a point P and circle O(r), the invariant quantity |PO|² − r², equal to the "
            "signed product |PA|·|PB| along any secant PAB (and to |PT|² along a tangent PT)."
        ),
    },
    "intersecting-chords-theorem": {
        "headword": "Intersecting Chords Theorem",
        "translation": "Euclid Elements III.35",
        "definition": (
            "If two chords AB and CD of a circle intersect internally at M, then "
            "|AM|·|MB| = |CM|·|MD|."
        ),
    },
    "butterfly-theorem": {
        "headword": "Butterfly Configuration",
        "translation": "Crossed Cyclic Chords across a Midpoint Chord",
        "definition": (
            "Cyclic quadrilateral diagonals crossing a reference chord symmetrically, inducing "
            "projective cross-ratio and golden-section divisions."
        ),
    },
    "kepler-triangle": {
        "headword": "Kepler Triangle",
        "translation": "1 : √φ : φ Right Triangle",
        "definition": (
            "The unique right triangle whose side lengths (and side quadrances 1 : φ : φ²) form "
            "a geometric progression."
        ),
    },
    "mixtilinear-incircle": {
        "headword": "Mixtilinear Incircle",
        "translation": "Two-Side & Circumcircle Tangent Circle",
        "definition": (
            "A circle internally tangent to two sides of a triangle and internally tangent to "
            "its circumcircle."
        ),
    },
    "golden-rhombus": {
        "headword": "Golden Rhombus",
        "translation": "Diagonal Ratio |d₁|/|d₂| = φ",
        "definition": (
            "A rhombus whose long and short diagonals stand in the golden ratio φ; thirty "
            "congruent golden rhombi bound Kepler's rhombic triacontahedron."
        ),
    },
    "golden-rectangle": {
        "headword": "Golden Rectangle",
        "translation": "Side Ratio φ : 1",
        "definition": (
            "A rectangle whose length-to-width ratio equals φ, characterized self-similarly by "
            "leaving a congruent-proportioned golden rectangle when a square gnomon is removed."
        ),
    },
}
