:type: construction
:order: 6
:excerpt: In square ABCD, let M be the midpoint of side AD. The inradii R and r of triangles triangle BCM (incircle cEH) and triangle CDM (incircle cFP) satisfy R / r = φ, and segment EF joining their incenters is divided by CM at K with EK/KF = φ.
:categories: 03-squares-rectangles
:tags: field-q-phi, ercole-suppa

GC-03.06 · Ercole Suppa's Square Midpoint Inradii Ratio (2015)
==============================================================

**Discoverer(s)**: :person:`Ercole Suppa <ercole-suppa>` | **Date**: 2015 | **Field**: :math:`\mathbb{Q}(\phi)` | **Loci**: 4 (:term:`Lemoine <geometrographie>` :math:`S = 12`)

.. enunciation::

   In square :g:`ABCD`, let :g:`M` be the midpoint of side :g:`AD`. The inradii :math:`R` and :math:`r` of triangles :math:`\triangle BCM` (incircle :g:`cEH`) and :math:`\triangle CDM` (incircle :g:`cFP`) satisfy :math:`R / r = \phi`, and segment :g:`EF` joining their incenters is divided by :g:`CM` at :g:`K` with :math:`|EK|/|KF| = \phi`.

.. picture:: 06-suppa-square-inradii.svg
   :alt: GC-03.06 — Ercole Suppa's Square Midpoint Inradii Ratio (2015)

Given & Constructive Steps
--------------------------

**Given**: Square :g:`ABCD` of side :math:`2` with :g:`D` :math:`= (0,0)`, :g:`C` :math:`= (2,0)`, :g:`B` :math:`= (2,2)`, :g:`A` :math:`= (0,2)` and midpoint :g:`M` :math:`= (0,1)`.

.. step::

   Join :g:`CM` and :g:`BM`, partitioning the lower and right regions into right :math:`\triangle CDM` and isosceles :math:`\triangle BCM`.

.. step::

   Inscribe circle :g:`cEH` in :math:`\triangle BCM` (incenter :g:`E`, tangent to :g:`BC` at :g:`H`) and circle :g:`cFP` in :math:`\triangle CDM` (incenter :g:`F`, tangent to :g:`CD` at :g:`P`).

.. step::

   Join incenters :g:`EF` to intersect shared side :g:`CM` at :g:`K`.

Exact Symbolic Proof & Certificate
----------------------------------

For :math:`\triangle BCM`, area :math:`= 2` and semiperimeter :math:`s_1 = 1 + \sqrt{5}` give inradius :math:`R = \frac{2}{\sqrt{5}+1} = \frac{\sqrt{5}-1}{2} = 1/\phi`. For right :math:`\triangle CDM` with legs :math:`1, 2` and hypotenuse :math:`\sqrt{5}`, inradius :math:`r = \frac{1 + 2 - \sqrt{5}}{2} = \frac{3 - \sqrt{5}}{2} = 1/\phi^2`. Since :g:`E` and :g:`F` lie at perpendicular distances :math:`R` and :math:`r` on opposite sides of shared line :g:`CM`, similar right triangles yield :math:`|EK|/|KF| = R/r = \phi`.

.. list-table:: Machine-Verified Symbolic Certificate
   :widths: 30 70
   :header-rows: 1

   * - Invariant
     - Exact Symbolic Value
   * - Primary Golden Ratio
     - :g:`EK` :math:`/` :g:`KF` :math:`= \frac{1}{2} + \frac{\sqrt{5}}{2}` on collinear triple (:g:`E`, :g:`K`, :g:`F`)
   * - Exact Segment Lengths
     - :math:`|EK| = \sqrt{5 - 2 \sqrt{5}}`, :math:`|KF| = \frac{\sqrt{2} \sqrt{25 - 11 \sqrt{5}}}{2}`
   * - Rational Trigonometry :term:`Quadrances <quadrance>`
     - :math:`Q(E, K) = 5 - 2 \sqrt{5}`, :math:`Q(K, F) = \frac{25}{2} - \frac{11 \sqrt{5}}{2}`, :math:`Q_{\text{long}}/Q_{\text{short}} = \frac{\sqrt{5}}{2} + \frac{3}{2} = \phi^2`
   * - Algebraic Number Field
     - :math:`\mathbb{Q}(\phi)`
   * - :term:`Géométrographie <geometrographie>` Loci
     - 2 given points · 2 lines · 2 circles · 1 polygons (elementary loci :math:`= 4`, Lemoine :math:`S = 12`)

Automated Divine Scan
---------------------

:mod:`geometor.divine.golden` detected **2** exact collinear golden section(s) and **0** connected golden chain(s) in this model:

- Section (:g:`M`, :g:`K`, :g:`C`): long :math:`|KC|^2 = \frac{15}{2} - \frac{5 \sqrt{5}}{2}` vs. short :math:`|MK|^2 = \frac{35}{2} - \frac{15 \sqrt{5}}{2}`
- Section (:g:`F`, :g:`K`, :g:`E`): long :math:`|KE|^2 = 5 - 2 \sqrt{5}` vs. short :math:`|FK|^2 = \frac{25}{2} - \frac{11 \sqrt{5}}{2}`

Historical Commentary & Attribution
-----------------------------------

Suppa's theorem exhibits consecutive negative powers of :math:`\phi` (:math:`\phi^{-1}` and :math:`\phi^{-2}`, whose sum :math:`\phi^{-1} + \phi^{-2} = 1` equals half the side of the square) as exact Euclidean inradii.

- **Scholarly Citations**: :cite:`Cut-the-Knot: Golden Ratio via Two Incircles in a Square <bogomolny-suppa-square>`, :cite:`Cut-the-Knot: Golden Ratio in Geometry <bogomolny-golden-ratio>`
- **Curated Reference**: `Golden Ratio via Two Incircles in a Square <https://www.cut-the-knot.org/do_you_know/GoldenRatioInSquare.shtml>`_ (curated by :person:`Alexander Bogomolny <alexander-bogomolny>`, *Cut-the-Knot*, © 1996–2018)
- **Concepts**: :term:`Golden Ratio (φ) <golden-ratio>` · :term:`Golden Section <golden-section>`

.. toctree::
   :hidden:

   code
