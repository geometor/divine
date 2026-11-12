GC-04.04 · Symbolic Model & Source
==================================

Companion symbolic Python construction for :doc:`index` (``GC-04.04``).

Programmatic Usage
------------------

.. code-block:: python

   from geometor.divine.catalog import build_construction

   model, cert = build_construction("GC-04.04")
   assert cert.ratio_expr == sp.GoldenRatio

Exact Builder Implementation
----------------------------

.. code-block:: python

   def build_bui_van_obel_isosceles() -> ConstructionResult:
       """Bùi Quang Tuân's Van Obel cevian division in a right isosceles triangle."""
       m = new_catalog_model("bui-van-obel-isosceles")
       B = m.set_point(-2, 0, classes=["given"], ID="B")
       C = m.set_point(2, 0, classes=["given"], ID="C")
       A = m.set_point(0, 2, ID="A")
       M = m.set_point(0, 0, ID="M")
       O = m.set_point(0, 1, ID="O")

       m.construct_polygon([A, B, C], ID="ABC")
       ln_am = m.construct_line(A, M, classes=["golden"], ID="AM")
       c_om = m.construct_circle(O, M, classes=["primary"], ID="cOM")

       ln_oc = m.construct_line(O, C, classes=["auxiliary"], ID="OC")
       ln_ob = m.construct_line(O, B, classes=["auxiliary"], ID="OB")
       D = m.intersect(c_om, ln_oc, between=(O, C), ID="D")
       F = m.intersect(c_om, ln_ob, between=(O, B), ID="F")

       ln_bd = m.construct_line(B, D, classes=["golden"], ID="BD")
       ln_cf = m.construct_line(C, F, classes=["golden"], ID="CF")
       _ = ln_cf
       m.intersect(ln_bd, ln_am, classes=["golden"], ID="E")

       return make_result(m, ("O", "E"), ("E", "M"), ("O", "E", "M"))

Exact Symbolic Point Coordinates
--------------------------------

All points in ``bui-van-obel-isosceles`` are certified free of floating-point approximations over :math:`\mathbb{Q}(\phi)`:

.. list-table::
   :widths: 15 42 43
   :header-rows: 1

   * - Point
     - Exact :math:`x`
     - Exact :math:`y`
   * - ``B``
     - :math:`-2`
     - :math:`0`
   * - ``C``
     - :math:`2`
     - :math:`0`
   * - ``A``
     - :math:`0`
     - :math:`2`
   * - ``M``
     - :math:`0`
     - :math:`0`
   * - ``O``
     - :math:`0`
     - :math:`1`
   * - ``D``
     - :math:`\frac{2 \sqrt{5}}{5}`
     - :math:`1 - \frac{\sqrt{5}}{5}`
   * - ``F``
     - :math:`- \frac{2 \sqrt{5}}{5}`
     - :math:`1 - \frac{\sqrt{5}}{5}`
   * - ``E``
     - :math:`0`
     - :math:`\frac{3}{2} - \frac{\sqrt{5}}{2}`

**Certified Golden Ratio**: ``OE`` / ``EM`` = ``GoldenRatio``.
