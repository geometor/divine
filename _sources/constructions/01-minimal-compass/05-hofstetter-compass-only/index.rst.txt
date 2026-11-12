:type: construction
:order: 5
:excerpt: Using a compass alone and zero straightedge lines, five circles constructed from given points A and B generate four collinear points Y, C, D, X such that CX/CD = CD/DX = φ.
:categories: 01-minimal-compass
:tags: field-q-sqrt3-phi, golden-chain, compass-only, kurt-hofstetter

GC-01.05 · Mascheroni Five-Circle Compass-Only Construction
===========================================================

**Discoverer(s)**: :person:`Kurt Hofstetter <kurt-hofstetter>` | **Date**: 2002 | **Field**: :math:`\mathbb{Q}(\sqrt{3}, \phi)` | **Loci**: 5 (:term:`Lemoine <geometrographie>` :math:`S = 15`)

.. enunciation::

   Using a compass alone and **zero straightedge lines**, five circles constructed from given points :g:`A` and :g:`B` generate four collinear points :g:`Y`, :g:`C`, :g:`D`, :g:`X` such that :math:`|CX|/|CD| = |CD|/|DX| = \phi`.

.. picture:: 05-hofstetter-compass-only.svg
   :alt: GC-01.05 — Mascheroni Five-Circle Compass-Only Construction

Given & Constructive Steps
--------------------------

**Given**: Two distinct points :g:`A` :math:`= (0, 0)` and :g:`B` :math:`= (1, 0)` with no lines drawn.

.. step::

   Draw unit circles :g:`c1` :math:`= A(B)` and :g:`c2` :math:`= B(A)`, intersecting at :g:`C` and :g:`D`.

.. step::

   Draw circle :g:`c3` :math:`= C(D)` of radius :math:`\sqrt{3}`; without a ruler, :g:`c3` meets :g:`c1` again at :g:`E` :math:`= (-1, 0)` and :g:`c2` again at :g:`F` :math:`= (2, 0)`.

.. step::

   Draw radius-:math:`2` circles :g:`c4` :math:`= B(E)` and :g:`c5` :math:`= A(F)`, intersecting at :g:`X` :math:`= (\tfrac{1}{2}, -\tfrac{\sqrt{15}}{2})` and :g:`Y` :math:`= (\tfrac{1}{2}, \tfrac{\sqrt{15}}{2})`.

Exact Symbolic Proof & Certificate
----------------------------------

For :g:`C` :math:`= (\tfrac{1}{2}, \tfrac{\sqrt{3}}{2})`, the quadrance to :math:`(-1, 0)` is :math:`(-\tfrac{3}{2})^2 + (\tfrac{\sqrt{3}}{2})^2 = 3 = Q(C, D)`, confirming that :g:`E` and symmetrically :g:`F` lie on :g:`c3` without drawing line :math:`AB`. Circles :g:`c4` and :g:`c5` both have radius :math:`2` centered at :g:`B` and :g:`A`, so their intersections :g:`X` and :g:`Y` lie on the perpendicular bisector :math:`x = \tfrac{1}{2}` alongside :g:`C` and :g:`D`, with ordinates :math:`\pm\tfrac{\sqrt{15}}{2}`. Thus :math:`|CD| = \sqrt{3}` and :math:`|DX| = \tfrac{\sqrt{15} - \sqrt{3}}{2} = \sqrt{3}/\phi`, proving :math:`|CD|/|DX| = \phi`.

.. list-table:: Machine-Verified Symbolic Certificate
   :widths: 30 70
   :header-rows: 1

   * - Invariant
     - Exact Symbolic Value
   * - Primary Golden Ratio
     - :g:`CD` :math:`/` :g:`DX` :math:`= \frac{1}{2} + \frac{\sqrt{5}}{2}` on collinear triple (:g:`C`, :g:`D`, :g:`X`)
   * - Exact Segment Lengths
     - :math:`|CD| = \sqrt{3}`, :math:`|DX| = \frac{- \sqrt{3} + \sqrt{15}}{2}`
   * - Rational Trigonometry :term:`Quadrances <quadrance>`
     - :math:`Q(C, D) = 3`, :math:`Q(D, X) = \frac{9}{2} - \frac{3 \sqrt{5}}{2}`, :math:`Q_{\text{long}}/Q_{\text{short}} = \frac{\sqrt{5}}{2} + \frac{3}{2} = \phi^2`
   * - Algebraic Number Field
     - :math:`\mathbb{Q}(\sqrt{3}, \phi)`
   * - :term:`Géométrographie <geometrographie>` Loci
     - 2 given points · 0 lines · 5 circles · 0 polygons (elementary loci :math:`= 5`, Lemoine :math:`S = 15`)

Automated Divine Scan
---------------------

:mod:`geometor.divine.golden` detected **2** exact collinear golden section(s) and **1** connected golden chain(s) in this model:

- Section (:g:`X`, :g:`D`, :g:`C`): long :math:`|DC|^2 = 3` vs. short :math:`|XD|^2 = \frac{9}{2} - \frac{3 \sqrt{5}}{2}`
- Section (:g:`D`, :g:`C`, :g:`Y`): long :math:`|DC|^2 = 3` vs. short :math:`|CY|^2 = \frac{9}{2} - \frac{3 \sqrt{5}}{2}`

**Connected Golden Chains**:

- Chain (:g:`X` — :g:`D` — :g:`C` — :g:`Y`) spanning 2 overlapping golden sections (progression ``< >``)

Historical Commentary & Attribution
-----------------------------------

In accordance with the Mohr–Mascheroni theorem, every ruler-and-compass point construction can be executed by compass alone. :person:`Kurt Hofstetter <kurt-hofstetter>`'s five-circle construction (:cite:`Hofstetter 2002 <hofstetter-2002>`, :cite:`Cut-the-Knot <ctk-compass-only>`) achieves the golden section in just five arcs—and our :mod:`geometor.divine.golden` collinear point scanner detects the entire :math:`(Y, C, D, X)` golden chain automatically despite zero lines in the model.

- **Scholarly Citations**: :cite:`A Simple Construction of the Golden Section <hofstetter-2002>`, :cite:`Cut-the-Knot: Golden Ratio by Compass Only <ctk-compass-only>`
- **Curated Reference**: `Golden Ratio by Compass Only <https://www.cut-the-knot.org/do_you_know/GoldenRatioByCompass.shtml>`_ (curated by :person:`Alexander Bogomolny <alexander-bogomolny>`, *Cut-the-Knot*, © 1996–2018)
- **Concepts**: :term:`Mascheroni Construction <mascheroni-construction>` · :term:`Golden Chain <golden-chain>` · :term:`Vesica Piscis <vesica-piscis>`

.. toctree::
   :hidden:

   code
