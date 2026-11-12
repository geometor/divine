GC-04.01 · Symbolic Model & Source
==================================

Companion symbolic Python construction for :doc:`index` (``GC-04.01``).

Programmatic Usage
------------------

.. code-block:: python

   from geometor.divine.catalog import build_construction

   model, cert = build_construction("GC-04.01")
   assert cert.ratio_expr == sp.GoldenRatio

Exact Builder Implementation
----------------------------

.. code-block:: python

   def build_huntley_egyptian_345() -> ConstructionResult:
       """H. E. Huntley's unexpected appearance of phi in a 3-4-5 right triangle."""
       m = new_catalog_model("huntley-egyptian-345")
       C = m.set_point(0, 0, classes=["given"], ID="C")
       B = m.set_point(3, 0, classes=["given"], ID="B")
       A = m.set_point(0, 4, ID="A")

       m.construct_polygon([A, B, C], ID="ABC")

       # Angle bisector of <ABC meets AC at O=(0, 3/2); circle O(C) is tangent to AB at T=(6/5, 12/5)
       O = m.set_point(0, sp.Rational(3, 2), ID="O")
       T = m.set_point(sp.Rational(6, 5), sp.Rational(12, 5), ID="T")
       _ = T

       ln_bo = m.construct_line(B, O, classes=["golden"], ID="BO")
       c_oc = m.construct_circle(O, C, classes=["golden"], ID="cOC")

       m.intersect(c_oc, ln_bo, between=(B, O), classes=["golden"], ID="P")
       m.intersect(c_oc, ln_bo, beyond=(B, O), classes=["golden"], ID="Q")

       return make_result(m, ("P", "Q"), ("B", "P"), ("B", "P", "Q"))

Exact Symbolic Point Coordinates
--------------------------------

All points in ``huntley-egyptian-345`` are certified free of floating-point approximations over :math:`\mathbb{Q}(\phi)`:

.. list-table::
   :widths: 15 42 43
   :header-rows: 1

   * - Point
     - Exact :math:`x`
     - Exact :math:`y`
   * - ``C``
     - :math:`0`
     - :math:`0`
   * - ``B``
     - :math:`3`
     - :math:`0`
   * - ``A``
     - :math:`0`
     - :math:`4`
   * - ``O``
     - :math:`0`
     - :math:`\frac{3}{2}`
   * - ``T``
     - :math:`\frac{6}{5}`
     - :math:`\frac{12}{5}`
   * - ``P``
     - :math:`\frac{3 \sqrt{5}}{5}`
     - :math:`\frac{3}{2} - \frac{3 \sqrt{5}}{10}`
   * - ``Q``
     - :math:`- \frac{3 \sqrt{5}}{5}`
     - :math:`\frac{3 \sqrt{5}}{10} + \frac{3}{2}`

**Certified Golden Ratio**: ``PQ`` / ``BP`` = ``GoldenRatio``.
