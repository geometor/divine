:type: construction
:order: 6
:excerpt: Inscribe twin tangent circles cA and cC of radius tfrac{1}{2} along horizontal diameter PLPR of unit circle cO, and let B be the apex of perpendicular radius OB. Secant BA cuts cA at H and I such that HI/BH = BI/HI = φ.
:categories: 06-circles-sangaku
:tags: field-q-phi, john-arioni

GC-06.06 · John Arioni's Golden Secant in the Yin-Yang Circle
=============================================================

**Discoverer(s)**: :person:`John Arioni <john-arioni>` | **Date**: 2016 | **Field**: :math:`\mathbb{Q}(\phi)` | **Loci**: 4 (:term:`Lemoine <geometrographie>` :math:`S = 12`)

.. enunciation::

   Inscribe twin tangent circles :g:`cA` and :g:`cC` of radius :math:`\tfrac{1}{2}` along horizontal diameter :g:`PLPR` of unit circle :g:`cO`, and let :g:`B` be the apex of perpendicular radius :g:`OB`. Secant :g:`BA` cuts :g:`cA` at :g:`H` and :g:`I` such that :math:`|HI|/|BH| = |BI|/|HI| = \phi`.

.. picture:: 06-arioni-yin-yang.svg
   :alt: GC-06.06 — John Arioni's Golden Secant in the Yin-Yang Circle

Given & Constructive Steps
--------------------------

**Given**: Unit circle :g:`cO` centered at :g:`O` :math:`= (0,0)` with apex :g:`B` :math:`= (0,1)`.

.. step::

   Bisect radii :g:`OPL` and :g:`OPR` at :g:`A` :math:`= (-\tfrac{1}{2}, 0)` and :g:`C` :math:`= (\tfrac{1}{2}, 0)` and draw inner circles :g:`cA` and :g:`cC` through :g:`O`.

.. step::

   Join apex :g:`B` to center :g:`A` of circle :g:`cA`.

.. step::

   Mark intersections :g:`H` and :g:`I` of secant :g:`BA` with :g:`cA`.

Exact Symbolic Proof & Certificate
----------------------------------

Right triangle :math:`\triangle AOB` has legs :math:`|OA| = 1/2` and :math:`|OB| = 1`, so :math:`|BA| = \sqrt{5}/2`. Since circle :g:`cA` has radius :math:`1/2` and diameter :math:`|HI| = 1`, we obtain :math:`|BH| = \frac{\sqrt{5}-1}{2} = 1/\phi` and :math:`|BI| = \frac{\sqrt{5}+1}{2} = \phi`, proving :math:`|HI|/|BH| = |BI|/|HI| = \phi`.

.. list-table:: Machine-Verified Symbolic Certificate
   :widths: 30 70
   :header-rows: 1

   * - Invariant
     - Exact Symbolic Value
   * - Primary Golden Ratio
     - :g:`HI` :math:`/` :g:`BH` :math:`= \frac{1}{2} + \frac{\sqrt{5}}{2}` on collinear triple (:g:`B`, :g:`H`, :g:`I`)
   * - Exact Segment Lengths
     - :math:`|HI| = 1`, :math:`|BH| = - \frac{1}{2} + \frac{\sqrt{5}}{2}`
   * - Rational Trigonometry :term:`Quadrances <quadrance>`
     - :math:`Q(H, I) = 1`, :math:`Q(B, H) = \frac{3}{2} - \frac{\sqrt{5}}{2}`, :math:`Q_{\text{long}}/Q_{\text{short}} = \frac{\sqrt{5}}{2} + \frac{3}{2} = \phi^2`
   * - Algebraic Number Field
     - :math:`\mathbb{Q}(\phi)`
   * - :term:`Géométrographie <geometrographie>` Loci
     - 2 given points · 1 lines · 3 circles · 0 polygons (elementary loci :math:`= 4`, Lemoine :math:`S = 12`)

Automated Divine Scan
---------------------

:mod:`geometor.divine.golden` detected **1** exact collinear golden section(s) and **0** connected golden chain(s) in this model:

- Section (:g:`I`, :g:`H`, :g:`B`): long :math:`|IH|^2 = 1` vs. short :math:`|HB|^2 = \frac{3}{2} - \frac{\sqrt{5}}{2}`

Historical Commentary & Attribution
-----------------------------------

Notice that :g:`BO` is tangent to both inner circles :g:`cA` and :g:`cC` at :g:`O`, making :math:`|BO|^2 = |BH|\cdot|BI| = 1` an immediate instance of Euclid III.36.

- **Scholarly Citations**: :cite:`Cut-the-Knot: Golden Ratio in Yin-Yang <bogomolny-yin-yang>`, :cite:`Cut-the-Knot: Golden Ratio in Geometry <bogomolny-golden-ratio>`
- **Curated Reference**: `Golden Ratio in Yin-Yang <https://www.cut-the-knot.org/do_you_know/GoldenRatioInYinYang.shtml>`_ (curated by :person:`Alexander Bogomolny <alexander-bogomolny>`, *Cut-the-Knot*, © 1996–2018)
- **Concepts**: :term:`Golden Ratio (φ) <golden-ratio>` · :term:`Golden Section <golden-section>` · :term:`Power of a Point <power-of-a-point>`

.. toctree::
   :hidden:

   code
