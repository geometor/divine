:type: construction
:order: 7
:excerpt: Inscribe a symmetrical five-square Greek cross CROSS and a concentric axis-aligned square S1S2S3S4 in the same circle cO. Along any inner arm line AC of the cross, the square edge S1S2 cuts AC at B such that BC/AB = φ, while BD/CD = φ.
:categories: 03-squares-rectangles
:tags: field-q-phi, golden-chain, bui-quang-tuan, alexandre-borovik

GC-03.07 · Bùi Quang Tuân & Alexandre Borovik's Greek Cross & Square
====================================================================

**Discoverer(s)**: :person:`Bùi Quang Tuân <bui-quang-tuan>`, :person:`Alexandre Borovik <alexandre-borovik>` | **Date**: 2015 | **Field**: :math:`\mathbb{Q}(\phi)` | **Loci**: 4 (:term:`Lemoine <geometrographie>` :math:`S = 12`)

.. enunciation::

   Inscribe a symmetrical five-square Greek cross :g:`CROSS` and a concentric axis-aligned square :g:`S1S2S3S4` in the same circle :g:`cO`. Along any inner arm line :g:`AC` of the cross, the square edge :g:`S1S2` cuts :g:`AC` at :g:`B` such that :math:`|BC|/|AB| = \phi`, while :math:`|BD|/|CD| = \phi`.

.. picture:: 07-bui-cross-and-square.svg
   :alt: GC-03.07 — Bùi Quang Tuân & Alexandre Borovik's Greek Cross & Square

Given & Constructive Steps
--------------------------

**Given**: Circle :g:`cO` centered at :g:`O` :math:`= (0,0)` through cross corner :g:`A` :math:`= (1,3)` (radius :math:`\sqrt{10}`).

.. step::

   Inscribe the five-square Greek cross :g:`CROSS` of square side :math:`2`, with right upper arm edge passing through :g:`A` :math:`= (1,3)`, :g:`C` :math:`= (1,1)`, and :g:`D` :math:`= (1,-1)`.

.. step::

   Inscribe concentric square :g:`S1S2S3S4` of side :math:`2\sqrt{5}` with vertices :math:`(\pm\sqrt{5}, \pm\sqrt{5})` on :g:`cO`.

.. step::

   Mark :g:`B` :math:`= (1, \sqrt{5})` and :g:`E` :math:`= (1, -\sqrt{5})` where horizontal square edges :g:`S1S2` and :g:`S4S3` meet line :g:`AC`.

Exact Symbolic Proof & Certificate
----------------------------------

Each cross arm has half-width :math:`1` and outer reach :math:`3`, so :math:`R^2 = 1^2 + 3^2 = 10`. An axis-aligned square in the same circle satisfies :math:`x^2 + y^2 = 10` with :math:`|x| = |y| = \sqrt{5}`. On vertical line :math:`x = 1`, points :math:`A(1,3), B(1,\sqrt{5}), C(1,1), D(1,-1)` have :math:`|BC| = \sqrt{5} - 1 = 2/\phi`, :math:`|AB| = 3 - \sqrt{5} = 2/\phi^2`, and :math:`|BD| = \sqrt{5} + 1 = 2\phi`, giving both :math:`|BC|/|AB| = \phi` and :math:`|BD|/|CD| = \phi`.

.. list-table:: Machine-Verified Symbolic Certificate
   :widths: 30 70
   :header-rows: 1

   * - Invariant
     - Exact Symbolic Value
   * - Primary Golden Ratio
     - :g:`BC` :math:`/` :g:`AB` :math:`= \frac{1}{2} + \frac{\sqrt{5}}{2}` on collinear triple (:g:`A`, :g:`B`, :g:`C`)
   * - Exact Segment Lengths
     - :math:`|BC| = -1 + \sqrt{5}`, :math:`|AB| = 3 - \sqrt{5}`
   * - Rational Trigonometry :term:`Quadrances <quadrance>`
     - :math:`Q(B, C) = 6 - 2 \sqrt{5}`, :math:`Q(A, B) = 14 - 6 \sqrt{5}`, :math:`Q_{\text{long}}/Q_{\text{short}} = \frac{\sqrt{5}}{2} + \frac{3}{2} = \phi^2`
   * - Algebraic Number Field
     - :math:`\mathbb{Q}(\phi)`
   * - :term:`Géométrographie <geometrographie>` Loci
     - 2 given points · 3 lines · 1 circles · 2 polygons (elementary loci :math:`= 4`, Lemoine :math:`S = 12`)

