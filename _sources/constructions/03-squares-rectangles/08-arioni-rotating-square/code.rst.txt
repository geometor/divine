GC-03.08 · Symbolic Model & Source
==================================

Companion symbolic Python construction for :doc:`index` (``GC-03.08``).

Programmatic Usage
------------------

.. code-block:: python

   from geometor.divine.catalog import build_construction

   model, cert = build_construction("GC-03.08")
   assert cert.ratio_expr == sp.GoldenRatio

Exact Builder Implementation
----------------------------

.. code-block:: python

   def build_arioni_rotating_square() -> ConstructionResult:
       """John Arioni's 30-degree rotated unit square and diagonal circle."""
       m = new_catalog_model("arioni-rotating-square")
       s3 = sp.sqrt(3)

       D = m.set_point(0, 0, classes=["given"], ID="D")
       G = m.set_point(1, 0, classes=["given"], ID="G")
       H = m.set_point(1, 1, ID="H")
       J = m.set_point(0, 1, ID="J")
       m.construct_polygon([D, G, H, J], ID="DGHJ")

       # Unit square DCBA rotated clockwise by 30 degrees around D
       A = m.set_point(sp.Rational(1, 2), s3 / 2, ID="A")
       B = m.set_point((1 + s3) / 2, (s3 - 1) / 2, ID="B")
       C = m.set_point(s3 / 2, -sp.Rational(1, 2), ID="C")
       m.construct_polygon([D, C, B, A], ID="DCBA")
       m.construct_segment(A, C, classes=["auxiliary"], ID="AC")

       ln_dg = m.construct_line(D, G, classes=["golden"], ID="DG")
       c_ac = m.construct_circle(A, C, classes=["golden"], ID="cAC")
       m.intersect(c_ac, ln_dg, beyond=(D, G), classes=["golden"], ID="E")
       F = m.intersect(c_ac, ln_dg, beyond=(G, D), classes=["golden"], ID="F")
       _ = F

       return make_result(m, ("D", "G"), ("G", "E"), ("D", "G", "E"))

Exact Symbolic Point Coordinates
--------------------------------

All points in ``arioni-rotating-square`` are certified free of floating-point approximations over :math:`\mathbb{Q}(\sqrt{3}, \phi)`:

.. list-table::
   :widths: 15 42 43
   :header-rows: 1

   * - Point
     - Exact :math:`x`
     - Exact :math:`y`
   * - ``D``
     - :math:`0`
     - :math:`0`
   * - ``G``
     - :math:`1`
     - :math:`0`
   * - ``H``
     - :math:`1`
     - :math:`1`
   * - ``J``
     - :math:`0`
     - :math:`1`
   * - ``A``
     - :math:`\frac{1}{2}`
     - :math:`\frac{\sqrt{3}}{2}`
   * - ``B``
     - :math:`\frac{1}{2} + \frac{\sqrt{3}}{2}`
     - :math:`- \frac{1}{2} + \frac{\sqrt{3}}{2}`
   * - ``C``
     - :math:`\frac{\sqrt{3}}{2}`
     - :math:`- \frac{1}{2}`
   * - ``E``
     - :math:`\frac{1}{2} + \frac{\sqrt{5}}{2}`
     - :math:`0`
   * - ``F``
     - :math:`\frac{1}{2} - \frac{\sqrt{5}}{2}`
     - :math:`0`

**Certified Golden Ratio**: ``DG`` / ``GE`` = ``GoldenRatio``.
