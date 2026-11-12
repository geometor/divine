GC-01.07 · Symbolic Model & Source
==================================

Companion symbolic Python construction for :doc:`index` (``GC-01.07``).

Programmatic Usage
------------------

.. code-block:: python

   from geometor.divine.catalog import build_construction

   model, cert = build_construction("GC-01.07")
   assert cert.ratio_expr == sp.GoldenRatio

Exact Builder Implementation
----------------------------

.. code-block:: python

   def build_bui_5step() -> ConstructionResult:
       """Bùi Quang Tuân's 5-step collinear three-circle secant construction."""
       m = new_catalog_model("bui-5step")
       O = m.set_point(0, 0, classes=["given"], ID="O")
       B = m.set_point(-1, 0, classes=["given"], ID="B")

       # 1. Line L, 2. Circle O(B), 3. Circle B(A), 4. Circle C(O), 5. Line MN
       ln_l = m.construct_line(O, B, ID="L")
       c_o = m.construct_circle(O, B, classes=["primary"], ID="cO")
       A = m.intersect(c_o, ln_l, other_than=B, ID="A")

       c_ba = m.construct_circle(B, A, classes=["compass"], ID="cBA")
       C = m.intersect(c_ba, ln_l, other_than=A, ID="C")

       c_co = m.construct_circle(C, O, classes=["compass"], ID="cCO")
       M = m.intersect(c_co, c_o, side_of=(O, A, 1), ID="M")
       N = m.intersect(c_co, c_ba, side_of=(O, A, -1), ID="N")

       ln_mn = m.construct_line(M, N, classes=["golden"], ID="MN")
       m.intersect(ln_mn, c_o, other_than=M, classes=["golden"], ID="P")

       return make_result(m, ("M", "P"), ("P", "N"), ("M", "P", "N"))

Exact Symbolic Point Coordinates
--------------------------------

All points in ``bui-5step`` are certified free of floating-point approximations over :math:`\mathbb{Q}(\sqrt{5}, \sqrt{7})`:

.. list-table::
   :widths: 15 42 43
   :header-rows: 1

   * - Point
     - Exact :math:`x`
     - Exact :math:`y`
   * - ``O``
     - :math:`0`
     - :math:`0`
   * - ``B``
     - :math:`-1`
     - :math:`0`
   * - ``A``
     - :math:`1`
     - :math:`0`
   * - ``C``
     - :math:`-3`
     - :math:`0`
   * - ``M``
     - :math:`- \frac{1}{6}`
     - :math:`\frac{\sqrt{35}}{6}`
   * - ``N``
     - :math:`- \frac{3}{4}`
     - :math:`- \frac{3 \sqrt{7}}{4}`
   * - ``P``
     - :math:`\frac{- 21 \sqrt{2} \sqrt{\sqrt{5} + 3} - 14 \sqrt{5} + 7 \sqrt{10} \sqrt{\sqrt{5} + 3}}{96} - \frac{1}{48}`
     - :math:`\frac{- 17 \sqrt{14} \sqrt{\sqrt{5} + 3} - 2 \sqrt{7} + 2 \sqrt{35} + 3 \sqrt{70} \sqrt{\sqrt{5} + 3}}{96}`

**Certified Golden Ratio**: ``MP`` / ``PN`` = ``GoldenRatio``.
