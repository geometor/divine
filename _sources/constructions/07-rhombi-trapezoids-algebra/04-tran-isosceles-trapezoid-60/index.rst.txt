:type: construction
:order: 4
:excerpt: In half-hexagon isosceles trapezoid ABCD (DA = AB = BC and angle C = angle D = 60^circ), reflect B across C to K. Circle cKB centered at K through B cuts diagonal AC internally at M such that CM/MA = CA/CM = φ.
:categories: 07-rhombi-trapezoids-algebra
:tags: field-q-sqrt3-phi, tran-quang-hung

GC-07.04 · Tran Quang Hung's 60° Isosceles Trapezoid Diagonal Division
======================================================================

**Discoverer(s)**: :person:`Tran Quang Hung <tran-quang-hung>` | **Date**: 2015 | **Field**: :math:`\mathbb{Q}(\sqrt{3}, \phi)` | **Loci**: 3 (:term:`Lemoine <geometrographie>` :math:`S = 9`)

.. enunciation::

   In half-hexagon isosceles trapezoid :g:`ABCD` (:math:`|DA| = |AB| = |BC|` and :math:`\angle C = \angle D = 60^\circ`), reflect :g:`B` across :g:`C` to :g:`K`. Circle :g:`cKB` centered at :g:`K` through :g:`B` cuts diagonal :g:`AC` internally at :g:`M` such that :math:`|CM|/|MA| = |CA|/|CM| = \phi`.

.. picture:: 04-tran-isosceles-trapezoid-60.svg
   :alt: GC-07.04 — Tran Quang Hung's 60° Isosceles Trapezoid Diagonal Division

Given & Constructive Steps
--------------------------

**Given**: Half-hexagon trapezoid :g:`ABCD` with base :g:`D` :math:`= (-2,0)` to :g:`C` :math:`= (2,0)` and top :g:`A` :math:`= (-1,\sqrt{3})` to :g:`B` :math:`= (1,\sqrt{3})`.

.. step::

   Extend leg :g:`BC` past :g:`C` by :math:`|CK| = |BC| = 2` to :g:`K` :math:`= (3, -\sqrt{3})`.

.. step::

   Draw diagonal :g:`AC` (of length :math:`2\sqrt{3}`, perpendicular to :g:`DA`).

.. step::

   Draw circle :g:`cKB` of radius :math:`4` centered at :g:`K`, cutting :g:`AC` at :g:`M`.

Exact Symbolic Proof & Certificate
----------------------------------

Vectors :math:`\vec{CA} = (-3, \sqrt{3})` (:math:`|CA| = 2\sqrt{3}`) and :math:`\vec{CK} = (1, -\sqrt{3})` (:math:`|CK| = 2`) satisfy :math:`\vec{CA}\cdot\vec{CK} = -6`, so :math:`\angle ACK = 120^\circ`. Parameterizing :g:`M` on :g:`CA` by :math:`x = |CM|/|CA|`, the Law of Cosines on :math:`\triangle KCM` with :math:`|KM| = 4` gives :math:`12x^2 + 12x + 4 = 16`, i.e. :math:`x^2 + x - 1 = 0`, whence :math:`x = 1/\phi` and :math:`|CM|/|MA| = \phi`.

.. list-table:: Machine-Verified Symbolic Certificate
   :widths: 30 70
   :header-rows: 1

   * - Invariant
     - Exact Symbolic Value
   * - Primary Golden Ratio
     - :g:`CM` :math:`/` :g:`MA` :math:`= \frac{1}{2} + \frac{\sqrt{5}}{2}` on collinear triple (:g:`A`, :g:`M`, :g:`C`)
   * - Exact Segment Lengths
     - :math:`|CM| = - \sqrt{3} + \sqrt{15}`, :math:`|MA| = - \sqrt{15} + 3 \sqrt{3}`
   * - Rational Trigonometry :term:`Quadrances <quadrance>`
     - :math:`Q(C, M) = 18 - 6 \sqrt{5}`, :math:`Q(M, A) = 42 - 18 \sqrt{5}`, :math:`Q_{\text{long}}/Q_{\text{short}} = \frac{\sqrt{5}}{2} + \frac{3}{2} = \phi^2`
   * - Algebraic Number Field
     - :math:`\mathbb{Q}(\sqrt{3}, \phi)`
   * - :term:`Géométrographie <geometrographie>` Loci
     - 2 given points · 2 lines · 1 circles · 1 polygons (elementary loci :math:`= 3`, Lemoine :math:`S = 9`)

Automated Divine Scan
---------------------

:mod:`geometor.divine.golden` detected **1** exact collinear golden section(s) and **0** connected golden chain(s) in this model:

- Section (:g:`A`, :g:`M`, :g:`C`): long :math:`|MC|^2 = 18 - 6 \sqrt{5}` vs. short :math:`|AM|^2 = 42 - 18 \sqrt{5}`

Historical Commentary & Attribution
-----------------------------------

Parallel lines through :g:`M` transfer this golden section simultaneously onto top base :g:`AB` and leg :g:`BC`, inscribing a golden parallelogram inside the half-hexagon.

- **Scholarly Citations**: :cite:`Cut-the-Knot: Golden Ratio in Isosceles Trapezoid <bogomolny-tqh-trapezoid>`, :cite:`Cut-the-Knot: Golden Ratio in Geometry <bogomolny-golden-ratio>`
- **Curated Reference**: `Golden Ratio in Isosceles Trapezoid <https://www.cut-the-knot.org/do_you_know/TQHGoldenRatio.shtml>`_ (curated by :person:`Alexander Bogomolny <alexander-bogomolny>`, *Cut-the-Knot*, © 1996–2018)
- **Concepts**: :term:`Golden Ratio (φ) <golden-ratio>` · :term:`Golden Section <golden-section>` · :term:`Quadrance <quadrance>`

.. toctree::
   :hidden:

   code
