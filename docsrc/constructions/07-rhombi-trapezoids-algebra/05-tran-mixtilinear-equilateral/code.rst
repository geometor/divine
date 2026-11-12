GC-07.05 · Symbolic Model & Source
==================================

Companion symbolic Python construction for :doc:`index` (``GC-07.05``).

Programmatic Usage
------------------

.. code-block:: python

   from geometor.divine.catalog import build_construction

   model, cert = build_construction("GC-07.05")
   assert cert.ratio_expr == sp.GoldenRatio

Exact Builder Implementation
----------------------------

.. code-block:: python

   def build_tran_mixtilinear_equilateral() -> ConstructionResult:
       """Tran Quang Hung's Golden Ratio in a mixtilinear circle of an equilateral triangle."""
       m = new_catalog_model("tran-mixtilinear-equilateral")
       s3 = sp.sqrt(3)

       # Side 18 equilateral triangle ABC => all key points have exact integer * radical coordinates
       A = m.set_point(-9, 0, classes=["given"], ID="A")
       B = m.set_point(9, 0, classes=["given"], ID="B")
       C = m.set_point(0, 9 * s3, ID="C")
       K = m.set_point(0, 3 * s3, ID="K")

       m.construct_polygon([A, B, C], ID="ABC")
       m.construct_circle(K, C, classes=["primary"], ID="cK")

       # A-mixtilinear incircle centered at F=(3, 4*sqrt(3)), tangent to AB at D=(3,0) and (ABC) at T=(9, 6*sqrt(3))
       D = m.set_point(3, 0, ID="D")
       F = m.set_point(3, 4 * s3, ID="F")
       c_f = m.construct_circle(F, D, classes=["golden"], ID="cF")

       # Horizontal line through circumcenter K=(0, 3*sqrt(3)) meets BC at O=(6, 3*sqrt(3))
       O = m.set_point(6, 3 * s3, classes=["golden"], ID="O")
       ln_ko = m.construct_line(K, O, classes=["golden"], ID="KO")

       I = m.intersect(c_f, ln_ko, beyond=(O, K), classes=["golden"], ID="I")
       m.intersect(c_f, ln_ko, beyond=(K, O), classes=["golden"], ID="J")
       _ = I

       return make_result(m, ("K", "O"), ("O", "J"), ("K", "O", "J"))

Exact Symbolic Point Coordinates
--------------------------------

All points in ``tran-mixtilinear-equilateral`` are certified free of floating-point approximations over :math:`\mathbb{Q}(\sqrt{3}, \phi)`:

.. list-table::
   :widths: 15 42 43
   :header-rows: 1

   * - Point
     - Exact :math:`x`
     - Exact :math:`y`
   * - ``A``
     - :math:`-9`
     - :math:`0`
   * - ``B``
     - :math:`9`
     - :math:`0`
   * - ``C``
     - :math:`0`
     - :math:`9 \sqrt{3}`
   * - ``K``
     - :math:`0`
     - :math:`3 \sqrt{3}`
   * - ``D``
     - :math:`3`
     - :math:`0`
   * - ``F``
     - :math:`3`
     - :math:`4 \sqrt{3}`
   * - ``O``
     - :math:`6`
     - :math:`3 \sqrt{3}`
   * - ``I``
     - :math:`3 - 3 \sqrt{5}`
     - :math:`3 \sqrt{3}`
   * - ``J``
     - :math:`3 + 3 \sqrt{5}`
     - :math:`3 \sqrt{3}`

**Certified Golden Ratio**: ``KO`` / ``OJ`` = ``GoldenRatio``.
