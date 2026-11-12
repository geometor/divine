GC-07.04 · Symbolic Model & Source
==================================

Companion symbolic Python construction for :doc:`index` (``GC-07.04``).

Programmatic Usage
------------------

.. code-block:: python

   from geometor.divine.catalog import build_construction

   model, cert = build_construction("GC-07.04")
   assert cert.ratio_expr == sp.GoldenRatio

Exact Builder Implementation
----------------------------

.. code-block:: python

   def build_tran_isosceles_trapezoid_60() -> ConstructionResult:
       """Tran Quang Hung's 60-degree half-hexagon trapezoid & reflected compass arc."""
       m = new_catalog_model("tran-isosceles-trapezoid-60")
       s3 = sp.sqrt(3)

       D = m.set_point(-2, 0, classes=["given"], ID="D")
       C = m.set_point(2, 0, classes=["given"], ID="C")
       B = m.set_point(1, s3, ID="B")
       A = m.set_point(-1, s3, ID="A")
       K = m.set_point(3, -s3, ID="K")

       m.construct_polygon([A, B, C, D], ID="ABCD")
       m.construct_line(B, K, classes=["auxiliary"], ID="BK")
       ln_ac = m.construct_line(A, C, classes=["golden"], ID="AC")

       c_kb = m.construct_circle(K, B, classes=["golden"], ID="cKB")
       m.intersect(c_kb, ln_ac, between=(A, C), classes=["golden"], ID="M")

       return make_result(m, ("C", "M"), ("M", "A"), ("A", "M", "C"))

Exact Symbolic Point Coordinates
--------------------------------

All points in ``tran-isosceles-trapezoid-60`` are certified free of floating-point approximations over :math:`\mathbb{Q}(\sqrt{3}, \phi)`:

.. list-table::
   :widths: 15 42 43
   :header-rows: 1

   * - Point
     - Exact :math:`x`
     - Exact :math:`y`
   * - ``D``
     - :math:`-2`
     - :math:`0`
   * - ``C``
     - :math:`2`
     - :math:`0`
   * - ``B``
     - :math:`1`
     - :math:`\sqrt{3}`
   * - ``A``
     - :math:`-1`
     - :math:`\sqrt{3}`
   * - ``K``
     - :math:`3`
     - :math:`- \sqrt{3}`
   * - ``M``
     - :math:`\frac{7}{2} - \frac{3 \sqrt{5}}{2}`
     - :math:`\frac{- \sqrt{3} + \sqrt{15}}{2}`

**Certified Golden Ratio**: ``CM`` / ``MA`` = ``GoldenRatio``.
