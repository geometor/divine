:type: construction
:order: 2
:excerpt: Let equal unit circles cB and cD touch externally at C, and let AF be the diameter of cB perpendicular to line of centers BD. Secant FD cuts cD at H and I such that HI/FH = FI/HI = FI/AF = φ.
:categories: 06-circles-sangaku
:tags: field-q-phi, elliot-mcgucken, thanos-kalogerakis

GC-06.02 · Elliot McGucken & Thanos Kalogerakis's Equal Tangent Circles
=======================================================================

**Discoverer(s)**: :person:`Elliot McGucken <elliot-mcgucken>`, :person:`Thanos Kalogerakis <thanos-kalogerakis>` | **Date**: 2016 | **Field**: :math:`\mathbb{Q}(\phi)` | **Loci**: 4 (:term:`Lemoine <geometrographie>` :math:`S = 12`)

.. enunciation::

   Let equal unit circles :g:`cB` and :g:`cD` touch externally at :g:`C`, and let :g:`AF` be the diameter of :g:`cB` perpendicular to line of centers :g:`BD`. Secant :g:`FD` cuts :g:`cD` at :g:`H` and :g:`I` such that :math:`|HI|/|FH| = |FI|/|HI| = |FI|/|AF| = \phi`.

.. picture:: 02-mcgucken-kalogerakis-equal-circles.svg
   :alt: GC-06.02 — Elliot McGucken & Thanos Kalogerakis's Equal Tangent Circles

Given & Constructive Steps
--------------------------

**Given**: Externally tangent unit circles :g:`cB` at :g:`B` :math:`= (0,0)` and :g:`cD` at :g:`D` :math:`= (2,0)`, touching at :g:`C` :math:`= (1,0)`.

.. step::

   Erect perpendicular diameter :g:`AF` of :g:`cB` with :g:`F` :math:`= (0,1)` and :g:`A` :math:`= (0,-1)`.

.. step::

   Draw secant line :g:`FD` through center :g:`D` of circle :g:`cD`.

.. step::

   Mark intersections :g:`H` (near) and :g:`I` (far) of :g:`FD` with :g:`cD`.

Exact Symbolic Proof & Certificate
----------------------------------

Right triangle :math:`\triangle FBD` has legs :math:`|BF| = 1` and :math:`|BD| = 2`, giving :math:`|FD| = \sqrt{5}`. Subtracting and adding radius :math:`1` of :g:`cD` yields :math:`|FH| = \sqrt{5} - 1 = 2/\phi`, diameter :math:`|HI| = 2`, and :math:`|FI| = \sqrt{5} + 1 = 2\phi`. Hence :math:`|HI|/|FH| = \phi` (McGucken) and :math:`|FI|/|AF| = \phi` (Kalogerakis).

.. list-table:: Machine-Verified Symbolic Certificate
   :widths: 30 70
   :header-rows: 1

   * - Invariant
     - Exact Symbolic Value
   * - Primary Golden Ratio
     - :g:`HI` :math:`/` :g:`FH` :math:`= \frac{1}{2} + \frac{\sqrt{5}}{2}` on collinear triple (:g:`F`, :g:`H`, :g:`I`)
   * - Exact Segment Lengths
     - :math:`|HI| = 2`, :math:`|FH| = -1 + \sqrt{5}`
   * - Rational Trigonometry :term:`Quadrances <quadrance>`
     - :math:`Q(H, I) = 4`, :math:`Q(F, H) = 6 - 2 \sqrt{5}`, :math:`Q_{\text{long}}/Q_{\text{short}} = \frac{\sqrt{5}}{2} + \frac{3}{2} = \phi^2`
   * - Algebraic Number Field
     - :math:`\mathbb{Q}(\phi)`
   * - :term:`Géométrographie <geometrographie>` Loci
     - 2 given points · 2 lines · 2 circles · 0 polygons (elementary loci :math:`= 4`, Lemoine :math:`S = 12`)

Automated Divine Scan
---------------------

:mod:`geometor.divine.golden` detected **1** exact collinear golden section(s) and **0** connected golden chain(s) in this model:

- Section (:g:`F`, :g:`H`, :g:`I`): long :math:`|HI|^2 = 4` vs. short :math:`|FH|^2 = 6 - 2 \sqrt{5}`

Historical Commentary & Attribution
-----------------------------------

This construction geometricizes the Heron-Ptolemy :math:`1\text{-}2\text{-}\sqrt{5}` right triangle purely through two tangent unit circles.

- **Scholarly Citations**: :cite:`Cut-the-Knot: Golden Ratio in Two Equal Circles <bogomolny-mcgucken-1>`, :cite:`Cut-the-Knot: Golden Ratio in Two Tangent Circles <bogomolny-kalogerakis>`, :cite:`Cut-the-Knot: Golden Ratio in Geometry <bogomolny-golden-ratio>`
- **Curated Reference**: `Golden Ratio in Two Equal Circles <https://www.cut-the-knot.org/do_you_know/ElliotMcGucken1.shtml>`_ (curated by :person:`Alexander Bogomolny <alexander-bogomolny>`, *Cut-the-Knot*, © 1996–2018)
- **Concepts**: :term:`Golden Ratio (φ) <golden-ratio>` · :term:`Golden Section <golden-section>` · :term:`Power of a Point <power-of-a-point>`

.. toctree::
   :hidden:

   code
