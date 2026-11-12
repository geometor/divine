GC-06.04 · Symbolic Model & Source
==================================

Companion symbolic Python construction for :doc:`index` (``GC-06.04``).

Programmatic Usage
------------------

.. code-block:: python

   from geometor.divine.catalog import build_construction

   model, cert = build_construction("GC-06.04")
   assert cert.ratio_expr == sp.GoldenRatio

Exact Builder Implementation
----------------------------

.. code-block:: python

   def build_tran_mcgucken_three_tangent_circles() -> ConstructionResult:
       """Tran Quang Hung & Elliot McGucken's three mutually tangent equal circles."""
       m = new_catalog_model("tran-mcgucken-three-tangent-circles")
       s3 = sp.sqrt(3)

       O = m.set_point(0, 0, classes=["given"], ID="O")
       A = m.set_point(0, 2 * s3 / 3, classes=["given"], ID="A")
       B = m.set_point(-1, -s3 / 3, ID="B")
       C = m.set_point(1, -s3 / 3, ID="C")

       D = m.set_point(0, -s3 / 3, classes=["golden"], ID="D")
       E = m.set_point(sp.Rational(1, 2), s3 / 6, ID="E")
       F = m.set_point(-sp.Rational(1, 2), s3 / 6, classes=["golden"], ID="F")
       _ = E

       m.construct_polygon([A, B, C], classes=["auxiliary"], ID="ABC")
       m.construct_circle(A, F, classes=["compass"], ID="cA")
       m.construct_circle(B, D, classes=["compass"], ID="cB")
       m.construct_circle(C, D, classes=["compass"], ID="cC")
       c_o = m.construct_circle(O, A, classes=["primary"], ID="cO")

       ln_df = m.construct_line(D, F, classes=["golden"], ID="DF")
       m.intersect(c_o, ln_df, beyond=(D, F), classes=["golden"], ID="G")
       J = m.intersect(c_o, ln_df, beyond=(F, D), classes=["golden"], ID="J")
       _ = J

       return make_result(m, ("D", "F"), ("F", "G"), ("D", "F", "G"))

Exact Symbolic Point Coordinates
--------------------------------

All points in ``tran-mcgucken-three-tangent-circles`` are certified free of floating-point approximations over :math:`\mathbb{Q}(\sqrt{3}, \phi)`:

.. list-table::
   :widths: 15 42 43
   :header-rows: 1

   * - Point
     - Exact :math:`x`
     - Exact :math:`y`
   * - ``O``
     - :math:`0`
     - :math:`0`
   * - ``A``
     - :math:`0`
     - :math:`\frac{2 \sqrt{3}}{3}`
   * - ``B``
     - :math:`-1`
     - :math:`- \frac{\sqrt{3}}{3}`
   * - ``C``
     - :math:`1`
     - :math:`- \frac{\sqrt{3}}{3}`
   * - ``D``
     - :math:`0`
     - :math:`- \frac{\sqrt{3}}{3}`
   * - ``E``
     - :math:`\frac{1}{2}`
     - :math:`\frac{\sqrt{3}}{6}`
   * - ``F``
     - :math:`- \frac{1}{2}`
     - :math:`\frac{\sqrt{3}}{6}`
   * - ``G``
     - :math:`- \frac{\sqrt{5}}{4} - \frac{1}{4}`
     - :math:`\frac{- \sqrt{3} + 3 \sqrt{15}}{12}`
   * - ``J``
     - :math:`- \frac{1}{4} + \frac{\sqrt{5}}{4}`
     - :math:`\frac{- 3 \sqrt{15} - \sqrt{3}}{12}`

**Certified Golden Ratio**: ``DF`` / ``FG`` = ``GoldenRatio``.
