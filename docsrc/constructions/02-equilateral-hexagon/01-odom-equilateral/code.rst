GC-02.01 · Symbolic Model & Source
==================================

Companion symbolic Python construction for :doc:`index` (``GC-02.01``).

Programmatic Usage
------------------

.. code-block:: python

   from geometor.divine.catalog import build_construction

   model, cert = build_construction("GC-02.01")
   assert cert.ratio_expr == sp.GoldenRatio

Exact Builder Implementation
----------------------------

.. code-block:: python

   def build_odom_equilateral() -> ConstructionResult:
       """George Odom's 1983 equilateral triangle midline & circumcircle secant."""
       m = new_catalog_model("odom-equilateral")
       s3 = sp.sqrt(3)
       A = m.set_point(0, 2, classes=["given"], ID="A")
       B = m.set_point(-s3, -1, classes=["given"], ID="B")
       C = m.set_point(s3, -1, classes=["given"], ID="C")
       O = m.set_point(0, 0, ID="O")

       m.construct_polygon([A, B, C], ID="ABC")
       c_o = m.construct_circle(O, A, classes=["primary"], ID="cO")

       L = m.set_point(-s3 / 2, sp.Rational(1, 2), ID="L")
       M = m.set_point(s3 / 2, sp.Rational(1, 2), ID="M")
       ln_lm = m.construct_line(L, M, classes=["golden"], ID="LM")

       X = m.intersect(ln_lm, c_o, beyond=(M, L), classes=["golden"], ID="X")
       m.intersect(ln_lm, c_o, beyond=(L, M), classes=["golden"], ID="Y")
       _ = X

       return make_result(m, ("L", "M"), ("M", "Y"), ("L", "M", "Y"))

Exact Symbolic Point Coordinates
--------------------------------

All points in ``odom-equilateral`` are certified free of floating-point approximations over :math:`\mathbb{Q}(\sqrt{3}, \phi)`:

.. list-table::
   :widths: 15 42 43
   :header-rows: 1

   * - Point
     - Exact :math:`x`
     - Exact :math:`y`
   * - ``A``
     - :math:`0`
     - :math:`2`
   * - ``B``
     - :math:`- \sqrt{3}`
     - :math:`-1`
   * - ``C``
     - :math:`\sqrt{3}`
     - :math:`-1`
   * - ``O``
     - :math:`0`
     - :math:`0`
   * - ``L``
     - :math:`- \frac{\sqrt{3}}{2}`
     - :math:`\frac{1}{2}`
   * - ``M``
     - :math:`\frac{\sqrt{3}}{2}`
     - :math:`\frac{1}{2}`
   * - ``X``
     - :math:`- \frac{\sqrt{15}}{2}`
     - :math:`\frac{1}{2}`
   * - ``Y``
     - :math:`\frac{\sqrt{15}}{2}`
     - :math:`\frac{1}{2}`

**Certified Golden Ratio**: ``LM`` / ``MY`` = ``GoldenRatio``.
