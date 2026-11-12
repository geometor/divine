GC-05.03 · Symbolic Model & Source
==================================

Companion symbolic Python construction for :doc:`index` (``GC-05.03``).

Programmatic Usage
------------------

.. code-block:: python

   from geometor.divine.catalog import build_construction

   model, cert = build_construction("GC-05.03")
   assert cert.ratio_expr == sp.GoldenRatio

Exact Builder Implementation
----------------------------

.. code-block:: python

   def build_prasolov_bui_irregular_pentagon() -> ConstructionResult:
       """V. V. Prasolov & Bùi Quang Tuân's equi-area irregular pentagon."""
       m = new_catalog_model("prasolov-bui-irregular-pentagon")
       phi = sp.Rational(1, 2) + sp.sqrt(5) / 2
       inv_phi = phi - 1

       # Sheared non-regular pentagon over Q(phi) whose five corner triangles all have exact area 2
       A = m.set_point(0, 0, classes=["given"], ID="A")
       B = m.set_point(2 * phi, 0, classes=["given"], ID="B")
       C = m.set_point(3 * phi + 1, 2 * inv_phi, ID="C")
       D = m.set_point(2 * phi + 1, 2, ID="D")
       E = m.set_point(inv_phi, 2 * inv_phi, ID="E")

       m.construct_polygon([A, B, C, D, E], ID="ABCDE")

       ln_bd = m.construct_line(B, D, classes=["golden"], ID="BD")
       ln_ce = m.construct_line(C, E, classes=["auxiliary"], ID="CE")
       ln_ac = m.construct_line(A, C, classes=["auxiliary"], ID="AC")
       m.construct_segment(D, A, classes=["auxiliary"], ID="DA")
       m.construct_segment(E, B, classes=["auxiliary"], ID="EB")

       m.intersect(ln_bd, ln_ce, classes=["golden"], ID="M")
       N = m.intersect(ln_bd, ln_ac, classes=["golden"], ID="N")
       _ = N

       return make_result(m, ("B", "M"), ("M", "D"), ("B", "M", "D"))

Exact Symbolic Point Coordinates
--------------------------------

All points in ``prasolov-bui-irregular-pentagon`` are certified free of floating-point approximations over :math:`\mathbb{Q}(\phi)`:

.. list-table::
   :widths: 15 42 43
   :header-rows: 1

   * - Point
     - Exact :math:`x`
     - Exact :math:`y`
   * - ``A``
     - :math:`0`
     - :math:`0`
   * - ``B``
     - :math:`1 + \sqrt{5}`
     - :math:`0`
   * - ``C``
     - :math:`\frac{5}{2} + \frac{3 \sqrt{5}}{2}`
     - :math:`-1 + \sqrt{5}`
   * - ``D``
     - :math:`2 + \sqrt{5}`
     - :math:`2`
   * - ``E``
     - :math:`- \frac{1}{2} + \frac{\sqrt{5}}{2}`
     - :math:`-1 + \sqrt{5}`
   * - ``M``
     - :math:`\frac{1}{2} + \frac{3 \sqrt{5}}{2}`
     - :math:`-1 + \sqrt{5}`
   * - ``N``
     - :math:`\frac{\sqrt{5}}{2} + \frac{5}{2}`
     - :math:`3 - \sqrt{5}`

**Certified Golden Ratio**: ``BM`` / ``MD`` = ``GoldenRatio``.
