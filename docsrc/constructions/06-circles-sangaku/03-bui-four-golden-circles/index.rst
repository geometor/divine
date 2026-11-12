:type: construction
:order: 3
:excerpt: Let unit circles cA and cB pass through each other's centers, intersecting at E and N, and let congruent unit circles cD and cC be externally tangent to both cA and cB. Then (C, N, E, D) is a 4-point golden chain with EN/ED = ND/EN = φ.
:categories: 06-circles-sangaku
:tags: field-q-sqrt3-phi, golden-chain, bui-quang-tuan

GC-06.03 · Bùi Quang Tuân's Four Congruent Golden Circles
=========================================================

**Discoverer(s)**: :person:`Bùi Quang Tuân <bui-quang-tuan>` | **Date**: 2015 | **Field**: :math:`\mathbb{Q}(\sqrt{3}, \phi)` | **Loci**: 5 (:term:`Lemoine <geometrographie>` :math:`S = 15`)

.. enunciation::

   Let unit circles :g:`cA` and :g:`cB` pass through each other's centers, intersecting at :g:`E` and :g:`N`, and let congruent unit circles :g:`cD` and :g:`cC` be externally tangent to both :g:`cA` and :g:`cB`. Then :math:`(C, N, E, D)` is a 4-point golden chain with :math:`|EN|/|ED| = |ND|/|EN| = \phi`.

.. picture:: 03-bui-four-golden-circles.svg
   :alt: GC-06.03 — Bùi Quang Tuân's Four Congruent Golden Circles

Given & Constructive Steps
--------------------------

**Given**: Unit vesica piscis circles :g:`cA` and :g:`cB` centered at :g:`A` :math:`= (-\tfrac{1}{2}, 0)` and :g:`B` :math:`= (\tfrac{1}{2}, 0)`.

.. step::

   Mark lens vertices :g:`E` :math:`= (0, \tfrac{\sqrt{3}}{2})` and :g:`N` :math:`= (0, -\tfrac{\sqrt{3}}{2})` on symmetry axis :g:`NE`.

.. step::

   Locate centers :g:`D` :math:`= (0, \tfrac{\sqrt{15}}{2})` and :g:`C` :math:`= (0, -\tfrac{\sqrt{15}}{2})` at distance :math:`2` from both :g:`A` and :g:`B`.

.. step::

   Draw congruent unit circles :g:`cD` and :g:`cC` externally tangent to :g:`cA` and :g:`cB`.

Exact Symbolic Proof & Certificate
----------------------------------

External tangency of unit circle :g:`cD` to :g:`cA` and :g:`cB` requires :math:`|AD| = |BD| = 2`. Since :math:`|AM| = 1/2`, :math:`y_D = \sqrt{2^2 - (1/2)^2} = \frac{\sqrt{15}}{2}`, whereas :math:`y_E = \frac{\sqrt{3}}{2}`. Consequently :math:`|EN| = \sqrt{3}` and :math:`|ED| = \frac{\sqrt{15} - \sqrt{3}}{2} = \frac{\sqrt{3}}{\phi}`, giving :math:`|EN|/|ED| = \phi`.

.. list-table:: Machine-Verified Symbolic Certificate
   :widths: 30 70
   :header-rows: 1

   * - Invariant
     - Exact Symbolic Value
   * - Primary Golden Ratio
     - :g:`EN` :math:`/` :g:`ED` :math:`= \frac{1}{2} + \frac{\sqrt{5}}{2}` on collinear triple (:g:`N`, :g:`E`, :g:`D`)
   * - Exact Segment Lengths
     - :math:`|EN| = \sqrt{3}`, :math:`|ED| = \frac{- \sqrt{3} + \sqrt{15}}{2}`
   * - Rational Trigonometry :term:`Quadrances <quadrance>`
     - :math:`Q(E, N) = 3`, :math:`Q(E, D) = \frac{9}{2} - \frac{3 \sqrt{5}}{2}`, :math:`Q_{\text{long}}/Q_{\text{short}} = \frac{\sqrt{5}}{2} + \frac{3}{2} = \phi^2`
   * - Algebraic Number Field
     - :math:`\mathbb{Q}(\sqrt{3}, \phi)`
   * - :term:`Géométrographie <geometrographie>` Loci
     - 2 given points · 1 lines · 4 circles · 0 polygons (elementary loci :math:`= 5`, Lemoine :math:`S = 15`)

Automated Divine Scan
---------------------

:mod:`geometor.divine.golden` detected **2** exact collinear golden section(s) and **1** connected golden chain(s) in this model:

- Section (:g:`C`, :g:`N`, :g:`E`): long :math:`|NE|^2 = 3` vs. short :math:`|CN|^2 = \frac{9}{2} - \frac{3 \sqrt{5}}{2}`
- Section (:g:`N`, :g:`E`, :g:`D`): long :math:`|NE|^2 = 3` vs. short :math:`|ED|^2 = \frac{9}{2} - \frac{3 \sqrt{5}}{2}`

**Connected Golden Chains**:

- Chain (:g:`C` — :g:`N` — :g:`E` — :g:`D`) spanning 2 overlapping golden sections (progression ``< >``)

Historical Commentary & Attribution
-----------------------------------

Compare this four-circle packing directly with Hofstetter's Mascheroni compass-only construction (:doc:`../../01-minimal-compass/05-hofstetter-compass-only/index`), which uses the same :math:`\sqrt{15}/2` vs. :math:`\sqrt{3}/2` radical ratio.

- **Scholarly Citations**: :cite:`Cut-the-Knot: Four Golden Circles <bogomolny-four-circles>`, :cite:`Cut-the-Knot: Golden Ratio in Geometry <bogomolny-golden-ratio>`
- **Curated Reference**: `Four Golden Circles <https://www.cut-the-knot.org/do_you_know/FourGoldenCircles.shtml>`_ (curated by :person:`Alexander Bogomolny <alexander-bogomolny>`, *Cut-the-Knot*, © 1996–2018)
- **Concepts**: :term:`Golden Ratio (φ) <golden-ratio>` · :term:`Golden Section <golden-section>` · :term:`Golden Chain <golden-chain>` · :term:`Vesica Piscis <vesica-piscis>`

.. toctree::
   :hidden:

   code
