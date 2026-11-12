GC-01.01 · Symbolic Model & Source
==================================

Companion symbolic Python construction for :doc:`index` (``GC-01.01``).

Programmatic Usage
------------------

.. code-block:: python

   from geometor.divine.catalog import build_construction

   model, cert = build_construction("GC-01.01")
   assert cert.ratio_expr == sp.GoldenRatio

Exact Builder Implementation
----------------------------

.. code-block:: python

   def build_euclid_ii_11() -> ConstructionResult:
       """Euclid's Elements II.11 & VI.30 square-and-midpoint division of AB."""
       m = new_catalog_model("euclid-ii-11")
       A = m.set_point(0, 0, classes=["given"], ID="A")
       B = m.set_point(2, 0, classes=["given"], ID="B")
       D = m.set_point(0, 2, ID="D")
       C = m.set_point(2, 2, ID="C")

       m.construct_polygon([A, B, C, D], ID="ABCD")
       ln_ad = m.construct_line(A, D, classes=["auxiliary"], ID="AD")
       seg_ab = m.construct_segment(A, B, ID="segAB")

       # Midpoint M of side AD and compass transfer M(B) onto ray DA
       M = m.set_point(0, 1, ID="M")
       m.construct_segment(M, B, classes=["auxiliary"], ID="MB")
       c_mb = m.construct_circle(M, B, classes=["compass"], ID="cMB")
       E = m.intersect(c_mb, ln_ad, beyond=(D, A), ID="E")

       # Transfer AE onto AB at G (and erect golden gnomon square AEFH)
       c_ae = m.construct_circle(A, E, classes=["golden"], ID="cAE")
       G = m.intersect(c_ae, seg_ab, between=(A, B), classes=["golden"], ID="G")
       F = m.set_point(G.x, E.y, ID="F")
       m.construct_polygon([A, G, F, E], classes=["golden"], ID="AGFE")

       return make_result(m, ("A", "G"), ("G", "B"), ("A", "G", "B"))

Exact Symbolic Point Coordinates
--------------------------------

All points in ``euclid-ii-11`` are certified free of floating-point approximations over :math:`\mathbb{Q}(\phi)`:

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
     - :math:`2`
     - :math:`0`
   * - ``D``
     - :math:`0`
     - :math:`2`
   * - ``C``
     - :math:`2`
     - :math:`2`
   * - ``M``
     - :math:`0`
     - :math:`1`
   * - ``E``
     - :math:`0`
     - :math:`1 - \sqrt{5}`
   * - ``G``
     - :math:`-1 + \sqrt{5}`
     - :math:`0`
   * - ``F``
     - :math:`-1 + \sqrt{5}`
     - :math:`1 - \sqrt{5}`

**Certified Golden Ratio**: ``AG`` / ``GB`` = ``GoldenRatio``.
