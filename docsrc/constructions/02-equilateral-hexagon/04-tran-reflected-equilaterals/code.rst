GC-02.04 · Symbolic Model & Source
==================================

Companion symbolic Python construction for :doc:`index` (``GC-02.04``).

Programmatic Usage
------------------

.. code-block:: python

   from geometor.divine.catalog import build_construction

   model, cert = build_construction("GC-02.04")
   assert cert.ratio_expr == sp.GoldenRatio

Exact Builder Implementation
----------------------------

.. code-block:: python

   def build_tran_reflected_equilaterals() -> ConstructionResult:
       """Tran Quang Hung's reflected equilateral triangles & midline secant."""
       m = new_catalog_model("tran-reflected-equilaterals")
       s3 = sp.sqrt(3)
       A = m.set_point(-1, 0, classes=["given"], ID="A")
       B = m.set_point(1, 0, classes=["given"], ID="B")
       C = m.set_point(0, s3, ID="C")
       C1 = m.set_point(0, -s3, ID="C1")
       O1 = m.set_point(0, -s3 / 3, ID="O1")

       m.construct_polygon([A, B, C], ID="ABC")
       m.construct_polygon([A, B, C1], ID="ABC1")
       c_abc1 = m.construct_circle(O1, A, classes=["primary"], ID="cO1")

       N = m.set_point(0, 0, ID="N")
       M = m.set_point(sp.Rational(1, 2), s3 / 2, ID="M")
       ln_mn = m.construct_line(M, N, classes=["auxiliary"], ID="MN")
       P = m.intersect(ln_mn, c_abc1, side_of=(A, B, 1), ID="P")

       ln_ap = m.construct_line(A, P, classes=["golden"], ID="AP")
       ln_bc = m.construct_line(B, C, ID="BC")
       m.intersect(ln_ap, ln_bc, classes=["golden"], ID="D")

       return make_result(m, ("C", "D"), ("D", "B"), ("C", "D", "B"))

Exact Symbolic Point Coordinates
--------------------------------

All points in ``tran-reflected-equilaterals`` are certified free of floating-point approximations over :math:`\mathbb{Q}(\sqrt{3}, \phi)`:

.. list-table::
   :widths: 15 42 43
   :header-rows: 1

   * - Point
     - Exact :math:`x`
     - Exact :math:`y`
   * - ``A``
     - :math:`-1`
     - :math:`0`
   * - ``B``
     - :math:`1`
     - :math:`0`
   * - ``C``
     - :math:`0`
     - :math:`\sqrt{3}`
   * - ``C1``
     - :math:`0`
     - :math:`- \sqrt{3}`
   * - ``O1``
     - :math:`0`
     - :math:`- \frac{\sqrt{3}}{3}`
   * - ``N``
     - :math:`0`
     - :math:`0`
   * - ``M``
     - :math:`\frac{1}{2}`
     - :math:`\frac{\sqrt{3}}{2}`
   * - ``P``
     - :math:`- \frac{1}{4} + \frac{\sqrt{5}}{4}`
     - :math:`\frac{- \sqrt{3} + \sqrt{15}}{4}`
   * - ``D``
     - :math:`- \frac{1}{2} + \frac{\sqrt{5}}{2}`
     - :math:`\frac{- \sqrt{15} + 3 \sqrt{3}}{2}`

**Certified Golden Ratio**: ``CD`` / ``DB`` = ``GoldenRatio``.
