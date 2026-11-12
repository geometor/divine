GC-03.07 · Symbolic Model & Source
==================================

Companion symbolic Python construction for :doc:`index` (``GC-03.07``).

Programmatic Usage
------------------

.. code-block:: python

   from geometor.divine.catalog import build_construction

   model, cert = build_construction("GC-03.07")
   assert cert.ratio_expr == sp.GoldenRatio

Exact Builder Implementation
----------------------------

.. code-block:: python

   def build_bui_cross_and_square() -> ConstructionResult:
       """Bùi Quang Tuân & Alexandre Borovik's Greek cross and square in a circle."""
       m = new_catalog_model("bui-cross-and-square")
       s5 = sp.sqrt(5)

       O = m.set_point(0, 0, classes=["given"], ID="O")
       A = m.set_point(1, 3, classes=["given"], ID="A")
       m.construct_circle(O, A, classes=["primary"], ID="cO")

       # Greek cross of five 2x2 squares inscribed in cO (radius sqrt(10))
       X1 = m.set_point(-1, 3, ID="X1")
       C = m.set_point(1, 1, ID="C")
       X2 = m.set_point(3, 1, ID="X2")
       X3 = m.set_point(3, -1, ID="X3")
       D = m.set_point(1, -1, ID="D")
       X4 = m.set_point(1, -3, ID="X4")
       X5 = m.set_point(-1, -3, ID="X5")
       X6 = m.set_point(-1, -1, ID="X6")
       X7 = m.set_point(-3, -1, ID="X7")
       X8 = m.set_point(-3, 1, ID="X8")
       X9 = m.set_point(-1, 1, ID="X9")
       m.construct_polygon([X1, A, C, X2, X3, D, X4, X5, X6, X7, X8, X9], ID="CROSS")

       # Inscribed concentric square S1 S2 S3 S4 of side 2*sqrt(5)
       S1 = m.set_point(-s5, s5, ID="S1")
       S2 = m.set_point(s5, s5, ID="S2")
       S3 = m.set_point(s5, -s5, ID="S3")
       S4 = m.set_point(-s5, -s5, ID="S4")
       m.construct_polygon([S1, S2, S3, S4], classes=["golden"], ID="S1S2S3S4")

       ln_ac = m.construct_line(A, C, classes=["golden"], ID="AC")
       ln_s1s2 = m.construct_line(S1, S2, classes=["auxiliary"], ID="S1S2")
       ln_s4s3 = m.construct_line(S4, S3, classes=["auxiliary"], ID="S4S3")
       m.intersect(ln_ac, ln_s1s2, classes=["golden"], ID="B")
       E = m.intersect(ln_ac, ln_s4s3, classes=["golden"], ID="E")
       _ = E

       return make_result(m, ("B", "C"), ("A", "B"), ("A", "B", "C"))

Exact Symbolic Point Coordinates
--------------------------------

All points in ``bui-cross-and-square`` are certified free of floating-point approximations over :math:`\mathbb{Q}(\phi)`:

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
     - :math:`1`
     - :math:`3`
   * - ``X1``
     - :math:`-1`
     - :math:`3`
   * - ``C``
     - :math:`1`
     - :math:`1`
   * - ``X2``
     - :math:`3`
     - :math:`1`
   * - ``X3``
     - :math:`3`
     - :math:`-1`
   * - ``D``
     - :math:`1`
     - :math:`-1`
   * - ``X4``
     - :math:`1`
     - :math:`-3`
   * - ``X5``
     - :math:`-1`
     - :math:`-3`
   * - ``X6``
     - :math:`-1`
     - :math:`-1`
   * - ``X7``
     - :math:`-3`
     - :math:`-1`
   * - ``X8``
     - :math:`-3`
     - :math:`1`
   * - ``X9``
     - :math:`-1`
     - :math:`1`
   * - ``S1``
     - :math:`- \sqrt{5}`
     - :math:`\sqrt{5}`
   * - ``S2``
     - :math:`\sqrt{5}`
     - :math:`\sqrt{5}`
   * - ``S3``
     - :math:`\sqrt{5}`
     - :math:`- \sqrt{5}`
   * - ``S4``
     - :math:`- \sqrt{5}`
     - :math:`- \sqrt{5}`
   * - ``B``
     - :math:`1`
     - :math:`\sqrt{5}`
   * - ``E``
     - :math:`1`
     - :math:`- \sqrt{5}`

**Certified Golden Ratio**: ``BC`` / ``AB`` = ``GoldenRatio``.
