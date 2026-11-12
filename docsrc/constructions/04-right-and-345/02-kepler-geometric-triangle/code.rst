GC-04.02 · Symbolic Model & Source
==================================

Companion symbolic Python construction for :doc:`index` (``GC-04.02``).

Programmatic Usage
------------------

.. code-block:: python

   from geometor.divine.catalog import build_construction

   model, cert = build_construction("GC-04.02")
   assert cert.ratio_expr == sp.GoldenRatio

Exact Builder Implementation
----------------------------

.. code-block:: python

   def build_kepler_geometric_triangle() -> ConstructionResult:
       """Johannes Kepler's right triangle with sides in geometric progression (1597)."""
       m = new_catalog_model("kepler-geometric-triangle")
       phi = sp.Rational(1, 2) + sp.sqrt(5) / 2
       phi2 = phi + 1

       A = m.set_point(0, 0, classes=["given"], ID="A")
       H = m.set_point(phi, 0, classes=["golden"], ID="H")
       B = m.set_point(phi2, 0, classes=["given"], ID="B")
       O = m.set_point(phi2 / 2, 0, ID="O")

       ln_ab = m.construct_line(A, B, classes=["golden"], ID="AB")
       _ = ln_ab
       m.construct_circle(O, B, classes=["primary"], ID="cOB")

       # Geometric mean altitude |HC| = sqrt(|AH| * |HB|) = sqrt(phi)
       C = m.set_point(phi, sp.sqrt(phi), classes=["golden"], ID="C")
       m.construct_polygon([A, B, C], classes=["golden"], ID="ABC")
       m.construct_segment(H, C, classes=["auxiliary"], ID="HC")

       return make_result(m, ("A", "H"), ("H", "B"), ("A", "H", "B"))

Exact Symbolic Point Coordinates
--------------------------------

All points in ``kepler-geometric-triangle`` are certified free of floating-point approximations over :math:`\mathbb{Q}(\sqrt{\phi})`:

.. list-table::
   :widths: 15 42 43
   :header-rows: 1

   * - Point
     - Exact :math:`x`
     - Exact :math:`y`
   * - ``A``
     - :math:`0`
     - :math:`0`
   * - ``H``
     - :math:`\frac{1}{2} + \frac{\sqrt{5}}{2}`
     - :math:`0`
   * - ``B``
     - :math:`\frac{\sqrt{5}}{2} + \frac{3}{2}`
     - :math:`0`
   * - ``O``
     - :math:`\frac{\sqrt{5}}{4} + \frac{3}{4}`
     - :math:`0`
   * - ``C``
     - :math:`\frac{1}{2} + \frac{\sqrt{5}}{2}`
     - :math:`\frac{\sqrt{2} \sqrt{1 + \sqrt{5}}}{2}`

**Certified Golden Ratio**: ``AH`` / ``HB`` = ``GoldenRatio``.
