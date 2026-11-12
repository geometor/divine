:type: construction
:order: 3
:excerpt: Let M be the midpoint of base BC of equilateral triangle ABC, and erect a second equilateral triangle AMN on altitude AM. Then circle cBA centered at B through A cuts side MN at P in the golden ratio MN/MP = MP/PN = φ.
:categories: 02-equilateral-hexagon
:tags: field-q-sqrt3-phi, bui-quang-tuan

GC-02.03 · Bùi Quang Tuân's Side-and-Altitude Equilateral Triangles
===================================================================

**Discoverer(s)**: :person:`Bùi Quang Tuân <bui-quang-tuan>` | **Date**: 2011 | **Field**: :math:`\mathbb{Q}(\sqrt{3}, \phi)` | **Loci**: 2 (:term:`Lemoine <geometrographie>` :math:`S = 6`)

.. enunciation::

   Let :g:`M` be the midpoint of base :g:`BC` of equilateral triangle :g:`ABC`, and erect a second equilateral triangle :g:`AMN` on altitude :g:`AM`. Then circle :g:`cBA` centered at :g:`B` through :g:`A` cuts side :g:`MN` at :g:`P` in the golden ratio :math:`|MN|/|MP| = |MP|/|PN| = \phi`.

.. picture:: 03-bui-two-equilaterals.svg
   :alt: GC-02.03 — Bùi Quang Tuân's Side-and-Altitude Equilateral Triangles

Given & Constructive Steps
--------------------------

**Given**: Equilateral triangle :g:`ABC` with :g:`B` :math:`= (-1, 0)`, :g:`C` :math:`= (1, 0)`, midpoint :g:`M` :math:`= (0, 0)`, and apex :g:`A` :math:`= (0, \sqrt{3})`.

.. step::

   Construct equilateral triangle :g:`ABC` of side :math:`2` and bisect :g:`BC` at :g:`M`.

.. step::

   On altitude :g:`AM` of length :math:`\sqrt{3}`, construct equilateral triangle :g:`AMN` with :g:`N` :math:`= (\tfrac{3}{2}, \tfrac{\sqrt{3}}{2})`.

.. step::

   Draw circle :g:`cBA` centered at :g:`B` through :g:`A` (radius :math:`2`), cutting :g:`MN` at :g:`P`.

Exact Symbolic Proof & Certificate
----------------------------------

Ray :g:`MN` makes angle :math:`30^\circ` with :math:`MC`, so :math:`\angle BMP = 150^\circ`. Setting :math:`t = |MP|` in :math:`\triangle BMP` with :math:`|BM| = 1` and :math:`|BP| = |BA| = 2` yields :math:`t^2 - 2t\cos 150^\circ + 1 = 4 \implies t^2 + \sqrt{3}\,t - 3 = 0`, whose positive root is :math:`t = \frac{\sqrt{15} - \sqrt{3}}{2} = \frac{\sqrt{3}}{\phi}`. Since :math:`|MN| = \sqrt{3}`, we obtain :math:`|PN| = \sqrt{3} - \sqrt{3}/\phi = \sqrt{3}/\phi^2` and :math:`|MP|/|PN| = \phi`.

.. list-table:: Machine-Verified Symbolic Certificate
   :widths: 30 70
   :header-rows: 1

   * - Invariant
     - Exact Symbolic Value
   * - Primary Golden Ratio
     - :g:`MP` :math:`/` :g:`PN` :math:`= \frac{1}{2} + \frac{\sqrt{5}}{2}` on collinear triple (:g:`M`, :g:`P`, :g:`N`)
   * - Exact Segment Lengths
     - :math:`|MP| = \frac{- \sqrt{3} + \sqrt{15}}{2}`, :math:`|PN| = \frac{- \sqrt{15} + 3 \sqrt{3}}{2}`
   * - Rational Trigonometry :term:`Quadrances <quadrance>`
     - :math:`Q(M, P) = \frac{9}{2} - \frac{3 \sqrt{5}}{2}`, :math:`Q(P, N) = \frac{21}{2} - \frac{9 \sqrt{5}}{2}`, :math:`Q_{\text{long}}/Q_{\text{short}} = \frac{\sqrt{5}}{2} + \frac{3}{2} = \phi^2`
   * - Algebraic Number Field
     - :math:`\mathbb{Q}(\sqrt{3}, \phi)`
   * - :term:`Géométrographie <geometrographie>` Loci
     - 2 given points · 1 lines · 1 circles · 2 polygons (elementary loci :math:`= 2`, Lemoine :math:`S = 6`)

Automated Divine Scan
---------------------

:mod:`geometor.divine.golden` detected **1** exact collinear golden section(s) and **0** connected golden chain(s) in this model:

- Section (:g:`M`, :g:`P`, :g:`N`): long :math:`|MP|^2 = \frac{9}{2} - \frac{3 \sqrt{5}}{2}` vs. short :math:`|PN|^2 = \frac{21}{2} - \frac{9 \sqrt{5}}{2}`

Historical Commentary & Attribution
-----------------------------------

Contributed by :person:`Bùi Quang Tuân <bui-quang-tuan>` (:cite:`Cut-the-Knot <ctk-bui-qtb>`), along with a companion variant (:cite:`Cut-the-Knot II <ctk-bui-qtb2>`), this figure exploits the :math:`150^\circ` cosine identity :math:`x^2 + \sqrt{3}\,x - 3 = 0`.

- **Scholarly Citations**: :cite:`Cut-the-Knot: Golden Section in Two Equilateral Triangles <ctk-bui-qtb>`, :cite:`Cut-the-Knot: Golden Section in Two Equilateral Triangles, II <ctk-bui-qtb2>`
- **Curated Reference**: `Golden Section in Two Equilateral Triangles <https://www.cut-the-knot.org/do_you_know/GoldenQTB.shtml>`_ (curated by :person:`Alexander Bogomolny <alexander-bogomolny>`, *Cut-the-Knot*, © 1996–2018)
- **Concepts**: :term:`Golden Section <golden-section>` · :term:`Quadrance <quadrance>`

.. toctree::
   :hidden:

   code
