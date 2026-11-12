:type: construction
:order: 1
:excerpt: Let ABC be a right isosceles triangle inscribed in a semicircle of cO on diameter AB, and let square DEGF sit on AB with vertices D and E on legs AC and BC. Extending top side DE to meet circle cO at Q and P divides DP in the golden ratio: DE/EP = DP/DE = φ.
:categories: 03-squares-rectangles
:tags: field-q-phi, golden-chain, tran-quang-hung

GC-03.01 · Tran Quang Hung's Square Inscribed in a Right Isosceles Semicircle
=============================================================================

**Discoverer(s)**: :person:`Tran Quang Hung <tran-quang-hung>` | **Date**: 2014 | **Field**: :math:`\mathbb{Q}(\phi)` | **Loci**: 3 (:term:`Lemoine <geometrographie>` :math:`S = 9`)

.. enunciation::

   Let :g:`ABC` be a right isosceles triangle inscribed in a semicircle of :g:`cO` on diameter :g:`AB`, and let square :g:`DEGF` sit on :g:`AB` with vertices :g:`D` and :g:`E` on legs :g:`AC` and :g:`BC`. Extending top side :g:`DE` to meet circle :g:`cO` at :g:`Q` and :g:`P` divides :g:`DP` in the golden ratio: :math:`|DE|/|EP| = |DP|/|DE| = \phi`.

.. picture:: 01-tran-square-inscribed-semicircle.svg
   :alt: GC-03.01 — Tran Quang Hung's Square Inscribed in a Right Isosceles Semicircle

Given & Constructive Steps
--------------------------

**Given**: Circle :g:`cO` centered at :g:`O` :math:`= (0,0)` of radius :math:`3` with diameter :g:`A` :math:`= (-3,0)`, :g:`B` :math:`= (3,0)` and apex :g:`C` :math:`= (0,3)`.

.. step::

   Inscribe right isosceles triangle :g:`ABC` in the upper semicircle on diameter :g:`AB`.

.. step::

   Inscribe square :g:`DEGF` of side :math:`2` with :g:`F` :math:`= (-1,0)`, :g:`G` :math:`= (1,0)` on :g:`AB` and :g:`D` :math:`= (-1,2)`, :g:`E` :math:`= (1,2)` on :g:`AC`, :g:`BC`.

.. step::

   Extend line :g:`DE` horizontally to meet circle :g:`cO` at :g:`Q` :math:`= (-\sqrt{5}, 2)` and :g:`P` :math:`= (\sqrt{5}, 2)`.

Exact Symbolic Proof & Certificate
----------------------------------

At :math:`x = \pm 1`, legs :g:`AC` (:math:`y = x + 3`) and :g:`BC` (:math:`y = -x + 3`) have height :math:`y = 2`, matching the horizontal side :math:`|DE| = 2` of inscribed square :g:`DEGF`. On circle :math:`x^2 + y^2 = 9`, setting :math:`y = 2` yields :math:`x = \pm\sqrt{5}`, so :math:`|EP| = \sqrt{5} - 1 = 2/\phi` and :math:`|DE|/|EP| = 2 / (2/\phi) = \phi`.

.. list-table:: Machine-Verified Symbolic Certificate
   :widths: 30 70
   :header-rows: 1

   * - Invariant
     - Exact Symbolic Value
   * - Primary Golden Ratio
     - :g:`DE` :math:`/` :g:`EP` :math:`= \frac{1}{2} + \frac{\sqrt{5}}{2}` on collinear triple (:g:`D`, :g:`E`, :g:`P`)
   * - Exact Segment Lengths
     - :math:`|DE| = 2`, :math:`|EP| = -1 + \sqrt{5}`
   * - Rational Trigonometry :term:`Quadrances <quadrance>`
     - :math:`Q(D, E) = 4`, :math:`Q(E, P) = 6 - 2 \sqrt{5}`, :math:`Q_{\text{long}}/Q_{\text{short}} = \frac{\sqrt{5}}{2} + \frac{3}{2} = \phi^2`
   * - Algebraic Number Field
     - :math:`\mathbb{Q}(\phi)`
   * - :term:`Géométrographie <geometrographie>` Loci
     - 3 given points · 2 lines · 1 circles · 2 polygons (elementary loci :math:`= 3`, Lemoine :math:`S = 9`)

Automated Divine Scan
---------------------

:mod:`geometor.divine.golden` detected **2** exact collinear golden section(s) and **1** connected golden chain(s) in this model:

- Section (:g:`Q`, :g:`D`, :g:`E`): long :math:`|DE|^2 = 4` vs. short :math:`|QD|^2 = 6 - 2 \sqrt{5}`
- Section (:g:`D`, :g:`E`, :g:`P`): long :math:`|DE|^2 = 4` vs. short :math:`|EP|^2 = 6 - 2 \sqrt{5}`

**Connected Golden Chains**:

- Chain (:g:`Q` — :g:`D` — :g:`E` — :g:`P`) spanning 2 overlapping golden sections (progression ``< >``)

Historical Commentary & Attribution
-----------------------------------

Because :math:`(Q, D, E, P)` is symmetric across the vertical axis, it forms a complete 4-point golden chain with lengths :math:`2/\phi, 2, 2/\phi`.

- **Scholarly Citations**: :cite:`Cut-the-Knot: Golden Ratio in Square and Circle <bogomolny-rectangles>`, :cite:`Cut-the-Knot: Golden Ratio in Geometry <bogomolny-golden-ratio>`
- **Curated Reference**: `Golden Ratio in Square and Circle <https://www.cut-the-knot.org/do_you_know/GoldenRatioInRectangles.shtml>`_ (curated by :person:`Alexander Bogomolny <alexander-bogomolny>`, *Cut-the-Knot*, © 1996–2018)
- **Concepts**: :term:`Golden Ratio (φ) <golden-ratio>` · :term:`Golden Section <golden-section>` · :term:`Golden Chain <golden-chain>` · :term:`Intersecting Chords Theorem <intersecting-chords-theorem>`

.. toctree::
   :hidden:

   code
