:type: construction
:order: 4
:excerpt: Erect regular hexagon ABCDEF and regular pentagon AMNPF on the same side AF. The perpendiculars MQ and PR to diagonal MP at M and P intersect upper hexagon sides BC and DE at Q and R such that CQ/QB = DR/RE = φ.
:categories: 05-pentagons-polygons
:tags: field-pentagonal-hexagonal, tran-quang-hung

GC-05.04 · Tran Quang Hung's Shared-Base Regular Pentagon & Hexagon
===================================================================

**Discoverer(s)**: :person:`Tran Quang Hung <tran-quang-hung>` | **Date**: 2015 | **Field**: :math:`\mathbb{Q}(\sqrt{3}, \phi, \sqrt{10 - 2\sqrt{5}})` | **Loci**: 4 (:term:`Lemoine <geometrographie>` :math:`S = 12`)

.. enunciation::

   Erect regular hexagon :g:`ABCDEF` and regular pentagon :g:`AMNPF` on the same side :g:`AF`. The perpendiculars :g:`MQ` and :g:`PR` to diagonal :g:`MP` at :g:`M` and :g:`P` intersect upper hexagon sides :g:`BC` and :g:`DE` at :g:`Q` and :g:`R` such that :math:`|CQ|/|QB| = |DR|/|RE| = \phi`.

.. picture:: 04-tran-pentagon-hexagon.svg
   :alt: GC-05.04 — Tran Quang Hung's Shared-Base Regular Pentagon & Hexagon

Given & Constructive Steps
--------------------------

**Given**: Shared horizontal base :g:`A` :math:`= (-1,0)`, :g:`F` :math:`= (1,0)` of length :math:`2`.

.. step::

   Construct regular hexagon :g:`ABCDEF` of side :math:`2` above :g:`AF`, with upper-left side :g:`B` :math:`= (-2, \sqrt{3})` to :g:`C` :math:`= (-1, 2\sqrt{3})`.

.. step::

   Construct regular pentagon :g:`AMNPF` of side :math:`2` on the same side of :g:`AF`, with horizontal diagonal :g:`MP`.

.. step::

   Erect perpendiculars :g:`MQ` and :g:`PR` to :g:`MP` at :g:`M` and :g:`P`, cutting :g:`BC` at :g:`Q` and :g:`DE` at :g:`R`.

Exact Symbolic Proof & Certificate
----------------------------------

For base :math:`|AF| = 2`, diagonal :g:`MP` of regular pentagon :g:`AMNPF` has length :math:`2\phi`, so :g:`M` has abscissa :math:`x_M = -\phi` while :g:`B` and :g:`C` have abscissas :math:`x_B = -2` and :math:`x_C = -1`. Because :g:`MQ` is vertical (:math:`x = -\phi`), linear projection onto the :math:`x`-axis yields :math:`|CQ|/|QB| = (-1 - (-\phi))/(-\phi - (-2)) = (\phi - 1)/(2 - \phi) = (1/\phi)/(1/\phi^2) = \phi`.

.. list-table:: Machine-Verified Symbolic Certificate
   :widths: 30 70
   :header-rows: 1

   * - Invariant
     - Exact Symbolic Value
   * - Primary Golden Ratio
     - :g:`CQ` :math:`/` :g:`QB` :math:`= \frac{1}{2} + \frac{\sqrt{5}}{2}` on collinear triple (:g:`C`, :g:`Q`, :g:`B`)
   * - Exact Segment Lengths
     - :math:`|CQ| = -1 + \sqrt{5}`, :math:`|QB| = 3 - \sqrt{5}`
   * - Rational Trigonometry :term:`Quadrances <quadrance>`
     - :math:`Q(C, Q) = 6 - 2 \sqrt{5}`, :math:`Q(Q, B) = 14 - 6 \sqrt{5}`, :math:`Q_{\text{long}}/Q_{\text{short}} = \frac{\sqrt{5}}{2} + \frac{3}{2} = \phi^2`
   * - Algebraic Number Field
     - :math:`\mathbb{Q}(\sqrt{3}, \phi, \sqrt{10 - 2\sqrt{5}})`
   * - :term:`Géométrographie <geometrographie>` Loci
     - 2 given points · 4 lines · 0 circles · 2 polygons (elementary loci :math:`= 4`, Lemoine :math:`S = 12`)

Automated Divine Scan
---------------------

:mod:`geometor.divine.golden` detected **2** exact collinear golden section(s) and **0** connected golden chain(s) in this model:

- Section (:g:`B`, :g:`Q`, :g:`C`): long :math:`|QC|^2 = 6 - 2 \sqrt{5}` vs. short :math:`|BQ|^2 = 14 - 6 \sqrt{5}`
- Section (:g:`D`, :g:`R`, :g:`E`): long :math:`|DR|^2 = 6 - 2 \sqrt{5}` vs. short :math:`|RE|^2 = 14 - 6 \sqrt{5}`

Historical Commentary & Attribution
-----------------------------------

Projected onto the horizontal axis, the hexagon's lateral overhang has width :math:`1` while the pentagon's lateral overhang has width :math:`\phi - 1 = 1/\phi`, immediately sectioning the overhang in extreme and mean ratio.

- **Scholarly Citations**: :cite:`Cut-the-Knot: Golden Ratio in Pentagon and Hexagon <bogomolny-5-6>`, :cite:`Cut-the-Knot: Golden Ratio in Geometry <bogomolny-golden-ratio>`
- **Curated Reference**: `Golden Ratio in Pentagon and Hexagon <https://www.cut-the-knot.org/do_you_know/5-6-GoldenRatioIn.shtml>`_ (curated by :person:`Alexander Bogomolny <alexander-bogomolny>`, *Cut-the-Knot*, © 1996–2018)
- **Concepts**: :term:`Golden Ratio (φ) <golden-ratio>` · :term:`Golden Section <golden-section>`

.. toctree::
   :hidden:

   code
