:type: construction
:order: 5
:excerpt: Reflect regular pentagon ABCDE across each of its five sides to obtain five surrounding congruent pentagons. Joining the outer lateral vertices across two intervening pentagons (such as chord S1) cuts every side of ABCDE in the golden ratio, dividing AB at G and H in a 4-point golden chain.
:categories: 05-pentagons-polygons
:tags: field-pentagonal, golden-chain, tran-quang-hung

GC-05.05 · Tran Quang Hung's Six-Pentagon Reflection Star
=========================================================

**Discoverer(s)**: :person:`Tran Quang Hung <tran-quang-hung>` | **Date**: 2016 | **Field**: :math:`\mathbb{Q}(\phi, \sqrt{10 - 2\sqrt{5}})` | **Loci**: 3 (:term:`Lemoine <geometrographie>` :math:`S = 9`)

.. enunciation::

   Reflect regular pentagon :g:`ABCDE` across each of its five sides to obtain five surrounding congruent pentagons. Joining the outer lateral vertices across two intervening pentagons (such as chord :g:`S1`) cuts every side of :g:`ABCDE` in the golden ratio, dividing :g:`AB` at :g:`G` and :g:`H` in a 4-point golden chain.

.. picture:: 05-tran-star-six-pentagons.svg
   :alt: GC-05.05 — Tran Quang Hung's Six-Pentagon Reflection Star

Given & Constructive Steps
--------------------------

**Given**: Central regular pentagon :g:`ABCDE` of side :math:`2` on base :g:`A` :math:`= (-1,0)`, :g:`B` :math:`= (1,0)`.

.. step::

   Reflect :g:`ABCDE` across each of its five sides :g:`AB`, :g:`BC`, :g:`CD`, :g:`DE`, :g:`EA`.

.. step::

   Join the outer lateral vertices in the two chiral :math:`\{5/2\}` star polygons (including chord :g:`S1`).

.. step::

   Mark intersections :g:`G` and :g:`H` where the star chords cross side :g:`AB`.

Exact Symbolic Proof & Certificate
----------------------------------

By fivefold dihedral symmetry :math:`D_5`, the two chiral :math:`\{5/2\}` star polygons on the reflected lateral vertices meet side :g:`AB` at mirror-symmetric points :g:`G` and :g:`H`. Using exact reflection across unit-quadrance-scaled sides, chord :g:`S1` meets :math:`y = 0` at :math:`x = \pm(\sqrt{5} - 2)`, partitioning :math:`[-1, 1]` into segments of lengths :math:`2/\phi^2, 2/\phi^3, 2/\phi^2` and proving :math:`|AG|/|GB| = \phi^{\pm 1}`.

.. list-table:: Machine-Verified Symbolic Certificate
   :widths: 30 70
   :header-rows: 1

   * - Invariant
     - Exact Symbolic Value
   * - Primary Golden Ratio
     - :g:`AG` :math:`/` :g:`GB` :math:`= \frac{1}{2} + \frac{\sqrt{5}}{2}` on collinear triple (:g:`A`, :g:`G`, :g:`B`)
   * - Exact Segment Lengths
     - :math:`|AG| = -1 + \sqrt{5}`, :math:`|GB| = 3 - \sqrt{5}`
   * - Rational Trigonometry :term:`Quadrances <quadrance>`
     - :math:`Q(A, G) = 6 - 2 \sqrt{5}`, :math:`Q(G, B) = 14 - 6 \sqrt{5}`, :math:`Q_{\text{long}}/Q_{\text{short}} = \frac{\sqrt{5}}{2} + \frac{3}{2} = \phi^2`
   * - Algebraic Number Field
     - :math:`\mathbb{Q}(\phi, \sqrt{10 - 2\sqrt{5}})`
   * - :term:`Géométrographie <geometrographie>` Loci
     - 2 given points · 3 lines · 0 circles · 6 polygons (elementary loci :math:`= 3`, Lemoine :math:`S = 9`)

Automated Divine Scan
---------------------

:mod:`geometor.divine.golden` detected **13** exact collinear golden section(s) and **5** connected golden chain(s) in this model:

