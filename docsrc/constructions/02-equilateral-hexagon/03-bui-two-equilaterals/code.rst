GC-02.03 · Symbolic Model & Source
==================================

Companion symbolic Python construction for :doc:`index` (``GC-02.03``).

Programmatic Usage
------------------

.. code-block:: python

   from geometor.divine.catalog import build_construction

   model, cert = build_construction("GC-02.03")
   assert cert.ratio_expr == sp.GoldenRatio

Exact Builder Implementation
----------------------------

.. code-block:: python

   def build_bui_two_equilaterals() -> ConstructionResult:
       """Bùi Quang Tuân's coupled equilateral triangles on side and altitude."""
       m = new_catalog_model("bui-two-equilaterals")
       s3 = sp.sqrt(3)
       B = m.set_point(-1, 0, classes=["given"], ID="B")
       C = m.set_point(1, 0, classes=["given"], ID="C")
       M = m.set_point(0, 0, ID="M")
       A = m.set_point(0, s3, ID="A")
       N = m.set_point(sp.Rational(3, 2), s3 / 2, ID="N")

       m.construct_polygon([A, B, C], ID="ABC")
       m.construct_polygon([A, M, N], ID="AMN")
       ln_mn = m.construct_line(M, N, classes=["golden"], ID="MN")

       c_ba = m.construct_circle(B, A, classes=["golden"], ID="cBA")
       m.intersect(c_ba, ln_mn, between=(M, N), classes=["golden"], ID="P")

       return make_result(m, ("M", "P"), ("P", "N"), ("M", "P", "N"))

Exact Symbolic Point Coordinates
--------------------------------

All points in ``bui-two-equilaterals`` are certified free of floating-point approximations over :math:`\mathbb{Q}(\sqrt{3}, \phi)`:

.. list-table::
   :widths: 15 42 43
   :header-rows: 1

   * - Point
     - Exact :math:`x`
     - Exact :math:`y`
   * - ``B``
     - :math:`-1`
     - :math:`0`
   * - ``C``
     - :math:`1`
     - :math:`0`
   * - ``M``
     - :math:`0`
     - :math:`0`
   * - ``A``
     - :math:`0`
     - :math:`\sqrt{3}`
   * - ``N``
     - :math:`\frac{3}{2}`
     - :math:`\frac{\sqrt{3}}{2}`
   * - ``P``
     - :math:`- \frac{3}{4} + \frac{3 \sqrt{5}}{4}`
     - :math:`\frac{- \sqrt{3} + \sqrt{15}}{4}`

**Certified Golden Ratio**: ``MP`` / ``PN`` = ``GoldenRatio``.
