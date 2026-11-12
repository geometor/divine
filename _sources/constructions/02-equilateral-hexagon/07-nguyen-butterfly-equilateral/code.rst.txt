GC-02.07 · Symbolic Model & Source
==================================

Companion symbolic Python construction for :doc:`index` (``GC-02.07``).

Programmatic Usage
------------------

.. code-block:: python

   from geometor.divine.catalog import build_construction

   model, cert = build_construction("GC-02.07")
   assert cert.ratio_expr == sp.GoldenRatio

Exact Builder Implementation
----------------------------

.. code-block:: python

   def build_nguyen_butterfly_equilateral() -> ConstructionResult:
       """Nguyen Thanh Dung's butterfly chords astride an equilateral triangle."""
       m = new_catalog_model("nguyen-butterfly-equilateral")
       s3 = sp.sqrt(3)

       O = m.set_point(0, 0, classes=["given"], ID="O")
       J = m.set_point(0, 2, classes=["given"], ID="J")
       I = m.set_point(0, 1, ID="I")

       c_o = m.construct_circle(O, J, classes=["primary"], ID="cO")
       m.construct_segment(O, J, classes=["auxiliary"], ID="OJ")

       # Chord XT perpendicular to OJ through I=(0,1): x^2 + 1 = 4 => x = +-sqrt(3)
       X = m.set_point(-s3, 1, ID="X")
       T = m.set_point(s3, 1, ID="T")
       ln_xt = m.construct_line(X, T, classes=["golden"], ID="XT")

       # Equilateral triangle ICD with apex I=(0,1) and C, D on circle x^2 + y^2 = 4 below I:
       # Let side of equilateral ICD be s, symmetric about y-axis: C = (-s/2, 1 - s*sqrt(3)/2), D = (s/2, 1 - s*sqrt(3)/2)
       # On x^2 + y^2 = 4: s^2/4 + 1 - s*sqrt(3) + 3*s^2/4 = 4 => s^2 - s*sqrt(3) - 3 = 0
       # => s = (sqrt(3) + sqrt(15))/2 = sqrt(3)*phi !!
       phi = sp.Rational(1, 2) + sp.sqrt(5) / 2
       s_eq = s3 * phi
       C = m.set_point(-s_eq / 2, 1 - s_eq * s3 / 2, ID="C")
       D = m.set_point(s_eq / 2, 1 - s_eq * s3 / 2, ID="D")
       m.construct_polygon([I, C, D], ID="ICD")

       ln_ic = m.construct_line(I, C, classes=["auxiliary"], ID="IC")
       ln_id = m.construct_line(I, D, classes=["auxiliary"], ID="ID")
       A = m.intersect(ln_ic, c_o, other_than=C, ID="A")
       B = m.intersect(ln_id, c_o, other_than=D, ID="B")

       ln_ad = m.construct_line(A, D, classes=["auxiliary"], ID="AD")
       ln_bc = m.construct_line(B, C, classes=["auxiliary"], ID="BC")
       m.intersect(ln_bc, ln_xt, classes=["golden"], ID="Y")
       m.intersect(ln_ad, ln_xt, classes=["golden"], ID="Z")

       return make_result(m, ("Y", "Z"), ("Z", "T"), ("Y", "Z", "T"))

Exact Symbolic Point Coordinates
--------------------------------

All points in ``nguyen-butterfly-equilateral`` are certified free of floating-point approximations over :math:`\mathbb{Q}(\sqrt{3}, \phi)`:

.. list-table::
   :widths: 15 42 43
   :header-rows: 1

   * - Point
     - Exact :math:`x`
     - Exact :math:`y`
   * - ``O``
     - :math:`0`
     - :math:`0`
   * - ``J``
     - :math:`0`
     - :math:`2`
   * - ``I``
     - :math:`0`
     - :math:`1`
   * - ``X``
     - :math:`- \sqrt{3}`
     - :math:`1`
   * - ``T``
     - :math:`\sqrt{3}`
     - :math:`1`
   * - ``C``
     - :math:`\frac{- \sqrt{15} - \sqrt{3}}{4}`
     - :math:`\frac{1}{4} - \frac{3 \sqrt{5}}{4}`
   * - ``D``
     - :math:`\frac{\sqrt{3} + \sqrt{15}}{4}`
     - :math:`\frac{1}{4} - \frac{3 \sqrt{5}}{4}`
   * - ``A``
     - :math:`\frac{- \sqrt{30} \sqrt{\sqrt{5} + 3} - 4 \sqrt{3} + 5 \sqrt{6} \sqrt{\sqrt{5} + 3}}{16}`
     - :math:`\frac{1}{4} + \frac{- 3 \sqrt{10} \sqrt{\sqrt{5} + 3} + 15 \sqrt{2} \sqrt{\sqrt{5} + 3}}{16}`
   * - ``B``
     - :math:`\frac{- 5 \sqrt{6} \sqrt{\sqrt{5} + 3} + 4 \sqrt{3} + \sqrt{30} \sqrt{\sqrt{5} + 3}}{16}`
     - :math:`\frac{1}{4} + \frac{- 3 \sqrt{10} \sqrt{\sqrt{5} + 3} + 15 \sqrt{2} \sqrt{\sqrt{5} + 3}}{16}`
   * - ``Y``
     - :math:`\frac{- 2 \sqrt{15} - 2 \sqrt{3} + 2 \sqrt{30} \sqrt{\sqrt{5} + 3}}{- 5 \sqrt{2} \sqrt{\sqrt{5} + 3} - 4 \sqrt{5} + \sqrt{10} \sqrt{\sqrt{5} + 3}}`
     - :math:`1`
   * - ``Z``
     - :math:`\frac{- 2 \sqrt{30} \sqrt{\sqrt{5} + 3} + 2 \sqrt{3} + 2 \sqrt{15}}{- 5 \sqrt{2} \sqrt{\sqrt{5} + 3} - 4 \sqrt{5} + \sqrt{10} \sqrt{\sqrt{5} + 3}}`
     - :math:`1`

**Certified Golden Ratio**: ``YZ`` / ``ZT`` = ``GoldenRatio``.
