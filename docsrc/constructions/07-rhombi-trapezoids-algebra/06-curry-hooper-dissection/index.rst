:type: construction
:order: 6
:excerpt: Replace integer Fibonacci lengths (3, 5, 8, 13) in the 8 times 8 = 64 vs. 5 times 13 = 65 dissection fallacy by exact powers (1, φ, φ^2, φ^3). In rectangle ABCD of width φ^3 and height φ, internal vertices Q = (φ, 1/φ) and P = (φ^2, 1) lie identically on diagonal AC, forming the 4-point golden chain AQ/QP = AP/AQ = φ.
:categories: 07-rhombi-trapezoids-algebra
:tags: field-q-phi, golden-chain, william-hooper, paul-curry

GC-07.06 · Exact φ-Limit Resolution of the Hooper–Curry Fibonacci Dissection
============================================================================

**Discoverer(s)**: :person:`William Hooper <william-hooper>`, :person:`Paul Curry <paul-curry>`, :person:`Alexander Bogomolny <alexander-bogomolny>` | **Date**: 1794 | **Field**: :math:`\mathbb{Q}(\phi)` | **Loci**: 1 (:term:`Lemoine <geometrographie>` :math:`S = 3`)

.. enunciation::

   Replace integer Fibonacci lengths :math:`(3, 5, 8, 13)` in the :math:`8 \times 8 = 64` vs. :math:`5 \times 13 = 65` dissection fallacy by exact powers :math:`(1, \phi, \phi^2, \phi^3)`. In rectangle :g:`ABCD` of width :math:`\phi^3` and height :math:`\phi`, internal vertices :g:`Q` :math:`= (\phi, 1/\phi)` and :g:`P` :math:`= (\phi^2, 1)` lie *identically* on diagonal :g:`AC`, forming the 4-point golden chain :math:`|AQ|/|QP| = |AP|/|AQ| = \phi`.

.. picture:: 06-curry-hooper-dissection.svg
   :alt: GC-07.06 — Exact φ-Limit Resolution of the Hooper–Curry Fibonacci Dissection

Given & Constructive Steps
--------------------------

**Given**: Rectangle :g:`ABCD` with :g:`A` :math:`= (0,0)`, :g:`B` :math:`= (\phi^3, 0)`, :g:`C` :math:`= (\phi^3, \phi)`, and :g:`D` :math:`= (0, \phi)`.

.. step::

   Mark golden cuts :g:`E` :math:`= (\phi^2, 0)` on :g:`AB` and :g:`F` :math:`= (\phi, \phi)` on :g:`DC`.

.. step::

   Erect vertical cuts :g:`EP` of height :math:`1` to :g:`P` :math:`= (\phi^2, 1)` and :g:`FQ` of length :math:`1` to :g:`Q` :math:`= (\phi, 1/\phi)`.

.. step::

   Draw diagonal :g:`AC`, which passes with zero area gap through both :g:`Q` and :g:`P`.

Exact Symbolic Proof & Certificate
----------------------------------

For Fibonacci numbers, Cassini's identity :math:`F_{n-1}F_{n+1} - F_n^2 = (-1)^n` produces a thin parallelogram of area :math:`\pm 1` because slopes :math:`F_{n-2}/F_n` and :math:`F_{n-1}/F_{n+1}` differ slightly. Replacing :math:`F_k` by :math:`\phi^k` gives :math:`\phi \cdot \phi^3 - (\phi^2)^2 = 0` and identical slopes :math:`\text{slope}(A,Q) = (1/\phi)/\phi = 1/\phi^2 = \text{slope}(A,P) = \text{slope}(A,C)`. Along :g:`AC`, abscissas :math:`(0, \phi, \phi^2, \phi^3)` yield :math:`|AQ|/|QP| = \phi / 1 = \phi`.

