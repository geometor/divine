:type: construction
:order: 4
:excerpt: In right isosceles triangle ABC with hypotenuse midpoint M and midpoint O of altitude AM, circle cOM cuts OC and OB at D and F. Cevians BD and CF concur on OM at E, dividing OM in the golden ratio: OE/EM = φ.
:categories: 04-right-and-345
:tags: field-q-phi, golden-chain, bui-quang-tuan

GC-04.04 · Bùi Quang Tuân's Van Obel Division in a Right Isosceles Triangle
===========================================================================

**Discoverer(s)**: :person:`Bùi Quang Tuân <bui-quang-tuan>` | **Date**: 2014 | **Field**: :math:`\mathbb{Q}(\phi)` | **Loci**: 6 (:term:`Lemoine <geometrographie>` :math:`S = 18`)

.. enunciation::

   In right isosceles triangle :g:`ABC` with hypotenuse midpoint :g:`M` and midpoint :g:`O` of altitude :g:`AM`, circle :g:`cOM` cuts :g:`OC` and :g:`OB` at :g:`D` and :g:`F`. Cevians :g:`BD` and :g:`CF` concur on :g:`OM` at :g:`E`, dividing :g:`OM` in the golden ratio: :math:`|OE|/|EM| = \phi`.

.. picture:: 04-bui-van-obel-isosceles.svg
   :alt: GC-04.04 — Bùi Quang Tuân's Van Obel Division in a Right Isosceles Triangle

Given & Constructive Steps
--------------------------

**Given**: Right isosceles triangle :g:`ABC` with :g:`B` :math:`= (-2,0)`, :g:`C` :math:`= (2,0)`, :g:`A` :math:`= (0,2)`, midpoint :g:`M` :math:`= (0,0)`, and :g:`O` :math:`= (0,1)`.

.. step::

   Draw circle :g:`cOM` centered at :g:`O` of radius :math:`1` (passing through :g:`A` and :g:`M`).

.. step::

   Join :g:`OC` and :g:`OB` to meet :g:`cOM` internally at :g:`D` and :g:`F`.

.. step::

   Draw cevians :g:`BD` and :g:`CF` meeting on symmetry axis :g:`AM` at :g:`E`.

Exact Symbolic Proof & Certificate
----------------------------------

In triangle :math:`\triangle OBC`, :math:`|OB| = |OC| = \sqrt{5}` and :math:`|OD| = |OF| = 1`, so :g:`D` divides :g:`OC` in ratio :math:`|OD|/|DC| = 1/(\sqrt{5}-1) = \phi/2`, and symmetrically :math:`|OF|/|FB| = \phi/2`. By Van Obel's theorem on :math:`\triangle OBC` with cevians :g:`OM`, :g:`BD`, :g:`CF` concurring at :g:`E`, :math:`|OE|/|EM| = |OD|/|DC| + |OF|/|FB| = \phi/2 + \phi/2 = \phi`.

.. list-table:: Machine-Verified Symbolic Certificate
   :widths: 30 70
   :header-rows: 1

   * - Invariant
     - Exact Symbolic Value
   * - Primary Golden Ratio
     - :g:`OE` :math:`/` :g:`EM` :math:`= \frac{1}{2} + \frac{\sqrt{5}}{2}` on collinear triple (:g:`O`, :g:`E`, :g:`M`)
   * - Exact Segment Lengths
     - :math:`|OE| = - \frac{1}{2} + \frac{\sqrt{5}}{2}`, :math:`|EM| = \frac{3}{2} - \frac{\sqrt{5}}{2}`
   * - Rational Trigonometry :term:`Quadrances <quadrance>`
     - :math:`Q(O, E) = \frac{3}{2} - \frac{\sqrt{5}}{2}`, :math:`Q(E, M) = \frac{7}{2} - \frac{3 \sqrt{5}}{2}`, :math:`Q_{\text{long}}/Q_{\text{short}} = \frac{\sqrt{5}}{2} + \frac{3}{2} = \phi^2`
   * - Algebraic Number Field
     - :math:`\mathbb{Q}(\phi)`
   * - :term:`Géométrographie <geometrographie>` Loci
     - 2 given points · 5 lines · 1 circles · 1 polygons (elementary loci :math:`= 6`, Lemoine :math:`S = 18`)

Automated Divine Scan
---------------------

:mod:`geometor.divine.golden` detected **2** exact collinear golden section(s) and **1** connected golden chain(s) in this model:

- Section (:g:`M`, :g:`E`, :g:`O`): long :math:`|EO|^2 = \frac{3}{2} - \frac{\sqrt{5}}{2}` vs. short :math:`|ME|^2 = \frac{7}{2} - \frac{3 \sqrt{5}}{2}`
- Section (:g:`E`, :g:`O`, :g:`A`): long :math:`|OA|^2 = 1` vs. short :math:`|EO|^2 = \frac{3}{2} - \frac{\sqrt{5}}{2}`

**Connected Golden Chains**:

- Chain (:g:`M` — :g:`E` — :g:`O` — :g:`A`) spanning 2 overlapping golden sections (progression ``< <``)

Historical Commentary & Attribution
-----------------------------------

Notice the elegance of the Van Obel proof: each symmetric side contributes half of :math:`\phi`, summing immediately to :math:`\phi` at the concurrence point :g:`E`.

- **Scholarly Citations**: :cite:`Cut-the-Knot: Golden Ratio in Right Isosceles Triangle <bogomolny-bui-3>`, :cite:`Cut-the-Knot: Golden Ratio in Geometry <bogomolny-golden-ratio>`
- **Curated Reference**: `Golden Ratio in Right Isosceles Triangle <https://www.cut-the-knot.org/do_you_know/BuiGoldenRatio3.shtml>`_ (curated by :person:`Alexander Bogomolny <alexander-bogomolny>`, *Cut-the-Knot*, © 1996–2018)
- **Concepts**: :term:`Golden Ratio (φ) <golden-ratio>` · :term:`Golden Section <golden-section>`

.. toctree::
   :hidden:

   code
