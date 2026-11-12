:type: construction
:order: 1
:excerpt: In a 3text{-}4text{-}5 right triangle ABC (BC=3, AC=4, AB=5), let the internal bisector of angle ABC meet leg AC at O. Circle cOC centered at O through C intersects line BO at P and Q such that PQ/BP = BQ/PQ = φ.
:categories: 04-right-and-345
:tags: field-q-phi, h-e-huntley, tran-quang-hung

GC-04.01 · H. E. Huntley's Golden Ratio in the 3-4-5 Right Triangle (1970)
==========================================================================

**Discoverer(s)**: :person:`H. E. Huntley <h-e-huntley>`, :person:`Tran Quang Hung <tran-quang-hung>` | **Date**: 1970 | **Field**: :math:`\mathbb{Q}(\phi)` | **Loci**: 2 (:term:`Lemoine <geometrographie>` :math:`S = 6`)

.. enunciation::

   In a :math:`3\text{-}4\text{-}5` right triangle :g:`ABC` (:math:`|BC|=3, |AC|=4, |AB|=5`), let the internal bisector of :math:`\angle ABC` meet leg :g:`AC` at :g:`O`. Circle :g:`cOC` centered at :g:`O` through :g:`C` intersects line :g:`BO` at :g:`P` and :g:`Q` such that :math:`|PQ|/|BP| = |BQ|/|PQ| = \phi`.

.. picture:: 01-huntley-egyptian-345.svg
   :alt: GC-04.01 — H. E. Huntley's Golden Ratio in the 3-4-5 Right Triangle (1970)

Given & Constructive Steps
--------------------------

**Given**: Right triangle :g:`ABC` with right angle at :g:`C` :math:`= (0,0)`, :g:`B` :math:`= (3,0)`, and :g:`A` :math:`= (0,4)`.

.. step::

   Bisect :math:`\angle ABC` to meet leg :g:`AC` at :g:`O` :math:`= (0, \tfrac{3}{2})`.

.. step::

   Draw circle :g:`cOC` of radius :math:`\tfrac{3}{2}` centered at :g:`O` through :g:`C` (tangent to both :g:`BC` at :g:`C` and hypotenuse :g:`AB` at :g:`T`).

.. step::

   Extend bisector :g:`BO` across :g:`cOC` to obtain secant intersections :g:`P` and :g:`Q`.

Exact Symbolic Proof & Certificate
----------------------------------

By the angle-bisector theorem, :math:`|CO|/|OA| = |BC|/|AB| = 3/5`, giving :math:`|CO| = 3/2` and diameter :math:`|PQ| = 3 = |BC|`. By Euclid III.36 (tangent-secant power from :g:`B` to :g:`cOC`), :math:`|BC|^2 = |BP| \cdot |BQ| = |BP|(|BP| + |PQ|)`. Substituting :math:`|BC| = |PQ|` gives :math:`|PQ|^2 = |BP|^2 + |BP|\cdot|PQ|`, whence :math:`|PQ|/|BP| = \phi`.

.. list-table:: Machine-Verified Symbolic Certificate
   :widths: 30 70
   :header-rows: 1

   * - Invariant
     - Exact Symbolic Value
   * - Primary Golden Ratio
     - :g:`PQ` :math:`/` :g:`BP` :math:`= \frac{1}{2} + \frac{\sqrt{5}}{2}` on collinear triple (:g:`B`, :g:`P`, :g:`Q`)
   * - Exact Segment Lengths
     - :math:`|PQ| = 3`, :math:`|BP| = - \frac{3}{2} + \frac{3 \sqrt{5}}{2}`
   * - Rational Trigonometry :term:`Quadrances <quadrance>`
     - :math:`Q(P, Q) = 9`, :math:`Q(B, P) = \frac{27}{2} - \frac{9 \sqrt{5}}{2}`, :math:`Q_{\text{long}}/Q_{\text{short}} = \frac{\sqrt{5}}{2} + \frac{3}{2} = \phi^2`
   * - Algebraic Number Field
     - :math:`\mathbb{Q}(\phi)`
   * - :term:`Géométrographie <geometrographie>` Loci
     - 2 given points · 1 lines · 1 circles · 1 polygons (elementary loci :math:`= 2`, Lemoine :math:`S = 6`)

Automated Divine Scan
---------------------

:mod:`geometor.divine.golden` detected **1** exact collinear golden section(s) and **0** connected golden chain(s) in this model:

- Section (:g:`Q`, :g:`P`, :g:`B`): long :math:`|QP|^2 = 9` vs. short :math:`|PB|^2 = \frac{27}{2} - \frac{9 \sqrt{5}}{2}`

Historical Commentary & Attribution
-----------------------------------

Featured in H. E. Huntley's *The Divine Proportion* (1970), this theorem links the oldest Pythagorean triple :math:`(3,4,5)` directly to extreme and mean ratio.

- **Scholarly Citations**: :cite:`The Divine Proportion: A Study in Mathematical Beauty <huntley-1970>`, :cite:`Cut-the-Knot: Golden Ratio and the Egyptian 3-4-5 Triangle <bogomolny-345>`, :cite:`Cut-the-Knot: Another Golden Ratio in the 3-4-5 Triangle <bogomolny-345-tqh>`
- **Curated Reference**: `Golden Ratio in the 3-4-5 Triangle <https://www.cut-the-knot.org/do_you_know/GoldenRatio345.shtml>`_ (curated by :person:`Alexander Bogomolny <alexander-bogomolny>`, *Cut-the-Knot*, © 1996–2018)
- **Concepts**: :term:`Golden Ratio (φ) <golden-ratio>` · :term:`Golden Section <golden-section>` · :term:`Power of a Point <power-of-a-point>`

.. toctree::
   :hidden:

   code
