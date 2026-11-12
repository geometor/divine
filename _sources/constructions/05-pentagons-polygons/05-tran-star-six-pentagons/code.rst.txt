GC-05.05 · Symbolic Model & Source
==================================

Companion symbolic Python construction for :doc:`index` (``GC-05.05``).

Programmatic Usage
------------------

.. code-block:: python

   from geometor.divine.catalog import build_construction

   model, cert = build_construction("GC-05.05")
   assert cert.ratio_expr == sp.GoldenRatio

Exact Builder Implementation
----------------------------

.. code-block:: python

   def build_tran_star_six_pentagons() -> ConstructionResult:
       """Tran Quang Hung's star formed by reflecting a regular pentagon across its five sides."""
       m = new_catalog_model("tran-star-six-pentagons")
       phi, s36, _c36, _s72, _c72 = _pentagon_radicals()
       phi2 = phi + 1

       verts_xy = [
           (sp.Integer(-1), sp.Integer(0)),
           (sp.Integer(1), sp.Integer(0)),
           (phi, 2 * phi * s36),
           (sp.Integer(0), 2 * phi2 * s36),
           (-phi, 2 * phi * s36),
       ]
       names = ["A", "B", "C", "D", "E"]
       pts = [
           m.set_point(
               x,
               y,
               classes=["given"] if nm in ("A", "B") else [],
               ID=nm,
           )
           for nm, (x, y) in zip(names, verts_xy, strict=True)
       ]
       m.construct_polygon(pts, ID="ABCDE")

       # Reflect ABCDE across each of its 5 sides (each of exact length 2 => Q = 4)
       outer_pts = []
       for i in range(5):
           ux, uy = verts_xy[i]
           vx, vy = verts_xy[(i + 1) % 5]
           tri = []
           for idx_k, k in enumerate((4, 3, 2), start=1):
               wx, wy = verts_xy[(i + k) % 5]
               rx, ry = _reflect_across_side2(wx, wy, ux, uy, vx, vy)
               p_out = m.set_point(rx, ry, guide=(idx_k == 2), ID=f"R{i + 1}{idx_k}")
               tri.append(p_out)
               outer_pts.append(p_out)
           m.construct_polygon([pts[i], pts[(i + 1) % 5], tri[2], tri[1], tri[0]], classes=["auxiliary"])

       ln_ab = m.construct_line(pts[0], pts[1], classes=["golden"], ID="AB")

       # Connect outer perimeter vertices with step 6 (the chiral {5/2} star on lateral vertices)
       # Indices in outer_pts (length 15): 0, 3, 6, 9, 12 (idx_k=1) and 2, 5, 8, 11, 14 (idx_k=3)
       s_a = m.construct_line(outer_pts[0], outer_pts[6], classes=["golden"], ID="S1")
       s_b = m.construct_line(outer_pts[3], outer_pts[9], classes=["auxiliary"], ID="S2")
       for idx in (0, 3, 6, 9, 12):
           m.construct_segment(outer_pts[idx], outer_pts[(idx + 6) % 15], classes=["auxiliary"])
       for idx in (2, 5, 8, 11, 14):
           m.construct_segment(outer_pts[idx], outer_pts[(idx + 6) % 15], classes=["auxiliary"])

       G = m.intersect(s_a, ln_ab, classes=["golden"], ID="G")
       H = m.intersect(s_b, ln_ab, classes=["golden"], ID="H")
       _ = H

       # Order long/short dynamically: G = (2 - sqrt(5), 0) or (sqrt(5) - 2, 0) on A=(-1,0)..B=(1,0)
       if float((G.x - pts[0].x).evalf()) >= float((pts[1].x - G.x).evalf()):
           return make_result(m, ("A", "G"), ("G", "B"), ("A", "G", "B"))
       return make_result(m, ("G", "B"), ("A", "G"), ("A", "G", "B"))

Exact Symbolic Point Coordinates
--------------------------------

All points in ``tran-star-six-pentagons`` are certified free of floating-point approximations over :math:`\mathbb{Q}(\phi, \sqrt{10 - 2\sqrt{5}})`:

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
   * - ``R11``
     - :math:`- \frac{\sqrt{5}}{2} - \frac{1}{2}`
     - :math:`\frac{- \sqrt{10} \sqrt{5 - \sqrt{5}} - \sqrt{2} \sqrt{5 - \sqrt{5}}}{4}`
   * - ``R13``
     - :math:`\frac{1}{2} + \frac{\sqrt{5}}{2}`
     - :math:`\frac{- \sqrt{10} \sqrt{5 - \sqrt{5}} - \sqrt{2} \sqrt{5 - \sqrt{5}}}{4}`
   * - ``R21``
     - :math:`\frac{\sqrt{5}}{2} + \frac{3}{2}`
     - :math:`- \frac{\sqrt{2} \sqrt{5 - \sqrt{5}}}{2}`
   * - ``R23``
     - :math:`\frac{\sqrt{5}}{2} + \frac{5}{2}`
     - :math:`\frac{\sqrt{2} \sqrt{5 - \sqrt{5}} + \sqrt{10} \sqrt{5 - \sqrt{5}}}{4}`
   * - ``R31``
     - :math:`1 + \sqrt{5}`
     - :math:`\frac{\sqrt{10} \sqrt{5 - \sqrt{5}} + 3 \sqrt{2} \sqrt{5 - \sqrt{5}}}{4}`
   * - ``R33``
     - :math:`- \frac{1}{2} + \frac{\sqrt{5}}{2}`
     - :math:`\frac{2 \sqrt{2} \sqrt{5 - \sqrt{5}} + \sqrt{10} \sqrt{5 - \sqrt{5}}}{2}`
   * - ``R41``
     - :math:`\frac{1}{2} - \frac{\sqrt{5}}{2}`
     - :math:`\frac{2 \sqrt{2} \sqrt{5 - \sqrt{5}} + \sqrt{10} \sqrt{5 - \sqrt{5}}}{2}`
   * - ``R43``
     - :math:`- \sqrt{5} - 1`
     - :math:`\frac{\sqrt{10} \sqrt{5 - \sqrt{5}} + 3 \sqrt{2} \sqrt{5 - \sqrt{5}}}{4}`
   * - ``R51``
     - :math:`- \frac{5}{2} - \frac{\sqrt{5}}{2}`
     - :math:`\frac{\sqrt{2} \sqrt{5 - \sqrt{5}} + \sqrt{10} \sqrt{5 - \sqrt{5}}}{4}`
   * - ``R53``
     - :math:`- \frac{3}{2} - \frac{\sqrt{5}}{2}`
     - :math:`- \frac{\sqrt{2} \sqrt{5 - \sqrt{5}}}{2}`
   * - ``G``
     - :math:`-2 + \sqrt{5}`
     - :math:`0`
   * - ``H``
     - :math:`2`
     - :math:`0`

**Certified Golden Ratio**: ``AG`` / ``GB`` = ``GoldenRatio``.
