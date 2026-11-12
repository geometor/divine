:type: construction
:order: 7
:excerpt: On line L through O, draw circle cO meeting L at A and B, circle cBA meeting L at C, and circle cCO meeting cO above L at M and cBA below L at N. Then chord MN cuts cO at P with MN/MP = MP/PN = φ.
:categories: 01-minimal-compass
:tags: field-algebraic, bui-quang-tuan

GC-01.07 · Bùi Quang Tuân's Five-Step Three-Circle Secant
=========================================================

**Discoverer(s)**: :person:`Bùi Quang Tuân <bui-quang-tuan>` | **Date**: 2014 | **Field**: :math:`\mathbb{Q}(\sqrt{5}, \sqrt{7})` | **Loci**: 5 (:term:`Lemoine <geometrographie>` :math:`S = 15`)

.. enunciation::

   On line :g:`L` through :g:`O`, draw circle :g:`cO` meeting :g:`L` at :g:`A` and :g:`B`, circle :g:`cBA` meeting :g:`L` at :g:`C`, and circle :g:`cCO` meeting :g:`cO` above :g:`L` at :g:`M` and :g:`cBA` below :g:`L` at :g:`N`. Then chord :g:`MN` cuts :g:`cO` at :g:`P` with :math:`|MN|/|MP| = |MP|/|PN| = \phi`.

.. picture:: 07-bui-5step.svg
   :alt: GC-01.07 — Bùi Quang Tuân's Five-Step Three-Circle Secant

Given & Constructive Steps
--------------------------

**Given**: Center :g:`O` :math:`= (0, 0)` and unit point :g:`B` :math:`= (-1, 0)` defining carrier line :g:`L`.

.. step::

   Draw line :g:`L` through :g:`O` and :g:`B`, and unit circle :g:`cO` meeting :g:`L` again at :g:`A` :math:`= (1, 0)`.

.. step::

   Draw circle :g:`cBA` of radius :math:`2` centered at :g:`B` through :g:`A`, meeting :g:`L` beyond :g:`B` at :g:`C` :math:`= (-3, 0)`.

.. step::

   Draw circle :g:`cCO` of radius :math:`3` centered at :g:`C` through :g:`O`, cutting :g:`cO` above :g:`L` at :g:`M` :math:`= (-\tfrac{1}{6}, \tfrac{\sqrt{35}}{6})` and :g:`cBA` below :g:`L` at :g:`N` :math:`= (-\tfrac{3}{4}, -\tfrac{3\sqrt{7}}{4})`.

.. step::

   Join :g:`MN`, intersecting unit circle :g:`cO` a second time at :g:`P`.

Exact Symbolic Proof & Certificate
----------------------------------

Direct quadrance computation between :g:`M` and :g:`N` yields :math:`Q(M, N) = (\tfrac{7}{12})^2 + (\tfrac{\sqrt{35}}{6} + \tfrac{3\sqrt{7}}{4})^2 = \tfrac{21}{4} + \tfrac{7\sqrt{5}}{4} = \tfrac{7}{2}\phi^2`. Because :g:`O`, :g:`M`, and :g:`N` all lie on radius-:math:`3` circle :g:`cCO` while :g:`M` and :g:`P` lie on unit circle :g:`cO`, inscribed-angle similarity with diameter endpoint :math:`(-6, 0)` of :g:`cCO` gives :math:`Q(M, P) = \tfrac{7}{2}` and :math:`Q(P, N) = \tfrac{7}{2}\phi^{-2}`. Hence :math:`Q(M, P) / Q(P, N) = \phi^2` and :math:`|MP|/|PN| = \phi`.

.. list-table:: Machine-Verified Symbolic Certificate
   :widths: 30 70
   :header-rows: 1

   * - Invariant
     - Exact Symbolic Value
   * - Primary Golden Ratio
     - :g:`MP` :math:`/` :g:`PN` :math:`= \frac{1}{2} + \frac{\sqrt{5}}{2}` on collinear triple (:g:`M`, :g:`P`, :g:`N`)
   * - Exact Segment Lengths
     - :math:`|MP| = \frac{\sqrt{7} \sqrt{- \sqrt{2} \sqrt{\sqrt{5} + 3} + 4 + \sqrt{10} \sqrt{\sqrt{5} + 3}}}{4}`, :math:`|PN| = \frac{\sqrt{7} \sqrt{- 5 \sqrt{2} \sqrt{\sqrt{5} + 3} + \sqrt{10} \sqrt{\sqrt{5} + 3} + 12}}{4}`
   * - Rational Trigonometry :term:`Quadrances <quadrance>`
     - :math:`Q(M, P) = \frac{7}{4} + \frac{- 7 \sqrt{2} \sqrt{\sqrt{5} + 3} + 7 \sqrt{10} \sqrt{\sqrt{5} + 3}}{16}`, :math:`Q(P, N) = \frac{- 35 \sqrt{2} \sqrt{\sqrt{5} + 3} + 7 \sqrt{10} \sqrt{\sqrt{5} + 3}}{16} + \frac{21}{4}`, :math:`Q_{\text{long}}/Q_{\text{short}} = \frac{\sqrt{5}}{2} + \frac{3}{2} = \phi^2`
   * - Algebraic Number Field
     - :math:`\mathbb{Q}(\sqrt{5}, \sqrt{7})`
   * - :term:`Géométrographie <geometrographie>` Loci
     - 2 given points · 2 lines · 3 circles · 0 polygons (elementary loci :math:`= 5`, Lemoine :math:`S = 15`)

Automated Divine Scan
---------------------

:mod:`geometor.divine.golden` detected **1** exact collinear golden section(s) and **0** connected golden chain(s) in this model:

- Section (:g:`N`, :g:`P`, :g:`M`): long :math:`|PM|^2 = \frac{7}{4} + \frac{- 7 \sqrt{2} \sqrt{\sqrt{5} + 3} + 7 \sqrt{10} \sqrt{\sqrt{5} + 3}}{16}` vs. short :math:`|NP|^2 = \frac{- 35 \sqrt{2} \sqrt{\sqrt{5} + 3} + 7 \sqrt{10} \sqrt{\sqrt{5} + 3}}{16} + \frac{21}{4}`

Historical Commentary & Attribution
-----------------------------------

Devised by :person:`Bùi Quang Tuân <bui-quang-tuan>` (:cite:`Cut-the-Knot <ctk-bui-5step>`), this five-step construction starts from an arbitrary radius on line :g:`L` rather than a pre-specified unit segment, generating :math:`\phi` inside the biquadratic field :math:`\mathbb{Q}(\sqrt{5}, \sqrt{7})`.

- **Scholarly Citations**: :cite:`Cut-the-Knot: Bùi Quang Tuân's 5-Step Construction of the Golden Ratio <ctk-bui-5step>`, :cite:`Cut-the-Knot: Golden Ratio in Geometry <bogomolny-golden-ratio>`
- **Curated Reference**: `Golden Ratio in Five Steps <https://www.cut-the-knot.org/do_you_know/BuiGoldenRatio5Step.shtml>`_ (curated by :person:`Alexander Bogomolny <alexander-bogomolny>`, *Cut-the-Knot*, © 1996–2018)
- **Concepts**: :term:`Géométrographie <geometrographie>` · :term:`Golden Section <golden-section>` · :term:`Quadrance <quadrance>`

.. toctree::
   :hidden:

   code
