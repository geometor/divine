:type: construction
:order: 5
:excerpt: Inscribe equilateral triangle FGH in the incircle cIn of equilateral triangle ABC so that extended sides HF, FG, GH pass through vertices A, C, B respectively. Then FH/AF = FG/CF_1 divides each secant in the golden ratio FH/AF = φ.
:categories: 02-equilateral-hexagon
:tags: field-q-sqrt3-phi, tran-quang-hung

GC-02.05 · Nested Equilateral Triangles on the Incircle
=======================================================

**Discoverer(s)**: :person:`Tran Quang Hung <tran-quang-hung>` | **Date**: 2014 | **Field**: :math:`\mathbb{Q}(\sqrt{3}, \phi)` | **Loci**: 4 (:term:`Lemoine <geometrographie>` :math:`S = 12`)

.. enunciation::

   Inscribe equilateral triangle :g:`FGH` in the incircle :g:`cIn` of equilateral triangle :g:`ABC` so that extended sides :g:`HF`, :g:`FG`, :g:`GH` pass through vertices :g:`A`, :g:`C`, :g:`B` respectively. Then :math:`|FH|/|AF| = |FG|/|CF_1|` divides each secant in the golden ratio :math:`|FH|/|AF| = \phi`.

.. picture:: 05-tran-incircle-equilateral.svg
   :alt: GC-02.05 — Nested Equilateral Triangles on the Incircle

Given & Constructive Steps
--------------------------

**Given**: Equilateral triangle :g:`ABC` of circumradius :math:`2` centered at :g:`O` :math:`= (0, 0)` with unit incircle :g:`cIn`.

.. step::

   Construct equilateral triangle :g:`ABC` and its unit incircle :g:`cIn` centered at :g:`O`.

.. step::

   Inscribe equilateral triangle :g:`FGH` of side :math:`\sqrt{3}` in :g:`cIn` such that :g:`F` lies on segment :g:`AH`, :g:`G` on :g:`CF`, and :g:`H` on :g:`BG`.

.. step::

   Draw the three three-fold symmetric secants :g:`AH`, :g:`BG`, and :g:`CF`.

Exact Symbolic Proof & Certificate
----------------------------------

For vertex :g:`A` :math:`= (0, 2)` and unit circle :g:`cIn`, the power of :g:`A` with respect to :g:`cIn` is :math:`|OA|^2 - 1^2 = 4 - 1 = 3`. Along secant :g:`AFH`, any equilateral triangle :g:`FGH` inscribed in :g:`cIn` has side :math:`|FH| = \sqrt{3}`. By the Tangent-Secant / Power-of-a-Point theorem, :math:`|AF| \cdot |AH| = |AF|(|AF| + \sqrt{3}) = 3`. Dividing by :math:`3` gives :math:`(|AF|/\sqrt{3})^2 + (|AF|/\sqrt{3}) - 1 = 0`, so :math:`|AF| = \sqrt{3}/\phi` and :math:`|FH|/|AF| = \phi`.

.. list-table:: Machine-Verified Symbolic Certificate
   :widths: 30 70
   :header-rows: 1

   * - Invariant
     - Exact Symbolic Value
   * - Primary Golden Ratio
     - :g:`FH` :math:`/` :g:`AF` :math:`= \frac{1}{2} + \frac{\sqrt{5}}{2}` on collinear triple (:g:`A`, :g:`F`, :g:`H`)
   * - Exact Segment Lengths
     - :math:`|FH| = \sqrt{3}`, :math:`|AF| = \frac{- \sqrt{3} + \sqrt{15}}{2}`
   * - Rational Trigonometry :term:`Quadrances <quadrance>`
     - :math:`Q(F, H) = 3`, :math:`Q(A, F) = \frac{9}{2} - \frac{3 \sqrt{5}}{2}`, :math:`Q_{\text{long}}/Q_{\text{short}} = \frac{\sqrt{5}}{2} + \frac{3}{2} = \phi^2`
   * - Algebraic Number Field
     - :math:`\mathbb{Q}(\sqrt{3}, \phi)`
   * - :term:`Géométrographie <geometrographie>` Loci
     - 3 given points · 3 lines · 1 circles · 2 polygons (elementary loci :math:`= 4`, Lemoine :math:`S = 12`)

Automated Divine Scan
---------------------

:mod:`geometor.divine.golden` detected **3** exact collinear golden section(s) and **0** connected golden chain(s) in this model:

- Section (:g:`H`, :g:`F`, :g:`A`): long :math:`|HF|^2 = 3` vs. short :math:`|FA|^2 = \frac{9}{2} - \frac{3 \sqrt{5}}{2}`
- Section (:g:`B`, :g:`H`, :g:`G`): long :math:`|HG|^2 = 3` vs. short :math:`|BH|^2 = \frac{9}{2} - \frac{3 \sqrt{5}}{2}`
- Section (:g:`F`, :g:`G`, :g:`C`): long :math:`|FG|^2 = 3` vs. short :math:`|GC|^2 = \frac{9}{2} - \frac{3 \sqrt{5}}{2}`

Historical Commentary & Attribution
-----------------------------------

Discovered by :person:`Tran Quang Hung <tran-quang-hung>` (:cite:`Cut-the-Knot <ctk-buratino2>`), this rotational-pinwheel configuration embeds three simultaneous golden sections with :math:`C_3` symmetry inside :math:`\mathbb{Q}(\sqrt{3}, \phi)`.

- **Scholarly Citations**: :cite:`Cut-the-Knot: Golden Ratio in Reflected Equilateral Triangles <ctk-buratino2>`, :cite:`Cut-the-Knot: Golden Ratio in Geometry <bogomolny-golden-ratio>`
- **Curated Reference**: `Golden Ratio in Equilateral Triangles <https://www.cut-the-knot.org/do_you_know/Buratino2.shtml>`_ (curated by :person:`Alexander Bogomolny <alexander-bogomolny>`, *Cut-the-Knot*, © 1996–2018)
- **Concepts**: :term:`Power of a Point <power-of-a-point>` · :term:`Golden Section <golden-section>`

.. toctree::
   :hidden:

   code
