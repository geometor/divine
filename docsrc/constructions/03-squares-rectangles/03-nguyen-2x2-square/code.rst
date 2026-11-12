GC-03.03 · Symbolic Model & Source
==================================

Companion symbolic Python construction for :doc:`index` (``GC-03.03``).

Programmatic Usage
------------------

.. code-block:: python

   from geometor.divine.catalog import build_construction

   model, cert = build_construction("GC-03.03")
   assert cert.ratio_expr == sp.GoldenRatio

Exact Builder Implementation
----------------------------

.. code-block:: python

   def build_nguyen_2x2_square() -> ConstructionResult:
       """Nguyen Thanh Dung's 2x2 square grid compass arc construction."""
       m = new_catalog_model("nguyen-2x2-square")
       P1 = m.set_point(-1, 1, ID="P1")
       P2 = m.set_point(1, 1, ID="P2")
       P3 = m.set_point(1, -1, ID="P3")
       P4 = m.set_point(-1, -1, ID="P4")

       A = m.set_point(-1, 0, classes=["given"], ID="A")
       O = m.set_point(0, 0, ID="O")
       B = m.set_point(1, 0, classes=["given"], ID="B")
       D = m.set_point(0, 1, ID="D")
       E = m.set_point(0, -1, ID="E")
       C = m.set_point(2, 0, ID="C")

       m.construct_polygon([P1, P2, P3, P4], ID="P1P2P3P4")
       ln_ab = m.construct_line(A, B, classes=["golden"], ID="AB")
       m.construct_segment(D, E, classes=["auxiliary"], ID="DE")
       m.construct_segment(C, D, classes=["auxiliary"], ID="CD")
       _ = O

       c_cd = m.construct_circle(C, D, classes=["golden"], ID="cCD")
       m.intersect(c_cd, ln_ab, between=(A, B), classes=["golden"], ID="M")

       return make_result(m, ("M", "B"), ("A", "M"), ("A", "M", "B"))

Exact Symbolic Point Coordinates
--------------------------------

All points in ``nguyen-2x2-square`` are certified free of floating-point approximations over :math:`\mathbb{Q}(\phi)`:

.. list-table::
   :widths: 15 42 43
   :header-rows: 1

   * - Point
     - Exact :math:`x`
     - Exact :math:`y`
   * - ``P1``
     - :math:`-1`
     - :math:`1`
   * - ``P2``
     - :math:`1`
     - :math:`1`
   * - ``P3``
     - :math:`1`
     - :math:`-1`
   * - ``P4``
     - :math:`-1`
     - :math:`-1`
   * - ``A``
     - :math:`-1`
     - :math:`0`
   * - ``O``
     - :math:`0`
     - :math:`0`
   * - ``B``
     - :math:`1`
     - :math:`0`
   * - ``D``
     - :math:`0`
     - :math:`1`
   * - ``E``
     - :math:`0`
     - :math:`-1`
   * - ``C``
     - :math:`2`
     - :math:`0`
   * - ``M``
     - :math:`2 - \sqrt{5}`
     - :math:`0`

**Certified Golden Ratio**: ``MB`` / ``AM`` = ``GoldenRatio``.
