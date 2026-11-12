GC-04.03 · Symbolic Model & Source
==================================

Companion symbolic Python construction for :doc:`index` (``GC-04.03``).

Programmatic Usage
------------------

.. code-block:: python

   from geometor.divine.catalog import build_construction

   model, cert = build_construction("GC-04.03")
   assert cert.ratio_expr == sp.GoldenRatio

Exact Builder Implementation
----------------------------

.. code-block:: python

   def build_niemeyer_three_segments() -> ConstructionResult:
       """Jo Niemeyer's three equal segments leaning on a perpendicular line."""
       m = new_catalog_model("niemeyer-three-segments")
       s3 = sp.sqrt(3)

       A1 = m.set_point(0, 0, classes=["given"], ID="A1")
       B1 = m.set_point(2, 0, classes=["given"], ID="B1")
       B2 = m.set_point(1, 0, ID="B2")
       G0 = m.set_point(0, 1, guide=True, ID="G0")

       ln_l = m.construct_line(A1, G0, classes=["golden"], ID="L")
       m.construct_segment(A1, B1, ID="A1B1")

       # Second segment B2 A2 of length 2 with A2 on L
       R2 = m.set_point(3, 0, guide=True, ID="R2")
       c_b2 = m.construct_circle(B2, R2, classes=["compass"], ID="cB2")
       A2 = m.intersect(c_b2, ln_l, side_of=(A1, B1, 1), classes=["golden"], ID="A2")
       m.construct_segment(B2, A2, ID="B2A2")

       # Midpoint B3 of B2 A2 and third segment B3 A3 of length 2 with A3 on L
       B3 = m.set_point(sp.Rational(1, 2), s3 / 2, ID="B3")
       R3 = m.set_point(sp.Rational(5, 2), s3 / 2, guide=True, ID="R3")
       c_b3 = m.construct_circle(B3, R3, classes=["golden"], ID="cB3")
       A3 = m.intersect(c_b3, ln_l, beyond=(A1, A2), classes=["golden"], ID="A3")
       m.construct_segment(B3, A3, classes=["golden"], ID="B3A3")

       return make_result(m, ("A1", "A2"), ("A2", "A3"), ("A1", "A2", "A3"))

Exact Symbolic Point Coordinates
--------------------------------

All points in ``niemeyer-three-segments`` are certified free of floating-point approximations over :math:`\mathbb{Q}(\sqrt{3}, \phi)`:

.. list-table::
   :widths: 15 42 43
   :header-rows: 1

   * - Point
     - Exact :math:`x`
     - Exact :math:`y`
   * - ``A1``
     - :math:`0`
     - :math:`0`
   * - ``B1``
     - :math:`2`
     - :math:`0`
   * - ``B2``
     - :math:`1`
     - :math:`0`
   * - ``A2``
     - :math:`0`
     - :math:`\sqrt{3}`
   * - ``B3``
     - :math:`\frac{1}{2}`
     - :math:`\frac{\sqrt{3}}{2}`
   * - ``A3``
     - :math:`0`
     - :math:`\frac{\sqrt{3} + \sqrt{15}}{2}`

**Certified Golden Ratio**: ``A1A2`` / ``A2A3`` = ``GoldenRatio``.
