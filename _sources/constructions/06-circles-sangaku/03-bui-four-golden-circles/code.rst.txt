GC-06.03 · Symbolic Model & Source
==================================

Companion symbolic Python construction for :doc:`index` (``GC-06.03``).

Programmatic Usage
------------------

.. code-block:: python

   from geometor.divine.catalog import build_construction

   model, cert = build_construction("GC-06.03")
   assert cert.ratio_expr == sp.GoldenRatio

Exact Builder Implementation
----------------------------

.. code-block:: python

   def build_bui_four_golden_circles() -> ConstructionResult:
       """Bùi Quang Tuân's four congruent circles generating a vertical golden chain."""
       m = new_catalog_model("bui-four-golden-circles")
       s3 = sp.sqrt(3)
       s15 = sp.sqrt(15)

       A = m.set_point(-sp.Rational(1, 2), 0, classes=["given"], ID="A")
       B = m.set_point(sp.Rational(1, 2), 0, classes=["given"], ID="B")
       c_a = m.construct_circle(A, B, classes=["primary"], ID="cA")
       c_b = m.construct_circle(B, A, classes=["primary"], ID="cB")

       E = m.intersect(c_a, c_b, side_of=(A, B, 1), classes=["golden"], ID="E")
       N = m.intersect(c_a, c_b, side_of=(A, B, -1), classes=["golden"], ID="N")
       ln_axis = m.construct_line(N, E, classes=["golden"], ID="NE")
       _ = ln_axis

       # Congruent unit circles centered at D=(0, sqrt(15)/2) and C=(0, -sqrt(15)/2) tangent to cA, cB
       D = m.set_point(0, s15 / 2, classes=["golden"], ID="D")
       C = m.set_point(0, -s15 / 2, classes=["golden"], ID="C")
       T1 = m.set_point(-sp.Rational(1, 4), s15 / 4, guide=True, ID="T1")
       T2 = m.set_point(-sp.Rational(1, 4), -s15 / 4, guide=True, ID="T2")
       m.construct_circle(D, T1, classes=["golden"], ID="cD")
       m.construct_circle(C, T2, classes=["compass"], ID="cC")
       _ = s3

       return make_result(m, ("E", "N"), ("E", "D"), ("N", "E", "D"))

Exact Symbolic Point Coordinates
--------------------------------

All points in ``bui-four-golden-circles`` are certified free of floating-point approximations over :math:`\mathbb{Q}(\sqrt{3}, \phi)`:

.. list-table::
   :widths: 15 42 43
   :header-rows: 1

   * - Point
     - Exact :math:`x`
     - Exact :math:`y`
   * - ``A``
     - :math:`- \frac{1}{2}`
     - :math:`0`
   * - ``B``
     - :math:`\frac{1}{2}`
     - :math:`0`
   * - ``E``
     - :math:`0`
     - :math:`\frac{\sqrt{3}}{2}`
   * - ``N``
     - :math:`0`
     - :math:`- \frac{\sqrt{3}}{2}`
   * - ``D``
     - :math:`0`
     - :math:`\frac{\sqrt{15}}{2}`
   * - ``C``
     - :math:`0`
     - :math:`- \frac{\sqrt{15}}{2}`

**Certified Golden Ratio**: ``EN`` / ``ED`` = ``GoldenRatio``.
