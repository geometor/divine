GC-01.05 · Symbolic Model & Source
==================================

Companion symbolic Python construction for :doc:`index` (``GC-01.05``).

Programmatic Usage
------------------

.. code-block:: python

   from geometor.divine.catalog import build_construction

   model, cert = build_construction("GC-01.05")
   assert cert.ratio_expr == sp.GoldenRatio

Exact Builder Implementation
----------------------------

.. code-block:: python

   def build_hofstetter_compass_only() -> ConstructionResult:
       """Kurt Hofstetter's 2002 Mascheroni 5-circle compass-only construction."""
       m = new_catalog_model("hofstetter-compass-only")
       A = m.set_point(0, 0, classes=["given"], ID="A")
       B = m.set_point(1, 0, classes=["given"], ID="B")

       # Strictly 5 circles and 0 lines
       c1 = m.construct_circle(A, B, classes=["compass"], ID="c1")
       c2 = m.construct_circle(B, A, classes=["compass"], ID="c2")
       C = m.intersect(c1, c2, side_of=(A, B, 1), ID="C")
       D = m.intersect(c1, c2, side_of=(A, B, -1), ID="D")

       c3 = m.construct_circle(C, D, classes=["compass"], ID="c3")
       E = m.intersect(c3, c1, other_than=D, ID="E")
       F = m.intersect(c3, c2, other_than=D, ID="F")

       c4 = m.construct_circle(B, E, classes=["golden"], ID="c4")
       c5 = m.construct_circle(A, F, classes=["golden"], ID="c5")
       m.intersect(c4, c5, side_of=(A, B, -1), classes=["golden"], ID="X")
       Y = m.intersect(c4, c5, side_of=(A, B, 1), classes=["golden"], ID="Y")
       _ = Y

       return make_result(m, ("C", "D"), ("D", "X"), ("C", "D", "X"))

Exact Symbolic Point Coordinates
--------------------------------

All points in ``hofstetter-compass-only`` are certified free of floating-point approximations over :math:`\mathbb{Q}(\sqrt{3}, \phi)`:

.. list-table::
   :widths: 15 42 43
   :header-rows: 1

   * - Point
     - Exact :math:`x`
     - Exact :math:`y`
   * - ``A``
     - :math:`0`
     - :math:`0`
   * - ``B``
     - :math:`1`
     - :math:`0`
   * - ``C``
     - :math:`\frac{1}{2}`
     - :math:`\frac{\sqrt{3}}{2}`
   * - ``D``
     - :math:`\frac{1}{2}`
     - :math:`- \frac{\sqrt{3}}{2}`
   * - ``E``
     - :math:`-1`
     - :math:`0`
   * - ``F``
     - :math:`2`
     - :math:`0`
   * - ``X``
     - :math:`\frac{1}{2}`
     - :math:`- \frac{\sqrt{15}}{2}`
   * - ``Y``
     - :math:`\frac{1}{2}`
     - :math:`\frac{\sqrt{15}}{2}`

**Certified Golden Ratio**: ``CD`` / ``DX`` = ``GoldenRatio``.
