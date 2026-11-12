GC-05.02 · Symbolic Model & Source
==================================

Companion symbolic Python construction for :doc:`index` (``GC-05.02``).

Programmatic Usage
------------------

.. code-block:: python

   from geometor.divine.catalog import build_construction

   model, cert = build_construction("GC-05.02")
   assert cert.ratio_expr == sp.GoldenRatio

Exact Builder Implementation
----------------------------

.. code-block:: python

   def build_dao_tran_pentagon_bisector_incircle() -> ConstructionResult:
       """Dao Thanh Oai's perpendicular at a vertex of a regular pentagon."""
       m = new_catalog_model("dao-tran-pentagon-bisector-incircle")
       phi, s36, _c36, _s72, _c72 = _pentagon_radicals()
       phi2 = phi + 1

       A = m.set_point(-1, 0, classes=["given"], ID="A")
       B = m.set_point(1, 0, classes=["given"], ID="B")
       C = m.set_point(phi, 2 * phi * s36, ID="C")
       D = m.set_point(0, 2 * phi2 * s36, ID="D")
       E = m.set_point(-phi, 2 * phi * s36, ID="E")

       m.construct_polygon([A, B, C, D, E], ID="ABCDE")
       ln_ab = m.construct_line(A, B, classes=["golden"], ID="AB")
       m.construct_line(D, E, classes=["auxiliary"], ID="DE")

       # Perpendicular to DE at E: direction (2*s36, -phi)
       G1 = m.set_point(-phi + 2 * s36, 2 * phi * s36 - phi, guide=True, ID="G1")
       ln_ef = m.construct_line(E, G1, classes=["golden"], ID="EF")
       m.intersect(ln_ef, ln_ab, classes=["golden"], ID="F")

       return make_result(m, ("F", "B"), ("A", "F"), ("A", "F", "B"))

Exact Symbolic Point Coordinates
--------------------------------

All points in ``dao-tran-pentagon-bisector-incircle`` are certified free of floating-point approximations over :math:`\mathbb{Q}(\phi, \sqrt{10 - 2\sqrt{5}})`:

.. list-table::
   :widths: 15 42 43
   :header-rows: 1

   * - Point
     - Exact :math:`x`
     - Exact :math:`y`
   * - ``A``
     - :math:`-1`
     - :math:`0`
   * - ``B``
     - :math:`1`
     - :math:`0`
   * - ``C``
     - :math:`\frac{1}{2} + \frac{\sqrt{5}}{2}`
     - :math:`\frac{\sqrt{2} \sqrt{5 - \sqrt{5}} + \sqrt{10} \sqrt{5 - \sqrt{5}}}{4}`
   * - ``D``
     - :math:`0`
     - :math:`\frac{\sqrt{10} \sqrt{5 - \sqrt{5}} + 3 \sqrt{2} \sqrt{5 - \sqrt{5}}}{4}`
   * - ``E``
     - :math:`- \frac{\sqrt{5}}{2} - \frac{1}{2}`
     - :math:`\frac{\sqrt{2} \sqrt{5 - \sqrt{5}} + \sqrt{10} \sqrt{5 - \sqrt{5}}}{4}`
   * - ``F``
     - :math:`2 - \sqrt{5}`
     - :math:`0`

**Certified Golden Ratio**: ``FB`` / ``AF`` = ``GoldenRatio``.
