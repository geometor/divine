:type: construction
:order: 6
:excerpt: Given regular hexagon ABCDEF and external square ABHG on side AB, circle cAH centered at A through opposite square corner H cuts hexagon sides EF at I and BC at L in the golden ratio: FI/IE = BL/LC = φ.
:categories: 02-equilateral-hexagon
:tags: field-q-sqrt3-phi, tran-quang-hung

GC-02.06 · Regular Hexagon & External Square Compass Sweep
==========================================================

**Discoverer(s)**: :person:`Tran Quang Hung <tran-quang-hung>` | **Date**: 2014 | **Field**: :math:`\mathbb{Q}(\sqrt{3}, \phi)` | **Loci**: 3 (:term:`Lemoine <geometrographie>` :math:`S = 9`)

.. enunciation::

   Given regular hexagon :g:`ABCDEF` and external square :g:`ABHG` on side :g:`AB`, circle :g:`cAH` centered at :g:`A` through opposite square corner :g:`H` cuts hexagon sides :g:`EF` at :g:`I` and :g:`BC` at :g:`L` in the golden ratio: :math:`|FI|/|IE| = |BL|/|LC| = \phi`.

.. picture:: 06-tran-hexagon-square.svg
   :alt: GC-02.06 — Regular Hexagon & External Square Compass Sweep

Given & Constructive Steps
--------------------------

**Given**: Regular hexagon :g:`ABCDEF` on side :g:`AB` from :g:`A` :math:`= (0, 0)` to :g:`B` :math:`= (2, 0)`.

.. step::

   Construct regular hexagon :g:`ABCDEF` of side :math:`2` above :g:`AB`.

.. step::

   Construct external square :g:`ABHG` of side :math:`2` below :g:`AB` and diagonal :g:`AH` of length :math:`2\sqrt{2}`.

.. step::

   Draw circle :g:`cAH` centered at :g:`A` through :g:`H`, intersecting side :g:`EF` at :g:`I` and side :g:`BC` at :g:`L`.

Exact Symbolic Proof & Certificate
----------------------------------

In :math:`\triangle AFI`, :math:`|AF| = 2`, :math:`\angle AFI = 120^\circ`, and radius :math:`|AI| = |AH| = 2\sqrt{2}`. Letting :math:`t = |FI|`, the Law of Cosines gives :math:`8 = 4 + t^2 - 2(2)t\cos 120^\circ = t^2 + 2t + 4`, so :math:`t^2 + 2t - 4 = 0` and :math:`t = \sqrt{5} - 1 = 2/\phi`. Since side :math:`|FE| = 2`, the remaining segment is :math:`|IE| = 2 - (\sqrt{5} - 1) = 3 - \sqrt{5} = 2/\phi^2`, proving :math:`|FI|/|IE| = \phi`.

.. list-table:: Machine-Verified Symbolic Certificate
   :widths: 30 70
   :header-rows: 1

   * - Invariant
     - Exact Symbolic Value
   * - Primary Golden Ratio
     - :g:`FI` :math:`/` :g:`IE` :math:`= \frac{1}{2} + \frac{\sqrt{5}}{2}` on collinear triple (:g:`F`, :g:`I`, :g:`E`)
   * - Exact Segment Lengths
     - :math:`|FI| = -1 + \sqrt{5}`, :math:`|IE| = 3 - \sqrt{5}`
   * - Rational Trigonometry :term:`Quadrances <quadrance>`
     - :math:`Q(F, I) = 6 - 2 \sqrt{5}`, :math:`Q(I, E) = 14 - 6 \sqrt{5}`, :math:`Q_{\text{long}}/Q_{\text{short}} = \frac{\sqrt{5}}{2} + \frac{3}{2} = \phi^2`
   * - Algebraic Number Field
     - :math:`\mathbb{Q}(\sqrt{3}, \phi)`
   * - :term:`Géométrographie <geometrographie>` Loci
     - 2 given points · 2 lines · 1 circles · 2 polygons (elementary loci :math:`= 3`, Lemoine :math:`S = 9`)

Automated Divine Scan
---------------------

:mod:`geometor.divine.golden` detected **2** exact collinear golden section(s) and **0** connected golden chain(s) in this model:

- Section (:g:`F`, :g:`I`, :g:`E`): long :math:`|FI|^2 = 6 - 2 \sqrt{5}` vs. short :math:`|IE|^2 = 14 - 6 \sqrt{5}`
- Section (:g:`B`, :g:`L`, :g:`C`): long :math:`|BL|^2 = 6 - 2 \sqrt{5}` vs. short :math:`|LC|^2 = 14 - 6 \sqrt{5}`

Historical Commentary & Attribution
-----------------------------------

Notice the structural duality between :person:`Tran Quang Hung <tran-quang-hung>`'s hexagon construction (:cite:`Cut-the-Knot <ctk-buratino3>`) and :person:`Michel Bataille <michel-bataille>`'s equilateral triangle construction: replacing the :math:`60^\circ` interior angle with the hexagon's :math:`120^\circ` angle flips :math:`t^2 - 2t - 4 = 0` to :math:`t^2 + 2t - 4 = 0`, bringing the intersection **inside** side :g:`EF`.

- **Scholarly Citations**: :cite:`Cut-the-Knot: Golden Ratio in Regular Hexagon and Square <ctk-buratino3>`, :cite:`Cut-the-Knot: Golden Ratio in Geometry <bogomolny-golden-ratio>`
- **Curated Reference**: `Golden Ratio in Hexagon <https://www.cut-the-knot.org/do_you_know/Buratino3.shtml>`_ (curated by :person:`Alexander Bogomolny <alexander-bogomolny>`, *Cut-the-Knot*, © 1996–2018)
- **Concepts**: :term:`Golden Section <golden-section>` · :term:`Quadrance <quadrance>`

.. toctree::
   :hidden:

   code