.. list-table:: Machine-Verified Symbolic Certificate
   :widths: 30 70
   :header-rows: 1

   * - Invariant
     - Exact Symbolic Value
   * - Primary Golden Ratio
     - :g:`AQ` :math:`/` :g:`QP` :math:`= \frac{1}{2} + \frac{\sqrt{5}}{2}` on collinear triple (:g:`A`, :g:`Q`, :g:`P`)
   * - Exact Segment Lengths
     - :math:`|AQ| = \sqrt{3}`, :math:`|QP| = \frac{- \sqrt{3} + \sqrt{15}}{2}`
   * - Rational Trigonometry :term:`Quadrances <quadrance>`
     - :math:`Q(A, Q) = 3`, :math:`Q(Q, P) = \frac{9}{2} - \frac{3 \sqrt{5}}{2}`, :math:`Q_{\text{long}}/Q_{\text{short}} = \frac{\sqrt{5}}{2} + \frac{3}{2} = \phi^2`
   * - Algebraic Number Field
     - :math:`\mathbb{Q}(\phi)`
   * - :term:`Géométrographie <geometrographie>` Loci
     - 2 given points · 1 lines · 0 circles · 3 polygons (elementary loci :math:`= 1`, Lemoine :math:`S = 3`)

Automated Divine Scan
---------------------

:mod:`geometor.divine.golden` detected **8** exact collinear golden section(s) and **1** connected golden chain(s) in this model:

- Section (:g:`A`, :g:`Q`, :g:`P`): long :math:`|AQ|^2 = 3` vs. short :math:`|QP|^2 = \frac{9}{2} - \frac{3 \sqrt{5}}{2}`
- Section (:g:`A`, :g:`Q`, :g:`C`): long :math:`|QC|^2 = \frac{3 \sqrt{5}}{2} + \frac{9}{2}` vs. short :math:`|AQ|^2 = 3`
- Section (:g:`A`, :g:`P`, :g:`C`): long :math:`|AP|^2 = \frac{3 \sqrt{5}}{2} + \frac{9}{2}` vs. short :math:`|PC|^2 = 3`
- Section (:g:`Q`, :g:`P`, :g:`C`): long :math:`|PC|^2 = 3` vs. short :math:`|QP|^2 = \frac{9}{2} - \frac{3 \sqrt{5}}{2}`
- Section (:g:`A`, :g:`E`, :g:`B`): long :math:`|AE|^2 = \frac{3 \sqrt{5}}{2} + \frac{7}{2}` vs. short :math:`|EB|^2 = \frac{\sqrt{5}}{2} + \frac{3}{2}`
- Section (:g:`F`, :g:`P`, :g:`B`): long :math:`|PB|^2 = \frac{\sqrt{5}}{2} + \frac{5}{2}` vs. short :math:`|FP|^2 = \frac{5}{2} - \frac{\sqrt{5}}{2}`
- Section (:g:`D`, :g:`F`, :g:`C`): long :math:`|FC|^2 = \frac{3 \sqrt{5}}{2} + \frac{7}{2}` vs. short :math:`|DF|^2 = \frac{\sqrt{5}}{2} + \frac{3}{2}`
- Section (:g:`D`, :g:`Q`, :g:`E`): long :math:`|DQ|^2 = \frac{\sqrt{5}}{2} + \frac{5}{2}` vs. short :math:`|QE|^2 = \frac{5}{2} - \frac{\sqrt{5}}{2}`

**Connected Golden Chains**:

- Chain (:g:`A` — :g:`Q` — :g:`P` — :g:`C`) spanning 2 overlapping golden sections (progression ``> <``)

Historical Commentary & Attribution
-----------------------------------

First published by William Hooper in *Rational Recreations* (1794) and generalized by magician Paul Curry (1953), the missing-square paradox vanishes solely at the irrational fixed point :math:`\phi`.

- **Scholarly Citations**: :cite:`Rational Recreations <hooper-1794>`, :cite:`Cut-the-Knot: Golden Ratio in Geometry <bogomolny-golden-ratio>`
- **Curated Reference**: `Golden Ratio and the Missing-Square Dissection <https://www.cut-the-knot.org/do_you_know/GoldenRatio.shtml>`_ (curated by :person:`Alexander Bogomolny <alexander-bogomolny>`, *Cut-the-Knot*, © 1996–2018)
- **Concepts**: :term:`Golden Ratio (φ) <golden-ratio>` · :term:`Golden Section <golden-section>` · :term:`Golden Chain <golden-chain>` · :term:`Golden Rectangle <golden-rectangle>`

.. toctree::
   :hidden:

   code
