:type: construction
:order: 3
:excerpt: On a 2 times 2 square grid P1P2P3P4 with horizontal midline AB, center O, and top midpoint D, extend AB by one grid unit to C. Circle cCD centered at C through D cuts AB at M in the golden ratio: MB/AM = AB/MB = φ.
:categories: 03-squares-rectangles
:tags: field-q-phi, nguyen-thanh-dung

GC-03.03 · Nguyen Thanh Dung's 2×2 Grid Compass Arc
===================================================

**Discoverer(s)**: :person:`Nguyen Thanh Dung <nguyen-thanh-dung>` | **Date**: 2016 | **Field**: :math:`\mathbb{Q}(\phi)` | **Loci**: 2 (:term:`Lemoine <geometrographie>` :math:`S = 6`)

.. enunciation::

   On a :math:`2 \times 2` square grid :g:`P1P2P3P4` with horizontal midline :g:`AB`, center :g:`O`, and top midpoint :g:`D`, extend :g:`AB` by one grid unit to :g:`C`. Circle :g:`cCD` centered at :g:`C` through :g:`D` cuts :g:`AB` at :g:`M` in the golden ratio: :math:`|MB|/|AM| = |AB|/|MB| = \phi`.

.. picture:: 03-nguyen-2x2-square.svg
   :alt: GC-03.03 — Nguyen Thanh Dung's 2×2 Grid Compass Arc

Given & Constructive Steps
--------------------------

**Given**: A :math:`2 \times 2` grid with midline endpoints :g:`A` :math:`= (-1,0)` and :g:`B` :math:`= (1,0)`.

.. step::

   Form the :math:`2 \times 2` grid :g:`P1P2P3P4` centered at :g:`O` :math:`= (0,0)` with top midpoint :g:`D` :math:`= (0,1)`.

.. step::

   Mark :g:`C` :math:`= (2,0)` on ray :g:`AB` at unit distance beyond :g:`B`.

.. step::

   Draw circle :g:`cCD` centered at :g:`C` through :g:`D`, intersecting :g:`AB` internally at :g:`M`.

Exact Symbolic Proof & Certificate
----------------------------------

In right triangle :math:`\triangle COD`, legs :math:`|OC| = 2` and :math:`|OD| = 1` give radius :math:`|CD| = \sqrt{5}`. Hence :math:`x_M = 2 - \sqrt{5}`, giving :math:`|MB| = 1 - (2 - \sqrt{5}) = \sqrt{5} - 1 = 2/\phi` and :math:`|AM| = (2 - \sqrt{5}) - (-1) = 3 - \sqrt{5} = 2/\phi^2`, so :math:`|MB|/|AM| = \phi`.

.. list-table:: Machine-Verified Symbolic Certificate
   :widths: 30 70
   :header-rows: 1

   * - Invariant
     - Exact Symbolic Value
   * - Primary Golden Ratio
     - :g:`MB` :math:`/` :g:`AM` :math:`= \frac{1}{2} + \frac{\sqrt{5}}{2}` on collinear triple (:g:`A`, :g:`M`, :g:`B`)
   * - Exact Segment Lengths
     - :math:`|MB| = -1 + \sqrt{5}`, :math:`|AM| = 3 - \sqrt{5}`
   * - Rational Trigonometry :term:`Quadrances <quadrance>`
     - :math:`Q(M, B) = 6 - 2 \sqrt{5}`, :math:`Q(A, M) = 14 - 6 \sqrt{5}`, :math:`Q_{\text{long}}/Q_{\text{short}} = \frac{\sqrt{5}}{2} + \frac{3}{2} = \phi^2`
   * - Algebraic Number Field
     - :math:`\mathbb{Q}(\phi)`
   * - :term:`Géométrographie <geometrographie>` Loci
     - 2 given points · 1 lines · 1 circles · 1 polygons (elementary loci :math:`= 2`, Lemoine :math:`S = 6`)

Automated Divine Scan
---------------------

:mod:`geometor.divine.golden` detected **1** exact collinear golden section(s) and **0** connected golden chain(s) in this model:

- Section (:g:`A`, :g:`M`, :g:`B`): long :math:`|MB|^2 = 6 - 2 \sqrt{5}` vs. short :math:`|AM|^2 = 14 - 6 \sqrt{5}`

Historical Commentary & Attribution
-----------------------------------

Lattice coordinates supply orthogonal unit and double-unit segments without auxiliary angle bisections, making lattice-grid constructions popular in recreational and olympiad geometry.

- **Scholarly Citations**: :cite:`Cut-the-Knot: Golden Ratio in 2×2 Square <bogomolny-2x2>`, :cite:`Cut-the-Knot: Golden Ratio in Geometry <bogomolny-golden-ratio>`
- **Curated Reference**: `Golden Ratio in 2x2 Square <https://www.cut-the-knot.org/do_you_know/2x2GoldenRatio.shtml>`_ (curated by :person:`Alexander Bogomolny <alexander-bogomolny>`, *Cut-the-Knot*, © 1996–2018)
- **Concepts**: :term:`Golden Ratio (φ) <golden-ratio>` · :term:`Golden Section <golden-section>` · :term:`Quadrance <quadrance>`

.. toctree::
   :hidden:

   code
