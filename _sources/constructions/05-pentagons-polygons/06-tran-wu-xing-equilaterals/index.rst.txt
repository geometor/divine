:type: construction
:order: 6
:excerpt: Arrange five congruent equilateral triangles OV1W1 … OV5W5 of unit side with fivefold rotational symmetry around shared vertex O. The pentagram star joining outer vertices V1 … V5 cuts the radial sides of the equilateral triangles in the golden ratio, e.g. chord V2V5 cuts OW1 at F with OF/FW1 = φ.
:categories: 05-pentagons-polygons
:tags: field-pentagonal-hexagonal, tran-quang-hung

GC-05.06 · Tran Quang Hung's Fivefold Wu Xing Equilateral Star
==============================================================

**Discoverer(s)**: :person:`Tran Quang Hung <tran-quang-hung>` | **Date**: 2015 | **Field**: :math:`\mathbb{Q}(\sqrt{3}, \phi, \sqrt{10 - 2\sqrt{5}})` | **Loci**: 2 (:term:`Lemoine <geometrographie>` :math:`S = 6`)

.. enunciation::

   Arrange five congruent equilateral triangles :g:`OV1W1` … :g:`OV5W5` of unit side with fivefold rotational symmetry around shared vertex :g:`O`. The pentagram star joining outer vertices :g:`V1` … :g:`V5` cuts the radial sides of the equilateral triangles in the golden ratio, e.g. chord :g:`V2V5` cuts :g:`OW1` at :g:`F` with :math:`|OF|/|FW1| = \phi`.

.. picture:: 06-tran-wu-xing-equilaterals.svg
   :alt: GC-05.06 — Tran Quang Hung's Fivefold Wu Xing Equilateral Star

Given & Constructive Steps
--------------------------

**Given**: Center :g:`O` :math:`= (0,0)` and leading apex :g:`V1` :math:`= (0,1)` of five :math:`72^\circ`-spaced unit equilateral triangles.

.. step::

   Construct the five :math:`72^\circ`-rotated unit equilateral triangles :g:`OV1W1` … :g:`OV5W5` sharing vertex :g:`O`.

.. step::

   Draw pentagram chord :g:`V2V5` (along with the remaining four chords of star :math:`\{5/2\}`).

.. step::

   Mark intersection :g:`F` of horizontal pentagram chord :g:`V2V5` with equilateral side :g:`OW1`.

Exact Symbolic Proof & Certificate
----------------------------------

Vertices :g:`V2` and :g:`V5` lie at angles :math:`90^\circ \pm 72^\circ`, so chord :g:`V2V5` is horizontal at height :math:`y = \sin 18^\circ = \frac{\sqrt{5}-1}{4} = \frac{1}{2\phi}`. Meanwhile, rotating :g:`V1` :math:`= (0,1)` clockwise by :math:`60^\circ` places :g:`W1` at :math:`(\tfrac{\sqrt{3}}{2}, \tfrac{1}{2})` (:math:`30^\circ` above the horizontal). Hence :g:`OW1` reaches height :math:`y_F = \frac{1}{2\phi}` at distance :math:`|OF| = \frac{y_F}{\sin 30^\circ} = \frac{1}{\phi}`, leaving :math:`|FW1| = 1 - \frac{1}{\phi} = \frac{1}{\phi^2}` and proving :math:`|OF|/|FW1| = \phi`.

.. list-table:: Machine-Verified Symbolic Certificate
   :widths: 30 70
   :header-rows: 1

   * - Invariant
     - Exact Symbolic Value
   * - Primary Golden Ratio
     - :g:`OF` :math:`/` :g:`FW1` :math:`= \frac{1}{2} + \frac{\sqrt{5}}{2}` on collinear triple (:g:`O`, :g:`F`, :g:`W1`)
   * - Exact Segment Lengths
     - :math:`|OF| = - \frac{1}{2} + \frac{\sqrt{5}}{2}`, :math:`|FW1| = \frac{3}{2} - \frac{\sqrt{5}}{2}`
   * - Rational Trigonometry :term:`Quadrances <quadrance>`
     - :math:`Q(O, F) = \frac{3}{2} - \frac{\sqrt{5}}{2}`, :math:`Q(F, W1) = \frac{7}{2} - \frac{3 \sqrt{5}}{2}`, :math:`Q_{\text{long}}/Q_{\text{short}} = \frac{\sqrt{5}}{2} + \frac{3}{2} = \phi^2`
   * - Algebraic Number Field
     - :math:`\mathbb{Q}(\sqrt{3}, \phi, \sqrt{10 - 2\sqrt{5}})`
   * - :term:`Géométrographie <geometrographie>` Loci
     - 2 given points · 2 lines · 0 circles · 5 polygons (elementary loci :math:`= 2`, Lemoine :math:`S = 6`)

Automated Divine Scan
---------------------

:mod:`geometor.divine.golden` detected **1** exact collinear golden section(s) and **0** connected golden chain(s) in this model:

- Section (:g:`O`, :g:`F`, :g:`W1`): long :math:`|OF|^2 = \frac{3}{2} - \frac{\sqrt{5}}{2}` vs. short :math:`|FW1|^2 = \frac{7}{2} - \frac{3 \sqrt{5}}{2}`

Historical Commentary & Attribution
-----------------------------------

This construction fuses :math:`C_5` (:math:`72^\circ`) and :math:`C_3` (:math:`60^\circ`) rotational symmetries: their :math:`12^\circ` phase difference aligns :math:`\sin 18^\circ` with :math:`\cos 60^\circ = 1/2`.

- **Scholarly Citations**: :cite:`Cut-the-Knot: Golden Ratio in Wu Xing <bogomolny-wu-xing>`, :cite:`Cut-the-Knot: Golden Ratio in Geometry <bogomolny-golden-ratio>`
- **Curated Reference**: `Golden Ratio in Wu Xing <https://www.cut-the-knot.org/do_you_know/GoldenRatioInWuXing.shtml>`_ (curated by :person:`Alexander Bogomolny <alexander-bogomolny>`, *Cut-the-Knot*, © 1996–2018)
- **Concepts**: :term:`Golden Ratio (φ) <golden-ratio>` · :term:`Golden Section <golden-section>`

.. toctree::
   :hidden:

   code
