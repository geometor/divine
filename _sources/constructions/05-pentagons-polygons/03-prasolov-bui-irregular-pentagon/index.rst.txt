:type: construction
:order: 3
:excerpt: Let ABCDE be any convex pentagon—regular or irregular—whose five peripheral triangles triangle ABE, triangle ABC, triangle BCD, triangle CDE, triangle DEA have equal area. Then every diagonal is parallel to the opposite side and is divided by the crossing diagonals in the golden ratio, e.g. BM/MD = φ.
:categories: 05-pentagons-polygons
:tags: field-q-phi, golden-chain, v-v-prasolov, bui-quang-tuan

GC-05.03 · Prasolov & Bùi Quang Tuân's Equi-Area Irregular Pentagon
===================================================================

**Discoverer(s)**: :person:`Viktor Vasil'evich Prasolov <v-v-prasolov>`, :person:`Bùi Quang Tuân <bui-quang-tuan>` | **Date**: 2006 | **Field**: :math:`\mathbb{Q}(\phi)` | **Loci**: 3 (:term:`Lemoine <geometrographie>` :math:`S = 9`)

.. enunciation::

   Let :g:`ABCDE` be *any* convex pentagon—regular or irregular—whose five peripheral triangles :math:`\triangle ABE, \triangle ABC, \triangle BCD, \triangle CDE, \triangle DEA` have equal area. Then every diagonal is parallel to the opposite side and is divided by the crossing diagonals in the golden ratio, e.g. :math:`|BM|/|MD| = \phi`.

.. picture:: 03-prasolov-bui-irregular-pentagon.svg
   :alt: GC-05.03 — Prasolov & Bùi Quang Tuân's Equi-Area Irregular Pentagon

Given & Constructive Steps
--------------------------

**Given**: Sheared irregular convex pentagon :g:`ABCDE` over :math:`\mathbb{Q}(\phi)` with :g:`A` :math:`= (0,0)` and :g:`B` :math:`= (2\phi, 0)`, each peripheral triangle having exact area :math:`2`.

.. step::

   Place irregular vertices :g:`A` :math:`= (0,0)`, :g:`B` :math:`= (2\phi, 0)`, :g:`C` :math:`= (3\phi+1, 2/\phi)`, :g:`D` :math:`= (2\phi+1, 2)`, and :g:`E` :math:`= (1/\phi, 2/\phi)`.

.. step::

   Draw diagonals :g:`BD`, :g:`CE`, and :g:`AC`.

.. step::

   Mark intersections :g:`M` :math:`= BD \cap CE` and :g:`N` :math:`= BD \cap AC`.

Exact Symbolic Proof & Certificate
----------------------------------

Equal areas :math:`[ABE] = [ABC]` with shared base :g:`AB` force :math:`CE \parallel AB`; cyclically, every diagonal is parallel to its opposite side, so :math:`ABME` is a parallelogram with :math:`|EM| = |AB|`. Set :math:`x = |BM|/|MD|`. Then :math:`[ABE] = [BM E]` (half of parallelogram :math:`ABME`), while :math:`[CDE] = [BCD]` implies :math:`|CE|/|EM| = 1 + 1/x` and :math:`x = 1 + 1/x`, forcing :math:`x = \phi` purely from affine area invariance!

.. list-table:: Machine-Verified Symbolic Certificate
   :widths: 30 70
   :header-rows: 1

   * - Invariant
     - Exact Symbolic Value
   * - Primary Golden Ratio
     - :g:`BM` :math:`/` :g:`MD` :math:`= \frac{1}{2} + \frac{\sqrt{5}}{2}` on collinear triple (:g:`B`, :g:`M`, :g:`D`)
   * - Exact Segment Lengths
     - :math:`|BM| = \frac{5}{2} - \frac{\sqrt{5}}{2}`, :math:`|MD| = - \frac{5}{2} + \frac{3 \sqrt{5}}{2}`
   * - Rational Trigonometry :term:`Quadrances <quadrance>`
     - :math:`Q(B, M) = \frac{15}{2} - \frac{5 \sqrt{5}}{2}`, :math:`Q(M, D) = \frac{35}{2} - \frac{15 \sqrt{5}}{2}`, :math:`Q_{\text{long}}/Q_{\text{short}} = \frac{\sqrt{5}}{2} + \frac{3}{2} = \phi^2`
   * - Algebraic Number Field
     - :math:`\mathbb{Q}(\phi)`
   * - :term:`Géométrographie <geometrographie>` Loci
     - 2 given points · 3 lines · 0 circles · 1 polygons (elementary loci :math:`= 3`, Lemoine :math:`S = 9`)

Automated Divine Scan
---------------------

:mod:`geometor.divine.golden` detected **6** exact collinear golden section(s) and **1** connected golden chain(s) in this model:

- Section (:g:`B`, :g:`N`, :g:`M`): long :math:`|BN|^2 = \frac{35}{2} - \frac{15 \sqrt{5}}{2}` vs. short :math:`|NM|^2 = 45 - 20 \sqrt{5}`
- Section (:g:`B`, :g:`N`, :g:`D`): long :math:`|ND|^2 = \frac{15}{2} - \frac{5 \sqrt{5}}{2}` vs. short :math:`|BN|^2 = \frac{35}{2} - \frac{15 \sqrt{5}}{2}`
- Section (:g:`B`, :g:`M`, :g:`D`): long :math:`|BM|^2 = \frac{15}{2} - \frac{5 \sqrt{5}}{2}` vs. short :math:`|MD|^2 = \frac{35}{2} - \frac{15 \sqrt{5}}{2}`
- Section (:g:`N`, :g:`M`, :g:`D`): long :math:`|MD|^2 = \frac{35}{2} - \frac{15 \sqrt{5}}{2}` vs. short :math:`|NM|^2 = 45 - 20 \sqrt{5}`
- Section (:g:`E`, :g:`M`, :g:`C`): long :math:`|EM|^2 = 2 \sqrt{5} + 6` vs. short :math:`|MC|^2 = 4`
- Section (:g:`A`, :g:`N`, :g:`C`): long :math:`|AN|^2 = \frac{43}{2} - \frac{7 \sqrt{5}}{2}` vs. short :math:`|NC|^2 = 41 - 16 \sqrt{5}`

**Connected Golden Chains**:

- Chain (:g:`B` — :g:`N` — :g:`M` — :g:`D`) spanning 2 overlapping golden sections (progression ``> <``)

Historical Commentary & Attribution
-----------------------------------

Because parallelisms and length ratios on parallel lines are affine invariants, *every* affine image of a regular pentagon retains all five golden pentagram chains while losing all metric symmetry—and lives entirely over :math:`\mathbb{Q}(\phi)` without :math:`\sin 36^\circ`.

- **Scholarly Citations**: :cite:`Problems in Plane Geometry <prasolov-2006>`, :cite:`Cut-the-Knot: Golden Ratio in an Irregular Pentagon <bogomolny-irregular-pentagon>`, :cite:`Cut-the-Knot: Golden Ratio in Geometry <bogomolny-golden-ratio>`
- **Curated Reference**: `Golden Ratio in an Irregular Pentagon <https://www.cut-the-knot.org/do_you_know/NoRegularPentagon.shtml>`_ (curated by :person:`Alexander Bogomolny <alexander-bogomolny>`, *Cut-the-Knot*, © 1996–2018)
- **Concepts**: :term:`Golden Ratio (φ) <golden-ratio>` · :term:`Golden Section <golden-section>` · :term:`Golden Chain <golden-chain>`

.. toctree::
   :hidden:

   code
