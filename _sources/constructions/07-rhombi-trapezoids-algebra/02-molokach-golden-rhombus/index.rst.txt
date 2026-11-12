:type: construction
:order: 2
:excerpt: Stack two 3 times 1 rectangles RECT1 and RECT2 shifted by one unit around center O, draw unit circle cO, and draw the two tangents to cO perpendicular to outer diagonal R1R6. Together with the horizontal outer edges, they bound a golden rhombus ABCD (AC/BD = φ) with T1K/KA = φ.
:categories: 07-rhombi-trapezoids-algebra
:tags: field-q-phi, golden-chain, john-molokach

GC-07.02 · John Molokach's Golden Rhombus from Shifted 1×3 Rectangles
=====================================================================

**Discoverer(s)**: :person:`John Molokach <john-molokach>` | **Date**: 2014 | **Field**: :math:`\mathbb{Q}(\phi)` | **Loci**: 2 (:term:`Lemoine <geometrographie>` :math:`S = 6`)

.. enunciation::

   Stack two :math:`3 \times 1` rectangles :g:`RECT1` and :g:`RECT2` shifted by one unit around center :g:`O`, draw unit circle :g:`cO`, and draw the two tangents to :g:`cO` perpendicular to outer diagonal :g:`R1R6`. Together with the horizontal outer edges, they bound a :term:`golden rhombus <golden-rhombus>` :g:`ABCD` (:math:`|AC|/|BD| = \phi`) with :math:`|T1K|/|KA| = \phi`.

.. picture:: 02-molokach-golden-rhombus.svg
   :alt: GC-07.02 — John Molokach's Golden Rhombus from Shifted 1×3 Rectangles

Given & Constructive Steps
--------------------------

**Given**: Center :g:`O` :math:`= (0,0)` and rectangle corner :g:`K` :math:`= (1,1)` of shifted :math:`3 \times 1` rectangles :g:`RECT1` and :g:`RECT2`.

.. step::

   Place :math:`3 \times 1` rectangles :math:`[-2,1]\times[0,1]` and :math:`[-1,2]\times[-1,0]` and draw unit circle :g:`cO` tangent to :math:`y = \pm 1` at :g:`T1` and :g:`T2`.

.. step::

   Draw long diagonal :g:`R1R6` from :math:`(-2,1)` to :math:`(2,-1)` and erect tangents to :g:`cO` where :g:`R1R6` crosses :g:`cO`.

.. step::

   Intersect the four tangents to obtain golden rhombus :g:`ABCD` with top vertices :g:`B` :math:`= (-1/\phi, 1)` and :g:`A` :math:`= (\phi, 1)`.

Exact Symbolic Proof & Certificate
----------------------------------

Diagonal :g:`R1R6` has direction :math:`(2, -1)`, meeting unit circle :g:`cO` at :math:`\pm(\tfrac{2}{\sqrt{5}}, -\tfrac{1}{\sqrt{5}})`. The tangents there are :math:`2x - y = \pm\sqrt{5}`, which intersect :math:`y = 1` at :math:`x_A = \frac{\sqrt{5}+1}{2} = \phi` and :math:`x_B = -\frac{\sqrt{5}-1}{2} = -1/\phi`. Along :math:`y = 1`, points :math:`B(-1/\phi,1), T1(0,1), K(1,1), A(\phi,1)` form a 4-point golden chain, while :math:`Q(A,C)/Q(B,D) = (4\phi^2 + 4)/(4\phi^{-2} + 4) = \phi^2`.

.. list-table:: Machine-Verified Symbolic Certificate
   :widths: 30 70
   :header-rows: 1

   * - Invariant
     - Exact Symbolic Value
   * - Primary Golden Ratio
     - :g:`T1K` :math:`/` :g:`KA` :math:`= \frac{1}{2} + \frac{\sqrt{5}}{2}` on collinear triple (:g:`T1`, :g:`K`, :g:`A`)
   * - Exact Segment Lengths
     - :math:`|T1K| = 1`, :math:`|KA| = - \frac{1}{2} + \frac{\sqrt{5}}{2}`
   * - Rational Trigonometry :term:`Quadrances <quadrance>`
     - :math:`Q(T1, K) = 1`, :math:`Q(K, A) = \frac{3}{2} - \frac{\sqrt{5}}{2}`, :math:`Q_{\text{long}}/Q_{\text{short}} = \frac{\sqrt{5}}{2} + \frac{3}{2} = \phi^2`
   * - Algebraic Number Field
     - :math:`\mathbb{Q}(\phi)`
   * - :term:`Géométrographie <geometrographie>` Loci
     - 2 given points · 1 lines · 1 circles · 3 polygons (elementary loci :math:`= 2`, Lemoine :math:`S = 6`)

Automated Divine Scan
---------------------

:mod:`geometor.divine.golden` detected **6** exact collinear golden section(s) and **2** connected golden chain(s) in this model:

- Section (:g:`R1`, :g:`B`, :g:`A`): long :math:`|BA|^2 = 5` vs. short :math:`|R1B|^2 = \frac{15}{2} - \frac{5 \sqrt{5}}{2}`
- Section (:g:`B`, :g:`T1`, :g:`K`): long :math:`|T1K|^2 = 1` vs. short :math:`|BT1|^2 = \frac{3}{2} - \frac{\sqrt{5}}{2}`
- Section (:g:`T1`, :g:`K`, :g:`A`): long :math:`|T1K|^2 = 1` vs. short :math:`|KA|^2 = \frac{3}{2} - \frac{\sqrt{5}}{2}`
- Section (:g:`C`, :g:`R7`, :g:`T2`): long :math:`|R7T2|^2 = 1` vs. short :math:`|CR7|^2 = \frac{3}{2} - \frac{\sqrt{5}}{2}`
- Section (:g:`C`, :g:`D`, :g:`R6`): long :math:`|CD|^2 = 5` vs. short :math:`|DR6|^2 = \frac{15}{2} - \frac{5 \sqrt{5}}{2}`
- Section (:g:`R7`, :g:`T2`, :g:`D`): long :math:`|R7T2|^2 = 1` vs. short :math:`|T2D|^2 = \frac{3}{2} - \frac{\sqrt{5}}{2}`

**Connected Golden Chains**:

- Chain (:g:`B` — :g:`T1` — :g:`K` — :g:`A`) spanning 2 overlapping golden sections (progression ``< >``)
- Chain (:g:`C` — :g:`R7` — :g:`T2` — :g:`D`) spanning 2 overlapping golden sections (progression ``< >``)

Historical Commentary & Attribution
-----------------------------------

A golden rhombus is the planar cross-section of Kepler's rhombic triacontahedron; Molokach's construction produces both :math:`\phi`, :math:`1/\phi`, :math:`1/\phi^2`, and the golden rhombus itself in a single stroke.

- **Scholarly Citations**: :cite:`Cut-the-Knot: Golden Ratio via Golden Rhombus <bogomolny-molokach>`, :cite:`Cut-the-Knot: Golden Ratio in Geometry <bogomolny-golden-ratio>`
- **Curated Reference**: `Golden Ratio via Golden Rhombus <https://www.cut-the-knot.org/do_you_know/GoldenRatioMolokach.shtml>`_ (curated by :person:`Alexander Bogomolny <alexander-bogomolny>`, *Cut-the-Knot*, © 1996–2018)
- **Concepts**: :term:`Golden Ratio (φ) <golden-ratio>` · :term:`Golden Section <golden-section>` · :term:`Golden Chain <golden-chain>` · :term:`Golden Rhombus <golden-rhombus>` · :term:`Quadrance <quadrance>`

.. toctree::
   :hidden:

   code
