:type: construction
:order: 7
:excerpt: Three congruent unit circles cC1, cC0, cC2 stand in a tangent row on diameter AB of enclosing circle cO centered at O, touching AB at T1, O, T2 and touching cO internally. Then cO has radius 2φ and T2 divides OB in the golden ratio: OT2/T2B = φ.
:categories: 06-circles-sangaku
:tags: field-q-phi, golden-chain, alexander-bogomolny

GC-06.07 · Three Tangent Equal Circles Inscribed in a Semicircle
================================================================

**Discoverer(s)**: :person:`Alexander Bogomolny <alexander-bogomolny>` | **Date**: 2010 | **Field**: :math:`\mathbb{Q}(\phi)` | **Loci**: 6 (:term:`Lemoine <geometrographie>` :math:`S = 18`)

.. enunciation::

   Three congruent unit circles :g:`cC1`, :g:`cC0`, :g:`cC2` stand in a tangent row on diameter :g:`AB` of enclosing circle :g:`cO` centered at :g:`O`, touching :g:`AB` at :g:`T1`, :g:`O`, :g:`T2` and touching :g:`cO` internally. Then :g:`cO` has radius :math:`2\phi` and :g:`T2` divides :g:`OB` in the golden ratio: :math:`|OT2|/|T2B| = \phi`.

.. picture:: 07-three-circles-in-semicircle.svg
   :alt: GC-06.07 — Three Tangent Equal Circles Inscribed in a Semicircle

Given & Constructive Steps
--------------------------

**Given**: Origin :g:`O` :math:`= (0,0)` and outer circle base tangency :g:`T2` :math:`= (2,0)`.

.. step::

   Erect three tangent unit circles :g:`cC1`, :g:`cC0`, :g:`cC2` centered at :math:`(-2,1), (0,1), (2,1)` resting on :g:`AB`.

.. step::

   Join :g:`O` to outer center :g:`C2` :math:`= (2,1)` (:math:`|OC2| = \sqrt{5}`) and extend by unit radius :math:`1` to outer tangency :g:`K`.

.. step::

   Draw enclosing circle :g:`cO` of radius :math:`|OK| = \sqrt{5} + 1 = 2\phi`, cutting base line :g:`AB` at :g:`A` and :g:`B`.

Exact Symbolic Proof & Certificate
----------------------------------

Center :g:`C2` :math:`= (2,1)` lies at distance :math:`\sqrt{2^2 + 1^2} = \sqrt{5}` from :g:`O`, so internal tangency of unit circle :g:`cC2` to :g:`cO` gives enclosing radius :math:`R = \sqrt{5} + 1 = 2\phi`. Along radius :g:`OB`, :math:`|OT2| = 2` and :math:`|T2B| = 2\phi - 2 = 2/\phi`, hence :math:`|OT2|/|T2B| = \phi` (and simultaneously along :g:`OK`, :math:`|SK|/|OS| = 2 / (\sqrt{5}-1) = \phi`).

.. list-table:: Machine-Verified Symbolic Certificate
   :widths: 30 70
   :header-rows: 1

   * - Invariant
     - Exact Symbolic Value
   * - Primary Golden Ratio
     - :g:`OT2` :math:`/` :g:`T2B` :math:`= \frac{1}{2} + \frac{\sqrt{5}}{2}` on collinear triple (:g:`O`, :g:`T2`, :g:`B`)
   * - Exact Segment Lengths
     - :math:`|OT2| = 2`, :math:`|T2B| = -1 + \sqrt{5}`
   * - Rational Trigonometry :term:`Quadrances <quadrance>`
     - :math:`Q(O, T2) = 4`, :math:`Q(T2, B) = 6 - 2 \sqrt{5}`, :math:`Q_{\text{long}}/Q_{\text{short}} = \frac{\sqrt{5}}{2} + \frac{3}{2} = \phi^2`
   * - Algebraic Number Field
     - :math:`\mathbb{Q}(\phi)`
   * - :term:`Géométrographie <geometrographie>` Loci
     - 2 given points · 2 lines · 4 circles · 0 polygons (elementary loci :math:`= 6`, Lemoine :math:`S = 18`)

Automated Divine Scan
---------------------

:mod:`geometor.divine.golden` detected **4** exact collinear golden section(s) and **2** connected golden chain(s) in this model:

- Section (:g:`A`, :g:`T1`, :g:`O`): long :math:`|T1O|^2 = 4` vs. short :math:`|AT1|^2 = 6 - 2 \sqrt{5}`
- Section (:g:`A`, :g:`O`, :g:`T2`): long :math:`|AO|^2 = 2 \sqrt{5} + 6` vs. short :math:`|OT2|^2 = 4`
- Section (:g:`T1`, :g:`O`, :g:`B`): long :math:`|OB|^2 = 2 \sqrt{5} + 6` vs. short :math:`|T1O|^2 = 4`
- Section (:g:`O`, :g:`T2`, :g:`B`): long :math:`|OT2|^2 = 4` vs. short :math:`|T2B|^2 = 6 - 2 \sqrt{5}`

**Connected Golden Chains**:

- Chain (:g:`A` — :g:`T1` — :g:`O` — :g:`B`) spanning 2 overlapping golden sections (progression ``< <``)
- Chain (:g:`A` — :g:`O` — :g:`T2` — :g:`B`) spanning 2 overlapping golden sections (progression ``> >``)

Historical Commentary & Attribution
-----------------------------------

In the Japanese *Sangaku* temple-tablet tradition, packing three equal circles inside a semicircle yields :math:`R / r = 2\phi` as the fundamental enclosing ratio.

- **Scholarly Citations**: :cite:`Cut-the-Knot: Golden Ratio in Geometry <bogomolny-golden-ratio>`
- **Curated Reference**: `Golden Ratio in Three Tangent Circles in a Semicircle <https://www.cut-the-knot.org/do_you_know/GoldenRatio.shtml>`_ (curated by :person:`Alexander Bogomolny <alexander-bogomolny>`, *Cut-the-Knot*, © 1996–2018)
- **Concepts**: :term:`Golden Ratio (φ) <golden-ratio>` · :term:`Golden Section <golden-section>`

.. toctree::
   :hidden:

   code