Automated Divine Scan
---------------------

:mod:`geometor.divine.golden` detected **10** exact collinear golden section(s) and **3** connected golden chain(s) in this model:

- Section (:g:`X4`, :g:`E`, :g:`D`): long :math:`|ED|^2 = 6 - 2 \sqrt{5}` vs. short :math:`|X4E|^2 = 14 - 6 \sqrt{5}`
- Section (:g:`X4`, :g:`D`, :g:`B`): long :math:`|DB|^2 = 2 \sqrt{5} + 6` vs. short :math:`|X4D|^2 = 4`
- Section (:g:`E`, :g:`D`, :g:`C`): long :math:`|DC|^2 = 4` vs. short :math:`|ED|^2 = 6 - 2 \sqrt{5}`
- Section (:g:`E`, :g:`C`, :g:`A`): long :math:`|EC|^2 = 2 \sqrt{5} + 6` vs. short :math:`|CA|^2 = 4`
- Section (:g:`D`, :g:`C`, :g:`B`): long :math:`|DC|^2 = 4` vs. short :math:`|CB|^2 = 6 - 2 \sqrt{5}`
- Section (:g:`C`, :g:`B`, :g:`A`): long :math:`|CB|^2 = 6 - 2 \sqrt{5}` vs. short :math:`|BA|^2 = 14 - 6 \sqrt{5}`
- Section (:g:`S4`, :g:`X6`, :g:`C`): long :math:`|X6C|^2 = 8` vs. short :math:`|S4X6|^2 = 12 - 4 \sqrt{5}`
- Section (:g:`X6`, :g:`C`, :g:`S2`): long :math:`|X6C|^2 = 8` vs. short :math:`|CS2|^2 = 12 - 4 \sqrt{5}`
- Section (:g:`S1`, :g:`X9`, :g:`D`): long :math:`|X9D|^2 = 8` vs. short :math:`|S1X9|^2 = 12 - 4 \sqrt{5}`
- Section (:g:`X9`, :g:`D`, :g:`S3`): long :math:`|X9D|^2 = 8` vs. short :math:`|DS3|^2 = 12 - 4 \sqrt{5}`

**Connected Golden Chains**:

- Chain (:g:`X4` — :g:`E` — :g:`D` — :g:`C` — :g:`B` — :g:`A`) spanning 4 overlapping golden sections (progression ``< < > >``)
- Chain (:g:`S4` — :g:`X6` — :g:`C` — :g:`S2`) spanning 2 overlapping golden sections (progression ``< >``)
- Chain (:g:`S1` — :g:`X9` — :g:`D` — :g:`S3`) spanning 2 overlapping golden sections (progression ``< >``)

Historical Commentary & Attribution
-----------------------------------

Alexandre Borovik noted that the overlap between the vertical arm of width :math:`2` and segment :g:`BD` of height :math:`2\phi` forms an exact :term:`golden rectangle <golden-rectangle>`.

- **Scholarly Citations**: :cite:`Cut-the-Knot: Golden Cross and Golden Square <bogomolny-golden-cross>`, :cite:`Cut-the-Knot: Golden Ratio in Geometry <bogomolny-golden-ratio>`
- **Curated Reference**: `Golden Cross and Golden Square <https://www.cut-the-knot.org/do_you_know/GoldenCross.shtml>`_ (curated by :person:`Alexander Bogomolny <alexander-bogomolny>`, *Cut-the-Knot*, © 1996–2018)
- **Concepts**: :term:`Golden Ratio (φ) <golden-ratio>` · :term:`Golden Section <golden-section>` · :term:`Golden Chain <golden-chain>` · :term:`Golden Rectangle <golden-rectangle>`

.. toctree::
   :hidden:

   code
