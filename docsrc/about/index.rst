:navigation: header
:order: 10
:nav_title: About

.. _about:
.. _about-index:
.. _about-divine:

About
=====

.. rubric:: Extracting Historical Semantic Knowledge & Repurposing It for Exact Symbolic Reasoning

About This Edition
------------------

``geometor.divine`` is the Golden Ratio analysis engine and computable **Catalog of Golden Ratio Constructions** within the GEOMETOR ecosystem. The edition formalizes, verifies, and analyzes the appearance of the golden ratio (:math:`\phi = \frac{1 + \sqrt{5}}{2}`) and harmonic ranges across historical treatises and modern mathematical geometry. By pairing automated proportional discovery with machine-certified symbolic demonstrations, it illuminates how extreme and mean ratio relationships emerge naturally from foundational ruler-and-compass configurations.

The repository catalogs **45 exact symbolic constructions across seven geometric families**—triangles, equilateral hexagons, squares and rectangles, pentagons, decagons, circles, and rhombi, trapezoids, and algebraic systems. Historical sources spanning Euclid's *Elements* (notably Book II.11, Book IV.10–11, and Book XIII), Claudius Ptolemy's *Almagest*, Johannes Kepler, and Émile Lemoine converge with peer-reviewed 20th- and 21st-century geometry papers (*Forum Geometricorum*, *American Mathematical Monthly*, *Mathematics Magazine*) and Alexander Bogomolny's *Cut-the-Knot* archive. Implicit geometric relationships—collinear point divisions, golden chains, and harmonic conjugates—are systematically extracted into machine-addressable semantic structures and rendered through calibrated Ink-to-Vector ``.euclid-graphic`` SVGs.

Within the GEOMETOR Digital Scriptorium, ``geometor.divine`` acts as an analytical bridge connecting classical axiomatic canons to modern symbolic computation. It connects directly with the foundational constructions of ``geometor.elements`` and ``geometor.euclid``, Renaissance investigations in Luca Pacioli's ``geometor.pacioli`` (*De Divina Proportione*, 1509) and Albrecht Dürer's ``geometor.durer`` (*Underweysung der Messung*, 1525), and utilizes the exact algebraic modeling engine ``geometor.model`` to guarantee that all geometric invariants and segment proportions are certified with zero floating-point error.

The GEOMETOR Mission
--------------------

Founded by **phi ARCHITECT**, the GEOMETOR project is dedicated to three foundational pillars:

Extracting Historical Semantic Knowledge
    Moving beyond passive page scans and OCR to recover the living deductive structure of 2,300+ years of geometric, axiomatic, and philosophical treatises. GEOMETOR elevates prose, marginal citations, primary-source folios (via ``publish folio``), and calibrated Ink-to-Vector ``.euclid-graphic`` diagrams into structured, machine-addressable semantic graphs.

Exact Symbolic Grounding (``geometor.model``)
    Anchoring geometric constructions in 100% exact symbolic algebra (`SymPy <https://www.sympy.org>`_) and Rational Trigonometry invariants (quadrance, spread, cross-ratio) over exact algebraic number fields rather than floating-point approximations. Every point coordinate, intersection, and proportional division is mathematically certified and permanently reproducible.

Repurposing Knowledge Across Mediums
    Re-deploying extracted semantic and algebraic structures across synchronized multi-track **Book Codices** and EPUB 3 editions (``photon-platform/publish``), computable deductive canons (``geometor.elements``, ``geometor.etc``, ``geometor.pappus``, ``geometor.divine``), interactive SVG laboratories (``geometor.explorer``), QHD visual broadcasts, and neuro-symbolic program synthesis (``geometor.seer``) across `geometor.com <https://geometor.com>`_.

Sources, Provenance & Methodology
---------------------------------

The catalog and analytical algorithms in ``geometor.divine`` draw from archival literature and classical geometric treatises:

- **Euclid of Alexandria**: *The Thirteen Books of Euclid's Elements*, translated with introduction and commentary by Sir Thomas L. Heath (Cambridge University Press, 1908; Dover Publications reprint).
- **Johannes Kepler**: *Harmonices Mundi* (1619) and *Mysterium Cosmographicum* (1596), exploring nested regular polyhedra and extreme and mean ratio divisions.
- **Alexander Bogomolny**: *Cut-the-Knot* Mathematics Archives (`GoldenRatio.shtml <https://www.cut-the-knot.org/do_you_know/GoldenRatio.shtml>`_, © 1996–2018), preserving dozens of classical and contemporary golden ratio demonstrations.
- **Modern Mathematical Journals**: Research contributions from *Forum Geometricorum*, *The American Mathematical Monthly*, and *Mathematics Magazine*, cataloged with full bibliographic attribution in the :doc:`Bibliography </constructions/bibliography>`.
- **Digital Scriptorium Methodology**: Every construction is implemented as a standalone, reproducible SymPy builder within ``geometor.divine.catalog``, paired with high-resolution vector graphics and interactive step-by-step visualizations compiled through the Photon Publisher framework.
