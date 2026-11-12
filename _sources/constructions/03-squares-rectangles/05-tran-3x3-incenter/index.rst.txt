:type: construction
:order: 5
:excerpt: In a 3 times 3 grid AQ1Q2Q3 on [0,3]^2, let S = (1,1) and T = (2,2) be opposite corners of the central unit cell, and let U = (3,1) and V = (1,3). The incenter P of isosceles triangle AUV divides diagonal ST of the central cell in the golden ratio: PT/SP = φ.
:categories: 03-squares-rectangles
:tags: field-q-sqrt2-phi, golden-chain, tran-quang-hung

GC-03.05 · Tran Quang Hung's 3×3 Grid Incenter Division
=======================================================

**Discoverer(s)**: :person:`Tran Quang Hung <tran-quang-hung>` | **Date**: 2016 | **Field**: :math:`\mathbb{Q}(\sqrt{2}, \phi)` | **Loci**: 2 (:term:`Lemoine <geometrographie>` :math:`S = 6`)

.. enunciation::

   In a :math:`3 \times 3` grid :g:`AQ1Q2Q3` on :math:`[0,3]^2`, let :g:`S` :math:`= (1,1)` and :g:`T` :math:`= (2,2)` be opposite corners of the central unit cell, and let :g:`U` :math:`= (3,1)` and :g:`V` :math:`= (1,3)`. The incenter :g:`P` of isosceles triangle :g:`AUV` divides diagonal :g:`ST` of the central cell in the golden ratio: :math:`|PT|/|SP| = \phi`.

.. picture:: 05-tran-3x3-incenter.svg
   :alt: GC-03.05 — Tran Quang Hung's 3×3 Grid Incenter Division

Given & Constructive Steps
--------------------------

**Given**: Outer :math:`3 \times 3` square :g:`AQ1Q2Q3` with :g:`A` :math:`= (0,0)` and :g:`Q1` :math:`= (3,0)`.

.. step::

   Mark central cell diagonal vertices :g:`S` :math:`= (1,1)` and :g:`T` :math:`= (2,2)` along symmetry axis :g:`AT`.

.. step::

   Form lattice isosceles triangle :g:`AUV` with :g:`U` :math:`= (3,1)` and :g:`V` :math:`= (1,3)` (whose base :g:`UV` has midpoint :g:`T`).

.. step::

   Construct incenter :g:`P` and incircle :g:`cPT` tangent to :g:`UV` at :g:`T`.

Exact Symbolic Proof & Certificate
----------------------------------

Triangle :g:`AUV` has side lengths :math:`|AU| = |AV| = \sqrt{10}` and :math:`|UV| = 2\sqrt{2}`. By the angle-bisector theorem on altitude :g:`AT` (:math:`|AT| = 2\sqrt{2}`), :math:`|PT|/|AP| = (|UV|/2)/|AU| = \sqrt{2}/\sqrt{10} = 1/\sqrt{5}`, so :math:`x_P = 2 \cdot \frac{\sqrt{5}}{\sqrt{5} + 1} = \frac{5 - \sqrt{5}}{2}`. Hence :math:`2 - x_P = \frac{\sqrt{5}-1}{2} = 1/\phi` and :math:`x_P - 1 = \frac{3-\sqrt{5}}{2} = 1/\phi^2`, proving :math:`|PT|/|SP| = \phi`.

.. list-table:: Machine-Verified Symbolic Certificate
   :widths: 30 70
   :header-rows: 1

   * - Invariant
     - Exact Symbolic Value
   * - Primary Golden Ratio
     - :g:`PT` :math:`/` :g:`SP` :math:`= \frac{1}{2} + \frac{\sqrt{5}}{2}` on collinear triple (:g:`S`, :g:`P`, :g:`T`)
   * - Exact Segment Lengths
     - :math:`|PT| = \frac{- \sqrt{2} + \sqrt{10}}{2}`, :math:`|SP| = \frac{- \sqrt{10} + 3 \sqrt{2}}{2}`
   * - Rational Trigonometry :term:`Quadrances <quadrance>`
     - :math:`Q(P, T) = 3 - \sqrt{5}`, :math:`Q(S, P) = 7 - 3 \sqrt{5}`, :math:`Q_{\text{long}}/Q_{\text{short}} = \frac{\sqrt{5}}{2} + \frac{3}{2} = \phi^2`
   * - Algebraic Number Field
     - :math:`\mathbb{Q}(\sqrt{2}, \phi)`
   * - :term:`Géométrographie <geometrographie>` Loci
     - 2 given points · 1 lines · 1 circles · 3 polygons (elementary loci :math:`= 2`, Lemoine :math:`S = 6`)

Automated Divine Scan
---------------------

:mod:`geometor.divine.golden` detected **2** exact collinear golden section(s) and **1** connected golden chain(s) in this model:

- Section (:g:`S`, :g:`P`, :g:`T`): long :math:`|PT|^2 = 3 - \sqrt{5}` vs. short :math:`|SP|^2 = 7 - 3 \sqrt{5}`
- Section (:g:`P`, :g:`T`, :g:`Q2`): long :math:`|TQ2|^2 = 2` vs. short :math:`|PT|^2 = 3 - \sqrt{5}`

**Connected Golden Chains**:

- Chain (:g:`S` — :g:`P` — :g:`T` — :g:`Q2`) spanning 2 overlapping golden sections (progression ``< <``)

Historical Commentary & Attribution
-----------------------------------

Because :g:`T` is simultaneously a grid vertex and the tangency point of incircle :g:`cPT` on base :g:`UV`, the inradius of :math:`\triangle AUV` equals :math:`|PT| = \sqrt{2}/\phi`.

- **Scholarly Citations**: :cite:`Cut-the-Knot: Another Golden Ratio in 3×3 Square <bogomolny-3x3-2>`, :cite:`Cut-the-Knot: Golden Ratio in Geometry <bogomolny-golden-ratio>`
- **Curated Reference**: `Another Golden Ratio in 3x3 Square <https://www.cut-the-knot.org/do_you_know/3x3GoldenRatio2.shtml>`_ (curated by :person:`Alexander Bogomolny <alexander-bogomolny>`, *Cut-the-Knot*, © 1996–2018)
- **Concepts**: :term:`Golden Ratio (φ) <golden-ratio>` · :term:`Golden Section <golden-section>`

.. toctree::
   :hidden:

   code
