GC-06.01 · Symbolic Model & Source
==================================

Companion symbolic Python construction for :doc:`index` (``GC-06.01``).

Programmatic Usage
------------------

.. code-block:: python

   from geometor.divine.catalog import build_construction

   model, cert = build_construction("GC-06.01")
   assert cert.ratio_expr == sp.GoldenRatio

Exact Builder Implementation
----------------------------

.. code-block:: python

   def build_bui_circle_droves() -> ConstructionResult:
       """Bùi Quang Tuân's infinite rational secant family dividing a radius in phi."""
       m = new_catalog_model("bui-circle-droves")
       s3 = sp.sqrt(3)
       s5 = sp.sqrt(5)

       O = m.set_point(0, 0, classes=["given"], ID="O")
       B = m.set_point(1, 0, classes=["given"], ID="B")
       A = m.set_point(-1, 0, ID="A")

       c_o = m.construct_circle(O, B, classes=["primary"], ID="cO")
       _ = c_o
       ln_ab = m.construct_line(A, B, classes=["golden"], ID="AB")

       # First pair (x1 = 0, y1 = 2/3): C1=(0,1), D1=(2/3, -sqrt(5)/3)
       C1 = m.set_point(0, 1, ID="C1")
       D1 = m.set_point(sp.Rational(2, 3), -s5 / 3, ID="D1")
       ln_c1d1 = m.construct_line(C1, D1, classes=["golden"], ID="C1D1")

       # Second pair (x2 = -1/2, y2 = 7/8): C2=(-1/2, sqrt(3)/2), D2=(7/8, -sqrt(15)/8)
       C2 = m.set_point(-sp.Rational(1, 2), s3 / 2, ID="C2")
       D2 = m.set_point(sp.Rational(7, 8), -(s3 * s5) / 8, ID="D2")
       ln_c2d2 = m.construct_line(C2, D2, classes=["auxiliary"], ID="C2D2")
       _ = ln_c2d2

       m.intersect(ln_c1d1, ln_ab, classes=["golden"], ID="M")

       return make_result(m, ("M", "B"), ("O", "M"), ("O", "M", "B"))

Exact Symbolic Point Coordinates
--------------------------------

All points in ``bui-circle-droves`` are certified free of floating-point approximations over :math:`\mathbb{Q}(\sqrt{3}, \phi)`:

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
     - :math:`1`
     - :math:`0`
   * - ``A``
     - :math:`-1`
     - :math:`0`
   * - ``C1``
     - :math:`0`
     - :math:`1`
   * - ``D1``
     - :math:`\frac{2}{3}`
     - :math:`- \frac{\sqrt{5}}{3}`
   * - ``C2``
     - :math:`- \frac{1}{2}`
     - :math:`\frac{\sqrt{3}}{2}`
   * - ``D2``
     - :math:`\frac{7}{8}`
     - :math:`- \frac{\sqrt{15}}{8}`
   * - ``M``
     - :math:`\frac{3}{2} - \frac{\sqrt{5}}{2}`
     - :math:`0`

**Certified Golden Ratio**: ``MB`` / ``OM`` = ``GoldenRatio``.
