:type: construction
:order: 4
:excerpt: Let congruent unit circles cA, cB, cC be mutually externally tangent at D, E, F, and let circle cO pass through their centers A, B, C. Line DF intersects cO at J and G to form a 4-point golden chain DF/FG = DG/DF = φ.
:categories: 06-circles-sangaku
:tags: field-q-sqrt3-phi, golden-chain, tran-quang-hung, elliot-mcgucken

GC-06.04 · Tran Quang Hung & Elliot McGucken's Three Tangent Circles
====================================================================

**Discoverer(s)**: :person:`Tran Quang Hung <tran-quang-hung>`, :person:`Elliot McGucken <elliot-mcgucken>` | **Date**: 2016 | **Field**: :math:`\mathbb{Q}(\sqrt{3}, \phi)` | **Loci**: 5 (:term:`Lemoine <geometrographie>` :math:`S = 15`)

.. enunciation::

   Let congruent unit circles :g:`cA`, :g:`cB`, :g:`cC` be mutually externally tangent at :g:`D`, :g:`E`, :g:`F`, and let circle :g:`cO` pass through their centers :g:`A`, :g:`B`, :g:`C`. Line :g:`DF` intersects :g:`cO` at :g:`J` and :g:`G` to form a 4-point golden chain :math:`|DF|/|FG| = |DG|/|DF| = \phi`.

.. picture:: 04-tran-mcgucken-three-tangent-circles.svg
   :alt: GC-06.04 — Tran Quang Hung & Elliot McGucken's Three Tangent Circles

Given & Constructive Steps
--------------------------

**Given**: Equilateral center triangle :g:`ABC` of side :math:`2` centered at :g:`O` :math:`= (0,0)` with :g:`A` :math:`= (0, \tfrac{2\sqrt{3}}{3})`.

.. step::

   Draw mutually tangent unit circles :g:`cA`, :g:`cB`, :g:`cC` touching at midpoints :g:`D`, :g:`E`, :g:`F` of :g:`ABC`.

.. step::

   Draw circumcircle :g:`cO` of radius :math:`\tfrac{2\sqrt{3}}{3}` through centers :g:`A`, :g:`B`, :g:`C`.

.. step::

   Extend midline :g:`DF` across :g:`cO` to obtain intersections :g:`G` and :g:`J`.

Exact Symbolic Proof & Certificate
----------------------------------

Because :g:`D`, :g:`E`, :g:`F` are the midpoints of equilateral :g:`ABC` inscribed in :g:`cO`, chord :g:`JG` along midline :g:`DF` reproduces George Odom's configuration (:doc:`../../02-equilateral-hexagon/01-odom-equilateral/index`) inside the three-circle packing: :math:`|DF| = 1` and :math:`|FG| = |DJ| = \frac{\sqrt{5}-1}{2} = 1/\phi`, hence :math:`|DF|/|FG| = \phi`.

.. list-table:: Machine-Verified Symbolic Certificate
   :widths: 30 70
   :header-rows: 1

   * - Invariant
     - Exact Symbolic Value
   * - Primary Golden Ratio
     - :g:`DF` :math:`/` :g:`FG` :math:`= \frac{1}{2} + \frac{\sqrt{5}}{2}` on collinear triple (:g:`D`, :g:`F`, :g:`G`)
   * - Exact Segment Lengths
     - :math:`|DF| = 1`, :math:`|FG| = - \frac{1}{2} + \frac{\sqrt{5}}{2}`
   * - Rational Trigonometry :term:`Quadrances <quadrance>`
     - :math:`Q(D, F) = 1`, :math:`Q(F, G) = \frac{3}{2} - \frac{\sqrt{5}}{2}`, :math:`Q_{\text{long}}/Q_{\text{short}} = \frac{\sqrt{5}}{2} + \frac{3}{2} = \phi^2`
   * - Algebraic Number Field
     - :math:`\mathbb{Q}(\sqrt{3}, \phi)`
   * - :term:`Géométrographie <geometrographie>` Loci
     - 2 given points · 1 lines · 4 circles · 1 polygons (elementary loci :math:`= 5`, Lemoine :math:`S = 15`)

Automated Divine Scan
---------------------

:mod:`geometor.divine.golden` detected **2** exact collinear golden section(s) and **1** connected golden chain(s) in this model:

- Section (:g:`G`, :g:`F`, :g:`D`): long :math:`|FD|^2 = 1` vs. short :math:`|GF|^2 = \frac{3}{2} - \frac{\sqrt{5}}{2}`
- Section (:g:`F`, :g:`D`, :g:`J`): long :math:`|FD|^2 = 1` vs. short :math:`|DJ|^2 = \frac{3}{2} - \frac{\sqrt{5}}{2}`

**Connected Golden Chains**:

- Chain (:g:`G` — :g:`F` — :g:`D` — :g:`J`) spanning 2 overlapping golden sections (progression ``< >``)

Historical Commentary & Attribution
-----------------------------------

Furthermore, extending :g:`DF` across :g:`cC` adds another unit chord segment beyond :g:`D`, weaving six circle intersections along a single line.

- **Scholarly Citations**: :cite:`Cut-the-Knot: Golden Ratio in Three Tangent Circles <bogomolny-3-tangent>`, :cite:`Cut-the-Knot: Golden Ratio in Geometry <bogomolny-golden-ratio>`
- **Curated Reference**: `Golden Ratio in Three Tangent Circles <https://www.cut-the-knot.org/do_you_know/3TangentCirclesGoldenRatio.shtml>`_ (curated by :person:`Alexander Bogomolny <alexander-bogomolny>`, *Cut-the-Knot*, © 1996–2018)
- **Concepts**: :term:`Golden Ratio (φ) <golden-ratio>` · :term:`Golden Section <golden-section>` · :term:`Golden Chain <golden-chain>` · :term:`Intersecting Chords Theorem <intersecting-chords-theorem>`

.. toctree::
   :hidden:

   code
