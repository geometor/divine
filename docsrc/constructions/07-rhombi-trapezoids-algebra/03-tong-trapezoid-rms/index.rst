:type: construction
:order: 3
:excerpt: Let ABCD be a trapezoid with parallel bases AD and BC satisfying BC = 3AD. The chord MN parallel to the bases that bisects the area of ABCD divides both non-parallel legs AB and DC in the golden ratio: AM/MB = DN/NC = φ.
:categories: 07-rhombi-trapezoids-algebra
:tags: field-q-phi, jingcheng-tong

GC-07.03 · Jingcheng Tong's Area-Bisecting Chord in a 1:3 Trapezoid
===================================================================

**Discoverer(s)**: :person:`Jingcheng Tong <jingcheng-tong>` | **Date**: 2005 | **Field**: :math:`\mathbb{Q}(\phi)` | **Loci**: 3 (:term:`Lemoine <geometrographie>` :math:`S = 9`)

.. enunciation::

   Let :g:`ABCD` be a trapezoid with parallel bases :g:`AD` and :g:`BC` satisfying :math:`|BC| = 3|AD|`. The chord :g:`MN` parallel to the bases that bisects the area of :g:`ABCD` divides both non-parallel legs :g:`AB` and :g:`DC` in the golden ratio: :math:`|AM|/|MB| = |DN|/|NC| = \phi`.

.. picture:: 03-tong-trapezoid-rms.svg
   :alt: GC-07.03 — Jingcheng Tong's Area-Bisecting Chord in a 1:3 Trapezoid

Given & Constructive Steps
--------------------------

**Given**: Trapezoid :g:`ABCD` with top base :g:`A` :math:`= (-1,2)` to :g:`D` :math:`= (1,2)` (:math:`a = 2`) and bottom base :g:`B` :math:`= (-3,0)` to :g:`C` :math:`= (3,0)` (:math:`b = 6`).

.. step::

   Construct trapezoid :g:`ABCD` with parallel bases of lengths :math:`a = 2` and :math:`b = 6`.

.. step::

   Compute the root-mean-square chord length :math:`c = \sqrt{(a^2 + b^2)/2} = 2\sqrt{5}`.

.. step::

   Draw parallel chord :g:`MN` at height :math:`y = 3 - \sqrt{5}` where horizontal width equals :math:`2\sqrt{5}`.

Exact Symbolic Proof & Certificate
----------------------------------

Any parallel chord of length :math:`c` divides legs :g:`AB` and :g:`DC` in the ratio :math:`|AM|/|MB| = (c - a)/(b - c)`, and bisects the trapezoid's area precisely when :math:`c^2 = (a^2 + b^2)/2`. For :math:`b = 3a`, :math:`c = \sqrt{5}\,a`, giving :math:`|AM|/|MB| = (\sqrt{5} - 1)/(3 - \sqrt{5}) = \phi`—independent of leg slopes or height!

.. list-table:: Machine-Verified Symbolic Certificate
   :widths: 30 70
   :header-rows: 1

   * - Invariant
     - Exact Symbolic Value
   * - Primary Golden Ratio
     - :g:`AM` :math:`/` :g:`MB` :math:`= \frac{1}{2} + \frac{\sqrt{5}}{2}` on collinear triple (:g:`A`, :g:`M`, :g:`B`)
   * - Exact Segment Lengths
     - :math:`|AM| = - \sqrt{2} + \sqrt{10}`, :math:`|MB| = - \sqrt{10} + 3 \sqrt{2}`
   * - Rational Trigonometry :term:`Quadrances <quadrance>`
     - :math:`Q(A, M) = 12 - 4 \sqrt{5}`, :math:`Q(M, B) = 28 - 12 \sqrt{5}`, :math:`Q_{\text{long}}/Q_{\text{short}} = \frac{\sqrt{5}}{2} + \frac{3}{2} = \phi^2`
   * - Algebraic Number Field
     - :math:`\mathbb{Q}(\phi)`
   * - :term:`Géométrographie <geometrographie>` Loci
     - 2 given points · 3 lines · 0 circles · 1 polygons (elementary loci :math:`= 3`, Lemoine :math:`S = 9`)

Automated Divine Scan
---------------------

:mod:`geometor.divine.golden` detected **2** exact collinear golden section(s) and **0** connected golden chain(s) in this model:

- Section (:g:`B`, :g:`M`, :g:`A`): long :math:`|MA|^2 = 12 - 4 \sqrt{5}` vs. short :math:`|BM|^2 = 28 - 12 \sqrt{5}`
- Section (:g:`D`, :g:`N`, :g:`C`): long :math:`|DN|^2 = 12 - 4 \sqrt{5}` vs. short :math:`|NC|^2 = 28 - 12 \sqrt{5}`

Historical Commentary & Attribution
-----------------------------------

Because area bisection depends only on the base ratio :math:`b/a = 3`, this theorem holds for *every* trapezoid (isosceles or scalene) whose parallel bases stand in ratio :math:`1 : 3`.

- **Scholarly Citations**: :cite:`Cut-the-Knot: Golden Ratio in Geometry <bogomolny-golden-ratio>`
- **Curated Reference**: `Golden Ratio in Geometry — Trapezoid Area Bisector <https://www.cut-the-knot.org/do_you_know/GoldenRatio.shtml>`_ (curated by :person:`Alexander Bogomolny <alexander-bogomolny>`, *Cut-the-Knot*, © 1996–2018)
- **Concepts**: :term:`Golden Ratio (φ) <golden-ratio>` · :term:`Golden Section <golden-section>`

.. toctree::
   :hidden:

   code
