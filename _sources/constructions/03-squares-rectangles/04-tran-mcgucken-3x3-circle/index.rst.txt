:type: construction
:order: 4
:excerpt: In a 3 times 3 square grid S1AS3S4 centered at O, let C be the upper-right vertex of the central grid cell, A the outer upper-right corner, and T the adjacent trisection vertex on the top edge. Circle cOT cuts diagonal segment CA at B such that CB/BA = φ.
:categories: 03-squares-rectangles
:tags: field-q-sqrt2-phi, golden-chain, tran-quang-hung, elliot-mcgucken

GC-03.04 · Tran Quang Hung & Elliot McGucken's 3×3 Grid Circle
==============================================================

**Discoverer(s)**: :person:`Tran Quang Hung <tran-quang-hung>`, :person:`Elliot McGucken <elliot-mcgucken>` | **Date**: 2016 | **Field**: :math:`\mathbb{Q}(\sqrt{2}, \phi)` | **Loci**: 2 (:term:`Lemoine <geometrographie>` :math:`S = 6`)

.. enunciation::

   In a :math:`3 \times 3` square grid :g:`S1AS3S4` centered at :g:`O`, let :g:`C` be the upper-right vertex of the central grid cell, :g:`A` the outer upper-right corner, and :g:`T` the adjacent trisection vertex on the top edge. Circle :g:`cOT` cuts diagonal segment :g:`CA` at :g:`B` such that :math:`|CB|/|BA| = \phi`.

.. picture:: 04-tran-mcgucken-3x3-circle.svg
   :alt: GC-03.04 — Tran Quang Hung & Elliot McGucken's 3×3 Grid Circle

Given & Constructive Steps
--------------------------

**Given**: A :math:`3 \times 3` square grid on :math:`[-3, 3]^2` centered at :g:`O` :math:`= (0,0)` with outer vertex :g:`A` :math:`= (3,3)`.

.. step::

   Identify central cell corner :g:`C` :math:`= (1,1)` and top boundary grid node :g:`T` :math:`= (1,3)`.

.. step::

   Draw diagonal line :g:`OA` through :g:`C` and :g:`A`.

.. step::

   Draw circle :g:`cOT` centered at :g:`O` through :g:`T`, cutting segment :g:`CA` at :g:`B`.

Exact Symbolic Proof & Certificate
----------------------------------

Circle :g:`cOT` has quadrance radius :math:`Q(O, T) = 1^2 + 3^2 = 10`. Along diagonal :math:`y = x`, :math:`2x^2 = 10` gives :g:`B` :math:`= (\sqrt{5}, \sqrt{5})`. Since collinear points :math:`C(1,1), B(\sqrt{5},\sqrt{5}), A(3,3)` project linearly onto the :math:`x`-axis, :math:`|CB|/|BA| = (\sqrt{5} - 1)/(3 - \sqrt{5}) = \phi`.

.. list-table:: Machine-Verified Symbolic Certificate
   :widths: 30 70
   :header-rows: 1

   * - Invariant
     - Exact Symbolic Value
   * - Primary Golden Ratio
     - :g:`CB` :math:`/` :g:`BA` :math:`= \frac{1}{2} + \frac{\sqrt{5}}{2}` on collinear triple (:g:`C`, :g:`B`, :g:`A`)
   * - Exact Segment Lengths
     - :math:`|CB| = - \sqrt{2} + \sqrt{10}`, :math:`|BA| = - \sqrt{10} + 3 \sqrt{2}`
   * - Rational Trigonometry :term:`Quadrances <quadrance>`
     - :math:`Q(C, B) = 12 - 4 \sqrt{5}`, :math:`Q(B, A) = 28 - 12 \sqrt{5}`, :math:`Q_{\text{long}}/Q_{\text{short}} = \frac{\sqrt{5}}{2} + \frac{3}{2} = \phi^2`
   * - Algebraic Number Field
     - :math:`\mathbb{Q}(\sqrt{2}, \phi)`
   * - :term:`Géométrographie <geometrographie>` Loci
     - 2 given points · 1 lines · 1 circles · 2 polygons (elementary loci :math:`= 2`, Lemoine :math:`S = 6`)

Automated Divine Scan
---------------------

:mod:`geometor.divine.golden` detected **3** exact collinear golden section(s) and **1** connected golden chain(s) in this model:

- Section (:g:`S4`, :g:`C4`, :g:`B`): long :math:`|C4B|^2 = 4 \sqrt{5} + 12` vs. short :math:`|S4C4|^2 = 8`
- Section (:g:`C4`, :g:`C`, :g:`B`): long :math:`|C4C|^2 = 8` vs. short :math:`|CB|^2 = 12 - 4 \sqrt{5}`
- Section (:g:`C`, :g:`B`, :g:`A`): long :math:`|CB|^2 = 12 - 4 \sqrt{5}` vs. short :math:`|BA|^2 = 28 - 12 \sqrt{5}`

**Connected Golden Chains**:

- Chain (:g:`C4` — :g:`C` — :g:`B` — :g:`A`) spanning 2 overlapping golden sections (progression ``> >``)

Historical Commentary & Attribution
-----------------------------------

Notice the structural kinship with the Greek Cross (:doc:`../07-bui-cross-and-square/index`): the four trisection nodes on the boundary of a :math:`3 \times 3` grid are precisely the twelve outer corners of a five-square Greek cross.

- **Scholarly Citations**: :cite:`Cut-the-Knot: Golden Ratio in 3×3 Square <bogomolny-3x3-1>`, :cite:`Cut-the-Knot: Golden Ratio in Geometry <bogomolny-golden-ratio>`
- **Curated Reference**: `Golden Ratio in 3x3 Square <https://www.cut-the-knot.org/do_you_know/3x3GoldenRatio.shtml>`_ (curated by :person:`Alexander Bogomolny <alexander-bogomolny>`, *Cut-the-Knot*, © 1996–2018)
- **Concepts**: :term:`Golden Ratio (φ) <golden-ratio>` · :term:`Golden Section <golden-section>` · :term:`Quadrance <quadrance>`

.. toctree::
   :hidden:

   code
