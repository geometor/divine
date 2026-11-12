:type: construction
:order: 2
:excerpt: Divide hypotenuse AB at H in the golden ratio (AH/HB = φ), and erect perpendicular HC to semicircle cOB on diameter AB. Right triangle ABC has side lengths in geometric progression 1 : sqrt{φ} : φ and side quadrances in progression 1 : φ : φ^2.
:categories: 04-right-and-345
:tags: field-q-sqrt-phi, johannes-kepler

GC-04.02 · Johannes Kepler's Geometric-Progression Right Triangle (1597)
========================================================================

**Discoverer(s)**: :person:`Johannes Kepler <johannes-kepler>` | **Date**: 1597 | **Field**: :math:`\mathbb{Q}(\sqrt{\phi})` | **Loci**: 2 (:term:`Lemoine <geometrographie>` :math:`S = 6`)

.. enunciation::

   Divide hypotenuse :g:`AB` at :g:`H` in the golden ratio (:math:`|AH|/|HB| = \phi`), and erect perpendicular :g:`HC` to semicircle :g:`cOB` on diameter :g:`AB`. Right triangle :g:`ABC` has side lengths in geometric progression :math:`1 : \sqrt{\phi} : \phi` and side quadrances in progression :math:`1 : \phi : \phi^2`.

.. picture:: 02-kepler-geometric-triangle.svg
   :alt: GC-04.02 — Johannes Kepler's Geometric-Progression Right Triangle (1597)

Given & Constructive Steps
--------------------------

**Given**: Golden-sectioned hypotenuse :g:`A` :math:`= (0,0)`, :g:`H` :math:`= (\phi, 0)`, :g:`B` :math:`= (\phi^2, 0)` with midpoint :g:`O` :math:`= (\tfrac{\phi^2}{2}, 0)`.

.. step::

   Draw circle :g:`cOB` on diameter :g:`AB` of length :math:`\phi^2 = \phi + 1`.

.. step::

   Erect altitude :g:`HC` perpendicular to :g:`AB` at golden division point :g:`H` to meet :g:`cOB` at :g:`C` :math:`= (\phi, \sqrt{\phi})`.

.. step::

   Join :g:`AC` and :g:`BC` to complete right triangle :g:`ABC`.

Exact Symbolic Proof & Certificate
----------------------------------

By Euclid VI.8 and VI.13, altitude :g:`HC` is the geometric mean :math:`|HC|^2 = |AH|\cdot|HB| = \phi \cdot 1 = \phi`. Thus :math:`Q(B, C) = 1 + \phi = \phi^2`, :math:`Q(A, C) = \phi^2 + \phi = \phi^3`, and :math:`Q(A, B) = \phi^4`. Because :math:`\phi^2 + \phi^3 = \phi^2(1 + \phi) = \phi^4`, Kepler's two 'treasures of geometry'—the Pythagorean theorem and the golden section—unite uniquely in :math:`\triangle ABC`.

.. list-table:: Machine-Verified Symbolic Certificate
   :widths: 30 70
   :header-rows: 1

   * - Invariant
     - Exact Symbolic Value
   * - Primary Golden Ratio
     - :g:`AH` :math:`/` :g:`HB` :math:`= \frac{1}{2} + \frac{\sqrt{5}}{2}` on collinear triple (:g:`A`, :g:`H`, :g:`B`)
   * - Exact Segment Lengths
     - :math:`|AH| = \frac{1}{2} + \frac{\sqrt{5}}{2}`, :math:`|HB| = 1`
   * - Rational Trigonometry :term:`Quadrances <quadrance>`
     - :math:`Q(A, H) = \frac{\sqrt{5}}{2} + \frac{3}{2}`, :math:`Q(H, B) = 1`, :math:`Q_{\text{long}}/Q_{\text{short}} = \frac{\sqrt{5}}{2} + \frac{3}{2} = \phi^2`
   * - Algebraic Number Field
     - :math:`\mathbb{Q}(\sqrt{\phi})`
   * - :term:`Géométrographie <geometrographie>` Loci
     - 2 given points · 1 lines · 1 circles · 1 polygons (elementary loci :math:`= 2`, Lemoine :math:`S = 6`)

Automated Divine Scan
---------------------

:mod:`geometor.divine.golden` detected **1** exact collinear golden section(s) and **0** connected golden chain(s) in this model:

- Section (:g:`A`, :g:`H`, :g:`B`): long :math:`|AH|^2 = \frac{\sqrt{5}}{2} + \frac{3}{2}` vs. short :math:`|HB|^2 = 1`

Historical Commentary & Attribution
-----------------------------------

Kepler's triangle is the canonical entry point in the catalog whose coordinates genuinely require the quadratic extension :math:`\mathbb{Q}(\sqrt{\phi})` of degree :math:`4` over :math:`\mathbb{Q}`.

- **Scholarly Citations**: :cite:`Letter to Michael Mästlin (Tübingen, October 1597) <kepler-1597>`, :cite:`Cut-the-Knot: Golden Ratio in Geometry <bogomolny-golden-ratio>`
- **Curated Reference**: `Golden Ratio in Geometry — Kepler's Triangle <https://www.cut-the-knot.org/do_you_know/GoldenRatio.shtml>`_ (curated by :person:`Alexander Bogomolny <alexander-bogomolny>`, *Cut-the-Knot*, © 1996–2018)
- **Concepts**: :term:`Golden Ratio (φ) <golden-ratio>` · :term:`Golden Section <golden-section>` · :term:`Kepler Triangle <kepler-triangle>` · :term:`Quadrance <quadrance>`

.. toctree::
   :hidden:

   code
