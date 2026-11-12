GC-06.02 · Symbolic Model & Source
==================================

Companion symbolic Python construction for :doc:`index` (``GC-06.02``).

Programmatic Usage
------------------

.. code-block:: python

   from geometor.divine.catalog import build_construction

   model, cert = build_construction("GC-06.02")
   assert cert.ratio_expr == sp.GoldenRatio

Exact Builder Implementation
----------------------------

.. code-block:: python

   def build_mcgucken_kalogerakis_equal_circles() -> ConstructionResult:
       """Elliot McGucken & Thanos Kalogerakis's two externally tangent equal circles."""
       m = new_catalog_model("mcgucken-kalogerakis-equal-circles")
       B = m.set_point(0, 0, classes=["given"], ID="B")
       C = m.set_point(1, 0, classes=["given"], ID="C")
       D = m.set_point(2, 0, ID="D")
       F = m.set_point(0, 1, ID="F")
       A = m.set_point(0, -1, ID="A")

       m.construct_circle(B, C, classes=["primary"], ID="cB")
       c_d = m.construct_circle(D, C, classes=["primary"], ID="cD")
       m.construct_segment(A, F, classes=["auxiliary"], ID="AF")
       m.construct_line(B, D, classes=["auxiliary"], ID="BD")

       ln_fd = m.construct_line(F, D, classes=["golden"], ID="FD")
       m.intersect(c_d, ln_fd, between=(F, D), classes=["golden"], ID="H")
       m.intersect(c_d, ln_fd, beyond=(F, D), classes=["golden"], ID="I")

       return make_result(m, ("H", "I"), ("F", "H"), ("F", "H", "I"))

Exact Symbolic Point Coordinates
--------------------------------

All points in ``mcgucken-kalogerakis-equal-circles`` are certified free of floating-point approximations over :math:`\mathbb{Q}(\phi)`:

.. list-table::
   :widths: 15 42 43
   :header-rows: 1

   * - Point
     - Exact :math:`x`
     - Exact :math:`y`
   * - ``B``
     - :math:`0`
     - :math:`0`
   * - ``C``
     - :math:`1`
     - :math:`0`
   * - ``D``
     - :math:`2`
     - :math:`0`
   * - ``F``
     - :math:`0`
     - :math:`1`
   * - ``A``
     - :math:`0`
     - :math:`-1`
   * - ``H``
     - :math:`2 - \frac{2 \sqrt{5}}{5}`
     - :math:`\frac{\sqrt{5}}{5}`
   * - ``I``
     - :math:`\frac{2 \sqrt{5}}{5} + 2`
     - :math:`- \frac{\sqrt{5}}{5}`

**Certified Golden Ratio**: ``HI`` / ``FH`` = ``GoldenRatio``.
