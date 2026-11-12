:type: construction
:order: 1
:excerpt: In unit circle cO on diameter AB, infinitely many rational-abscissa point pairs on opposite semicircles—including C1 = (0,1), D1 = (tfrac{2}{3}, -tfrac{sqrt{5}}{3}) and C2 = (-tfrac{1}{2}, tfrac{sqrt{3}}{2}), D2 = (tfrac{7}{8}, -tfrac{sqrt{15}}{8})—concur on radius OB at the exact golden point M = (1/φ^2, 0) where MB/OM = φ.
:categories: 06-circles-sangaku
:tags: field-q-sqrt3-phi, bui-quang-tuan

GC-06.01 · Bùi Quang Tuân's Infinite Family of Golden Circle Secants
====================================================================

**Discoverer(s)**: :person:`Bùi Quang Tuân <bui-quang-tuan>` | **Date**: 2014 | **Field**: :math:`\mathbb{Q}(\sqrt{3}, \phi)` | **Loci**: 4 (:term:`Lemoine <geometrographie>` :math:`S = 12`)

.. enunciation::

   In unit circle :g:`cO` on diameter :g:`AB`, infinitely many rational-abscissa point pairs on opposite semicircles—including :g:`C1` :math:`= (0,1)`, :g:`D1` :math:`= (\tfrac{2}{3}, -\tfrac{\sqrt{5}}{3})` and :g:`C2` :math:`= (-\tfrac{1}{2}, \tfrac{\sqrt{3}}{2})`, :g:`D2` :math:`= (\tfrac{7}{8}, -\tfrac{\sqrt{15}}{8})`—concur on radius :g:`OB` at the exact golden point :g:`M` :math:`= (1/\phi^2, 0)` where :math:`|MB|/|OM| = \phi`.

.. picture:: 01-bui-circle-droves.svg
   :alt: GC-06.01 — Bùi Quang Tuân's Infinite Family of Golden Circle Secants

Given & Constructive Steps
--------------------------

**Given**: Unit circle :g:`cO` centered at :g:`O` :math:`= (0,0)` with diameter :g:`A` :math:`= (-1,0)` to :g:`B` :math:`= (1,0)`.

.. step::

   Plot upper apex :g:`C1` :math:`= (0,1)` and lower chord point :g:`D1` at abscissa :math:`x = \tfrac{2}{3}` on :g:`cO`.

.. step::

   Plot a second rational-abscissa pair :g:`C2` at :math:`x = -\tfrac{1}{2}` and :g:`D2` at :math:`x = \tfrac{7}{8}` on opposite semicircles.

.. step::

   Draw chords :g:`C1D1` and :g:`C2D2`, which concur on :g:`OB` at :g:`M` :math:`= (\tfrac{3-\sqrt{5}}{2}, 0)`.

Exact Symbolic Proof & Certificate
----------------------------------

For :math:`C(x, \sqrt{1-x^2})` and :math:`D(y, -\sqrt{1-y^2})`, chord :math:`CD` crosses :math:`AB` at :math:`x_M = \frac{x\sqrt{1-y^2} + y\sqrt{1-x^2}}{\sqrt{1-x^2} + \sqrt{1-y^2}}`. Setting :math:`x_M = \frac{3 - \sqrt{5}}{2} = \frac{1}{\phi^2}` yields Bùi Quang Tuân's Diophantine condition :math:`\frac{5(1 - x^2)}{1 - y^2} = \left(\frac{3 - 2y}{1 - 2x}\right)^2`, satisfied simultaneously by :math:`(0, \tfrac{2}{3})`, :math:`(-\tfrac{1}{2}, \tfrac{7}{8})`, and infinitely many rational pairs.

.. list-table:: Machine-Verified Symbolic Certificate
   :widths: 30 70
   :header-rows: 1

   * - Invariant
     - Exact Symbolic Value
   * - Primary Golden Ratio
     - :g:`MB` :math:`/` :g:`OM` :math:`= \frac{1}{2} + \frac{\sqrt{5}}{2}` on collinear triple (:g:`O`, :g:`M`, :g:`B`)
   * - Exact Segment Lengths
     - :math:`|MB| = - \frac{1}{2} + \frac{\sqrt{5}}{2}`, :math:`|OM| = \frac{3}{2} - \frac{\sqrt{5}}{2}`
   * - Rational Trigonometry :term:`Quadrances <quadrance>`
     - :math:`Q(M, B) = \frac{3}{2} - \frac{\sqrt{5}}{2}`, :math:`Q(O, M) = \frac{7}{2} - \frac{3 \sqrt{5}}{2}`, :math:`Q_{\text{long}}/Q_{\text{short}} = \frac{\sqrt{5}}{2} + \frac{3}{2} = \phi^2`
   * - Algebraic Number Field
     - :math:`\mathbb{Q}(\sqrt{3}, \phi)`
   * - :term:`Géométrographie <geometrographie>` Loci
     - 2 given points · 3 lines · 1 circles · 0 polygons (elementary loci :math:`= 4`, Lemoine :math:`S = 12`)

Automated Divine Scan
---------------------

:mod:`geometor.divine.golden` detected **1** exact collinear golden section(s) and **0** connected golden chain(s) in this model:

- Section (:g:`O`, :g:`M`, :g:`B`): long :math:`|MB|^2 = \frac{3}{2} - \frac{\sqrt{5}}{2}` vs. short :math:`|OM|^2 = \frac{7}{2} - \frac{3 \sqrt{5}}{2}`

Historical Commentary & Attribution
-----------------------------------

At :g:`M`, :math:`|OM| = 1/\phi^2` and :math:`|MB| = 1 - 1/\phi^2 = 1/\phi`, so :math:`|MB|/|OM| = |OB|/|MB| = \phi`.

- **Scholarly Citations**: :cite:`Cut-the-Knot: Golden Ratio in Circle — in Droves <bogomolny-bui-general>`, :cite:`Cut-the-Knot: Golden Ratio in Circle <bogomolny-bui-1>`, :cite:`Cut-the-Knot: Golden Ratio in Geometry <bogomolny-golden-ratio>`
- **Curated Reference**: `Golden Ratio in Circle — in Droves <https://www.cut-the-knot.org/do_you_know/BuiGoldenRatioGeneral.shtml>`_ (curated by :person:`Alexander Bogomolny <alexander-bogomolny>`, *Cut-the-Knot*, © 1996–2018)
- **Concepts**: :term:`Golden Ratio (φ) <golden-ratio>` · :term:`Golden Section <golden-section>`

.. toctree::
   :hidden:

   code
