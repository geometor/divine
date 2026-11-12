GC-02.05 · Symbolic Model & Source
==================================

Companion symbolic Python construction for :doc:`index` (``GC-02.05``).

Programmatic Usage
------------------

.. code-block:: python

   from geometor.divine.catalog import build_construction

   model, cert = build_construction("GC-02.05")
   assert cert.ratio_expr == sp.GoldenRatio

Exact Builder Implementation
----------------------------

.. code-block:: python

   def build_tran_incircle_equilateral() -> ConstructionResult:
       """Tran Quang Hung's nested equilateral triangles inscribed in the incircle."""
       m = new_catalog_model("tran-incircle-equilateral")
       s3 = sp.sqrt(3)
       phi = sp.Rational(1, 2) + sp.sqrt(5) / 2

       # Outer equilateral triangle ABC of circumradius 2 (incircle radius 1 at O = (0,0))
       O = m.set_point(0, 0, ID="O")
       A = m.set_point(0, 2, classes=["given"], ID="A")
       B = m.set_point(-s3, -1, classes=["given"], ID="B")
       C = m.set_point(s3, -1, classes=["given"], ID="C")
       m.construct_polygon([A, B, C], ID="ABC")

       P_top = m.set_point(0, 1, guide=True, ID="Ptop")
       c_in = m.construct_circle(O, P_top, classes=["primary"], ID="cIn")

       # Inner equilateral triangle FGH on unit circle x^2 + y^2 = 1 such that
       # F lies on AH, G lies on CF, H lies on BG.
       # For F = (cos t, sin t) with 3-fold rotational symmetry:
       # Collinearity of A=(0,2), F=(x,y), H=(-x/2 - sqrt(3)y/2, sqrt(3)x/2 - y/2)
       # gives 3y + sqrt(3)x = 3*(x^2 + y^2)... exact solution:
       # y_F = (3 + sqrt(15))/8? Let's construct via exact algebraic coordinates!
       # Wait: if |AF| = a and |FH| = s = sqrt(3) (side of inscribed equilateral in unit circle!):
       # Power of A=(0,2) wrt unit circle x^2+y^2=1 is OA^2 - 1 = 4 - 1 = 3!
       # Secant AFH satisfies |AF| * |AH| = |AF| * (|AF| + |FH|) = 3!
       # Since |FH| = sqrt(3), |AF|*(|AF| + sqrt(3)) = 3 => (|AF|/sqrt(3))*((|AF|/sqrt(3)) + 1) = 1
       # => |AF| = sqrt(3)/phi !! And |FH| / |AF| = sqrt(3) / (sqrt(3)/phi) = phi !!
       # Let's compute exact coordinates of F on x^2+y^2=1 with |AF|^2 = 3/phi^2 = 3*(2 - phi):
       # x_F^2 + (y_F - 2)^2 = 3*(2 - phi) => 1 + 4 - 4*y_F = 6 - 3*phi => y_F = (3*phi - 1)/4 = (1 + 3*sqrt(5))/8!
       # And x_F^2 = 1 - y_F^2 = 1 - (46 + 6*sqrt(5))/64 = (18 - 6*sqrt(5))/64 = 3*(3 - sqrt(5))/32 = 3/(16*phi^2)!
       #Wait: 1^2 + (3*sqrt(5))^2 = 1 + 45 = 46! 64 - 46 = 18! 18 - 6*sqrt(5) = 3*(6 - 2*sqrt(5)) = 3*(sqrt(5)-1)^2!
       # SO x_F = sqrt(3)*(sqrt(5) - 1)/8 = sqrt(3)/(4*phi) (rational in sqrt(3) and phi, ZERO nested radicals!!)!
       xf = s3 / (4 * phi)
       yf = (3 * phi - 1) / 4

       F = m.set_point(-xf, yf, classes=["golden"], ID="F")
       H = m.set_point(xf / 2 - s3 * yf / 2, -s3 * xf / 2 - yf / 2, classes=["golden"], ID="H")
       G = m.set_point(xf / 2 + s3 * yf / 2, s3 * xf / 2 - yf / 2, classes=["golden"], ID="G")

       m.construct_polygon([F, G, H], classes=["golden"], ID="FGH")
       m.construct_line(A, H, classes=["golden"], ID="AH")
       m.construct_line(B, G, classes=["auxiliary"], ID="BG")
       m.construct_line(C, F, classes=["auxiliary"], ID="CF")
       _ = c_in

       return make_result(m, ("F", "H"), ("A", "F"), ("A", "F", "H"))

Exact Symbolic Point Coordinates
--------------------------------

All points in ``tran-incircle-equilateral`` are certified free of floating-point approximations over :math:`\mathbb{Q}(\sqrt{3}, \phi)`:

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
     - :math:`0`
     - :math:`2`
   * - ``B``
     - :math:`- \sqrt{3}`
     - :math:`-1`
   * - ``C``
     - :math:`\sqrt{3}`
     - :math:`-1`
   * - ``F``
     - :math:`\frac{- \sqrt{15} + \sqrt{3}}{8}`
     - :math:`\frac{1}{8} + \frac{3 \sqrt{5}}{8}`
   * - ``H``
     - :math:`\frac{- \sqrt{15} - \sqrt{3}}{8}`
     - :math:`\frac{1}{8} - \frac{3 \sqrt{5}}{8}`
   * - ``G``
     - :math:`\frac{\sqrt{15}}{4}`
     - :math:`- \frac{1}{4}`

**Certified Golden Ratio**: ``FH`` / ``AF`` = ``GoldenRatio``.