- Section (:g:`A`, :g:`G`, :g:`B`): long :math:`|AG|^2 = 6 - 2 \sqrt{5}` vs. short :math:`|GB|^2 = 14 - 6 \sqrt{5}`
- Section (:g:`R11`, :g:`G`, :g:`R31`): long :math:`|GR31|^2 = 2 \sqrt{5} + 14` vs. short :math:`|R11G|^2 = 16 - 4 \sqrt{5}`
- Section (:g:`R53`, :g:`A`, :g:`C`): long :math:`|AC|^2 = 2 \sqrt{5} + 6` vs. short :math:`|R53A|^2 = 4`
- Section (:g:`A`, :g:`C`, :g:`R31`): long :math:`|AC|^2 = 2 \sqrt{5} + 6` vs. short :math:`|CR31|^2 = 4`
- Section (:g:`R11`, :g:`A`, :g:`D`): long :math:`|AD|^2 = 2 \sqrt{5} + 6` vs. short :math:`|R11A|^2 = 4`
- Section (:g:`A`, :g:`D`, :g:`R33`): long :math:`|AD|^2 = 2 \sqrt{5} + 6` vs. short :math:`|DR33|^2 = 4`
- Section (:g:`R41`, :g:`D`, :g:`B`): long :math:`|DB|^2 = 2 \sqrt{5} + 6` vs. short :math:`|R41D|^2 = 4`
- Section (:g:`D`, :g:`B`, :g:`R13`): long :math:`|DB|^2 = 2 \sqrt{5} + 6` vs. short :math:`|BR13|^2 = 4`
- Section (:g:`R43`, :g:`E`, :g:`B`): long :math:`|EB|^2 = 2 \sqrt{5} + 6` vs. short :math:`|R43E|^2 = 4`
- Section (:g:`E`, :g:`B`, :g:`R21`): long :math:`|EB|^2 = 2 \sqrt{5} + 6` vs. short :math:`|BR21|^2 = 4`
- Section (:g:`R51`, :g:`E`, :g:`C`): long :math:`|EC|^2 = 2 \sqrt{5} + 6` vs. short :math:`|R51E|^2 = 4`
- Section (:g:`E`, :g:`C`, :g:`R23`): long :math:`|EC|^2 = 2 \sqrt{5} + 6` vs. short :math:`|CR23|^2 = 4`
- Section (:g:`R51`, :g:`G`, :g:`R21`): long :math:`|R51G|^2 = 2 \sqrt{5} + 14` vs. short :math:`|GR21|^2 = 16 - 4 \sqrt{5}`

**Connected Golden Chains**:

- Chain (:g:`R53` — :g:`A` — :g:`C` — :g:`R31`) spanning 2 overlapping golden sections (progression ``< >``)
- Chain (:g:`R11` — :g:`A` — :g:`D` — :g:`R33`) spanning 2 overlapping golden sections (progression ``< >``)
- Chain (:g:`R41` — :g:`D` — :g:`B` — :g:`R13`) spanning 2 overlapping golden sections (progression ``< >``)
- Chain (:g:`R43` — :g:`E` — :g:`B` — :g:`R21`) spanning 2 overlapping golden sections (progression ``< >``)
- Chain (:g:`R51` — :g:`E` — :g:`C` — :g:`R23`) spanning 2 overlapping golden sections (progression ``< >``)

Historical Commentary & Attribution
-----------------------------------

Remarkably, at each golden division point :g:`G` and :g:`H` on a side of :g:`ABCDE`, two distinct star chords concur directly on the pentagon edge.

- **Scholarly Citations**: :cite:`Cut-the-Knot: Star, Six Pentagons and Golden Ratio <bogomolny-six-pentagons>`, :cite:`Cut-the-Knot: Golden Ratio in Geometry <bogomolny-golden-ratio>`
- **Curated Reference**: `Star, Six Pentagons and Golden Ratio <https://www.cut-the-knot.org/do_you_know/StarSixPentagonsGoldenRatio.shtml>`_ (curated by :person:`Alexander Bogomolny <alexander-bogomolny>`, *Cut-the-Knot*, © 1996–2018)
- **Concepts**: :term:`Golden Ratio (φ) <golden-ratio>` · :term:`Golden Section <golden-section>` · :term:`Golden Chain <golden-chain>`

.. toctree::
   :hidden:

   code
