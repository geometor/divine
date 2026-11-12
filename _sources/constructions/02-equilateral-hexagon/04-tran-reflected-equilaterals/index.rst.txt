:type: construction
:order: 4
:excerpt: Reflect equilateral triangle ABC across base AB to ABC_1 with circumcircle cO1. If midpoints M of BC and N of AB are joined to meet cO1 at P, then line AP divides side BC at D in the golden ratio CD/DB = φ.
:categories: 02-equilateral-hexagon
:tags: field-q-sqrt3-phi, tran-quang-hung

GC-02.04 · Tran Quang Hung's Reflected Equilateral Triangles
============================================================

**Discoverer(s)**: :person:`Tran Quang Hung <tran-quang-hung>` | **Date**: 2014 | **Field**: :math:`\mathbb{Q}(\sqrt{3}, \phi)` | **Loci**: 4 (:term:`Lemoine <geometrographie>` :math:`S = 12`)

.. enunciation::

   Reflect equilateral triangle :g:`ABC` across base :g:`AB` to :g:`ABC_1 <ABC1>` with circumcircle :g:`cO1`. If midpoints :g:`M` of :g:`BC` and :g:`N` of :g:`AB` are joined to meet :g:`cO1` at :g:`P`, then line :g:`AP` divides side :g:`BC` at :g:`D` in the golden ratio :math:`|CD|/|DB| = \phi`.

.. picture:: 04-tran-reflected-equilaterals.svg
   :alt: GC-02.04 — Tran Quang Hung's Reflected Equilateral Triangles

Given & Constructive Steps
--------------------------

**Given**: Shared base :g:`AB` from :g:`A` :math:`= (-1, 0)` to :g:`B` :math:`= (1, 0)` with reflected equilateral apices :g:`C` :math:`= (0, \sqrt{3})` and :g:`C_1 <C1>` :math:`= (0, -\sqrt{3})`.

.. step::

   Construct equilateral triangles :g:`ABC` and :g:`ABC_1 <ABC1>`, and circumcircle :g:`cO1` of :g:`ABC_1 <ABC1>` centered at :g:`O_1 <O1>` :math:`= (0, -\tfrac{\sqrt{3}}{3})`.

.. step::

   Join midpoint :g:`M` :math:`= (\tfrac{1}{2}, \tfrac{\sqrt{3}}{2})` of :g:`BC` and midpoint :g:`N` :math:`= (0, 0)` of :g:`AB`, extending ray :g:`MN` to meet :g:`cO1` at :g:`P`.

.. step::

   Draw line :g:`AP` to intersect side :g:`BC` at :g:`D`.

Exact Symbolic Proof & Certificate
----------------------------------

Line :g:`MN` passes through the origin with slope :math:`\sqrt{3}` (:math:`y = \sqrt{3}\,x`). Intersecting with :g:`cO1` :math:`(x^2 + (y + \tfrac{\sqrt{3}}{3})^2 = \tfrac{4}{3})` gives :math:`4x^2 + 2x - 1 = 0`, whose positive root is :math:`x_P = \frac{\sqrt{5} - 1}{4} = \frac{1}{2\phi}` and :math:`y_P = \frac{\sqrt{3}}{2\phi}`, so :math:`|NP| = 1/\phi` along :g:`NM` (of length :math:`1`). Because :g:`MN` is the midline parallel to :g:`AC` and :g:`N` bisects :g:`AB`, projecting :g:`P` from :g:`A` onto :g:`BC` yields :math:`|CD|/|DB| = \phi`.

.. list-table:: Machine-Verified Symbolic Certificate
   :widths: 30 70
   :header-rows: 1

   * - Invariant
     - Exact Symbolic Value
   * - Primary Golden Ratio
     - :g:`CD` :math:`/` :g:`DB` :math:`= \frac{1}{2} + \frac{\sqrt{5}}{2}` on collinear triple (:g:`C`, :g:`D`, :g:`B`)
   * - Exact Segment Lengths
     - :math:`|CD| = -1 + \sqrt{5}`, :math:`|DB| = 3 - \sqrt{5}`
   * - Rational Trigonometry :term:`Quadrances <quadrance>`
     - :math:`Q(C, D) = 6 - 2 \sqrt{5}`, :math:`Q(D, B) = 14 - 6 \sqrt{5}`, :math:`Q_{\text{long}}/Q_{\text{short}} = \frac{\sqrt{5}}{2} + \frac{3}{2} = \phi^2`
   * - Algebraic Number Field
     - :math:`\mathbb{Q}(\sqrt{3}, \phi)`
   * - :term:`Géométrographie <geometrographie>` Loci
     - 2 given points · 3 lines · 1 circles · 2 polygons (elementary loci :math:`= 4`, Lemoine :math:`S = 12`)

Automated Divine Scan
---------------------

:mod:`geometor.divine.golden` detected **2** exact collinear golden section(s) and **0** connected golden chain(s) in this model:

- Section (:g:`N`, :g:`P`, :g:`M`): long :math:`|NP|^2 = \frac{3}{2} - \frac{\sqrt{5}}{2}` vs. short :math:`|PM|^2 = \frac{7}{2} - \frac{3 \sqrt{5}}{2}`
- Section (:g:`C`, :g:`D`, :g:`B`): long :math:`|CD|^2 = 6 - 2 \sqrt{5}` vs. short :math:`|DB|^2 = 14 - 6 \sqrt{5}`

Historical Commentary & Attribution
-----------------------------------

Contributed by :person:`Tran Quang Hung <tran-quang-hung>` (:cite:`Cut-the-Knot <ctk-buratino5>`), this construction produces golden divisions simultaneously along midline :g:`MN` (:math:`|NP|/|MN| = \phi`) and along side :g:`BC` (:math:`|CD|/|DB| = \phi`).

- **Scholarly Citations**: :cite:`Cut-the-Knot: Golden Ratio in Equilateral Triangle and Incircle <ctk-buratino5>`, :cite:`Cut-the-Knot: Golden Ratio in Geometry <bogomolny-golden-ratio>`
- **Curated Reference**: `Golden Ratio in Two Equilateral Triangles <https://www.cut-the-knot.org/do_you_know/Buratino5.shtml>`_ (curated by :person:`Alexander Bogomolny <alexander-bogomolny>`, *Cut-the-Knot*, © 1996–2018)
- **Concepts**: :term:`Golden Section <golden-section>` · :term:`Quadrance <quadrance>`

.. toctree::
   :hidden:

   code
