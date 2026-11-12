GC-07.03 · Symbolic Model & Source
==================================

Companion symbolic Python construction for :doc:`index` (``GC-07.03``).

Programmatic Usage
------------------

.. code-block:: python

   from geometor.divine.catalog import build_construction

   model, cert = build_construction("GC-07.03")
   assert cert.ratio_expr == sp.GoldenRatio

Exact Builder Implementation
----------------------------

.. code-block:: python

   def build_tong_trapezoid_rms() -> ConstructionResult:
       """Jingcheng Tong's area-bisecting chord in a trapezoid of base ratio 1:3."""
       m = new_catalog_model("tong-trapezoid-rms")
       s5 = sp.sqrt(5)

       A = m.set_point(-1, 2, classes=["given"], ID="A")
       D = m.set_point(1, 2, ID="D")
       B = m.set_point(-3, 0, classes=["given"], ID="B")
       C = m.set_point(3, 0, ID="C")

       m.construct_polygon([A, B, C, D], ID="ABCD")
       ln_ab = m.construct_line(A, B, classes=["golden"], ID="AB")
       ln_cd = m.construct_line(D, C, classes=["auxiliary"], ID="DC")

       # Area-bisecting parallel chord MN of RMS length sqrt((2^2 + 6^2)/2) = 2*sqrt(5) at y = 3 - sqrt(5)
       M = m.set_point(-s5, 3 - s5, classes=["golden"], ID="M")
       N = m.set_point(s5, 3 - s5, classes=["golden"], ID="N")
       _ = (ln_ab, ln_cd)
       m.construct_line(M, N, classes=["golden"], ID="MN")

       return make_result(m, ("A", "M"), ("M", "B"), ("A", "M", "B"))

Exact Symbolic Point Coordinates
--------------------------------

All points in ``tong-trapezoid-rms`` are certified free of floating-point approximations over :math:`\mathbb{Q}(\phi)`:

.. list-table::
   :widths: 15 42 43
   :header-rows: 1

   * - Point
     - Exact :math:`x`
     - Exact :math:`y`
   * - ``A``
     - :math:`-1`
     - :math:`2`
   * - ``D``
     - :math:`1`
     - :math:`2`
   * - ``B``
     - :math:`-3`
     - :math:`0`
   * - ``C``
     - :math:`3`
     - :math:`0`
   * - ``M``
     - :math:`- \sqrt{5}`
     - :math:`3 - \sqrt{5}`
   * - ``N``
     - :math:`\sqrt{5}`
     - :math:`3 - \sqrt{5}`

**Certified Golden Ratio**: ``AM`` / ``MB`` = ``GoldenRatio``.
