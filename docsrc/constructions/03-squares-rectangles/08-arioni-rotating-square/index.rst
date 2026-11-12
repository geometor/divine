:type: construction
:order: 8
:excerpt: Rotate unit square DGHJ clockwise by 30^circ around vertex D to obtain congruent square DCBA. Circle cAC centered at A through opposite vertex C intersects line DG at E and F such that DG/GE = DE/DG = φ.
:categories: 03-squares-rectangles
:tags: field-q-sqrt3-phi, golden-chain, john-arioni

GC-03.08 · John Arioni's 30°-Rotated Unit Square & Diagonal Circle
==================================================================

**Discoverer(s)**: :person:`John Arioni <john-arioni>` | **Date**: 2016 | **Field**: :math:`\mathbb{Q}(\sqrt{3}, \phi)` | **Loci**: 2 (:term:`Lemoine <geometrographie>` :math:`S = 6`)

.. enunciation::

   Rotate unit square :g:`DGHJ` clockwise by :math:`30^\circ` around vertex :g:`D` to obtain congruent square :g:`DCBA`. Circle :g:`cAC` centered at :g:`A` through opposite vertex :g:`C` intersects line :g:`DG` at :g:`E` and :g:`F` such that :math:`|DG|/|GE| = |DE|/|DG| = \phi`.

.. picture:: 08-arioni-rotating-square.svg
   :alt: GC-03.08 — John Arioni's 30°-Rotated Unit Square & Diagonal Circle

Given & Constructive Steps
--------------------------

**Given**: Unit square :g:`DGHJ` on base :g:`D` :math:`= (0,0)`, :g:`G` :math:`= (1,0)`.

.. step::

   Rotate :g:`DGHJ` clockwise by :math:`30^\circ` about :g:`D` so :g:`A` :math:`= (\tfrac{1}{2}, \tfrac{\sqrt{3}}{2})` and :g:`C` :math:`= (\tfrac{\sqrt{3}}{2}, -\tfrac{1}{2})`.

.. step::

   Draw diagonal :g:`AC` (of length :math:`\sqrt{2}`) of the rotated unit square :g:`DCBA`.

.. step::

   Draw circle :g:`cAC` centered at :g:`A` through :g:`C`, cutting base line :g:`DG` at :g:`E` and :g:`F`.

Exact Symbolic Proof & Certificate
----------------------------------

Center :g:`A` has altitude :math:`y_A = \frac{\sqrt{3}}{2}` above line :g:`DG` (:math:`y = 0`) and abscissa :math:`x_A = \frac{1}{2}`, while radius :math:`|AC| = \sqrt{2}`. Setting :math:`y = 0` in :math:`(x - \tfrac{1}{2})^2 + (\tfrac{\sqrt{3}}{2})^2 = 2` gives :math:`(x - \tfrac{1}{2})^2 = \frac{5}{4}`, hence :math:`x_E = \frac{1 + \sqrt{5}}{2} = \phi` and :math:`x_F = -1/\phi`, forming the 4-point golden chain :math:`(F, D, G, E)`.

.. list-table:: Machine-Verified Symbolic Certificate
   :widths: 30 70
   :header-rows: 1

   * - Invariant
     - Exact Symbolic Value
   * - Primary Golden Ratio
     - :g:`DG` :math:`/` :g:`GE` :math:`= \frac{1}{2} + \frac{\sqrt{5}}{2}` on collinear triple (:g:`D`, :g:`G`, :g:`E`)
   * - Exact Segment Lengths
     - :math:`|DG| = 1`, :math:`|GE| = - \frac{1}{2} + \frac{\sqrt{5}}{2}`
   * - Rational Trigonometry :term:`Quadrances <quadrance>`
     - :math:`Q(D, G) = 1`, :math:`Q(G, E) = \frac{3}{2} - \frac{\sqrt{5}}{2}`, :math:`Q_{\text{long}}/Q_{\text{short}} = \frac{\sqrt{5}}{2} + \frac{3}{2} = \phi^2`
   * - Algebraic Number Field
     - :math:`\mathbb{Q}(\sqrt{3}, \phi)`
   * - :term:`Géométrographie <geometrographie>` Loci
     - 2 given points · 1 lines · 1 circles · 2 polygons (elementary loci :math:`= 2`, Lemoine :math:`S = 6`)

Automated Divine Scan
---------------------

:mod:`geometor.divine.golden` detected **2** exact collinear golden section(s) and **1** connected golden chain(s) in this model:

- Section (:g:`F`, :g:`D`, :g:`G`): long :math:`|DG|^2 = 1` vs. short :math:`|FD|^2 = \frac{3}{2} - \frac{\sqrt{5}}{2}`
- Section (:g:`D`, :g:`G`, :g:`E`): long :math:`|DG|^2 = 1` vs. short :math:`|GE|^2 = \frac{3}{2} - \frac{\sqrt{5}}{2}`

**Connected Golden Chains**:

- Chain (:g:`F` — :g:`D` — :g:`G` — :g:`E`) spanning 2 overlapping golden sections (progression ``< >``)

Historical Commentary & Attribution
-----------------------------------

Rotating by :math:`30^\circ` converts the square's diagonal quadrance :math:`2` minus the equilateral altitude quadrance :math:`3/4` directly into :math:`5/4`.

- **Scholarly Citations**: :cite:`Cut-the-Knot: Golden Ratio by Rotating a Square <bogomolny-arioni-square>`, :cite:`Cut-the-Knot: Golden Ratio in Geometry <bogomolny-golden-ratio>`
- **Curated Reference**: `Golden Ratio by Rotating a Square <https://www.cut-the-knot.org/do_you_know/JohnArioni.shtml>`_ (curated by :person:`Alexander Bogomolny <alexander-bogomolny>`, *Cut-the-Knot*, © 1996–2018)
- **Concepts**: :term:`Golden Ratio (φ) <golden-ratio>` · :term:`Golden Section <golden-section>` · :term:`Golden Chain <golden-chain>` · :term:`Quadrance <quadrance>`

.. toctree::
   :hidden:

   code
