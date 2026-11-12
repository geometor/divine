GEOMETOR • divine
=================

.. image:: https://img.shields.io/pypi/v/geometor-divine.svg
   :target: https://pypi.python.org/pypi/geometor-divine
.. image:: https://img.shields.io/github/license/geometor/divine.svg
   :target: https://github.com/geometor/divine/blob/main/LICENSE

**Exact symbolic discovery engine for golden sections, golden chains, and the Catalog of Golden Ratio Constructions.**

Overview
--------

``geometor.divine`` observes exact symbolic `geometor.model <https://github.com/geometor/model>`_ constructions to discover instances of the **Divine Proportion** ($\phi = \frac{1 + \sqrt{5}}{2}$), connected golden chains, and proportional symmetries using Rational Trigonometry quadrances over $\mathbb{Q}(\sqrt{5})$ and radical extensions.

Alongside the automated discovery engine, ``geometor.divine.catalog`` provides a comprehensive **Catalog of Golden Ratio Constructions** — **45 100% exact symbolic constructions** organized across **7 geometric families**, cataloging universal geometric facts curated by **Alexander Bogomolny** on `Cut-the-Knot <https://www.cut-the-knot.org/do_you_know/GoldenRatio.shtml>`_ (`© 1996–2018`) together with classical treatises and peer-reviewed geometry journals (*Forum Geometricorum*, *Crux Mathematicorum*, *Mathematical Reflections*, *American Mathematical Monthly*). It complements the sibling `geometor/knott <https://github.com/geometor/knott>`_ Ron Knott Golden Ratio Catalog.

Key Features
------------

- **Exact Golden Section & Chain Scanner** (``geometor.divine.golden``): Combines sub-millisecond coordinate screening with 100% exact Rational Trigonometry ``quadrance`` and ``zero_test`` verification ($Q_{\text{long}} = (\phi + 1)\,Q_{\text{short}}$) and connected golden-chain graph assembly.
- **Catalog of 45 Golden Ratio Constructions** (``geometor.divine.catalog``):

  1. *Minimal & Compass-Only Constructions* (7 entries — Euclid II.11, VI.30, Hofstetter 5-step & 4-step compass-only, Bui Quang Tuan)
  2. *Equilateral Triangle & Hexagon Constructions* (7 entries — George Odom, Tran Quang Hung, Bataille, Reuschle)
  3. *Squares, Rectangles & Crosses* (8 entries — Golden Rectangle, Semicircle-in-Square, Greek Cross & Inscribed Square, Nested Squares)
  4. *Right Triangles & 3-4-5 Constructions* (4 entries — Kepler Triangle, 3-4-5 Incircle Bisector, Three Equal Segments)
  5. *Regular Pentagons, Star Polygons & Higher Polygons* (6 entries — Ptolemy's Pentagon, Pentagram, Wu Xing, Six-Pentagon Star Wreath, Golden Gnomon)
  6. *Circles, Arbelos & Sangaku Packings* (7 entries — Mixtilinear Twin Circles, Tangent Four-Circle Chain, Kocik's Golden Window, Radical Axis)
  7. *Rhombi, Trapezoids, Algebraic Curiosities & Fallacies* (6 entries — Golden Rhombus, Trapezoid Harmonic Diagonals, Folded Triangle, Hooper–Curry $64 = 65$ Paradox)

- **Interactive Book Codex & ``.euclid-graphic`` SVGs**: Theme-adaptive vector diagrams with synchronized ``:g:`` hover highlights, Lemoine Geometrographie metrics, and companion ``Overview`` / ``Code`` reading panes compiled via ``photon-platform/publish``.

Usage
-----

.. code-block:: python

   from geometor.divine import CATALOG, build_construction
   from geometor.divine.golden import find_golden_sections_in_model, find_chains_in_model

   # Build and certify any construction by catalog code or slug
   model, cert = build_construction("GC-02.01")  # George Odom's Equilateral Construction
   print(cert.ratio_expr)                        # GoldenRatio
   print(len(cert.detected_sections), len(cert.detected_chains))

   # Scan any exact geometor.model.Model for golden sections and chains
   sections, chains = find_chains_in_model(model)

Resources & Attribution
-----------------------

Mathematical theorems and geometric constructions are universal facts; ``geometor.divine`` authors 100% original prose, exact ``geometor.model`` symbolic DAGs, Rational Trigonometry proofs, and ``.euclid-graphic`` vector diagrams while attributing every cataloged construction to its original geometer and primary source, with grateful scholarly credit to **Alexander Bogomolny** (`Cut-the-Knot <https://www.cut-the-knot.org/do_you_know/GoldenRatio.shtml>`_, ``© 1996–2018``).

- **Source Code**: https://github.com/geometor/divine
- **Issues**: https://github.com/geometor/divine/issues
