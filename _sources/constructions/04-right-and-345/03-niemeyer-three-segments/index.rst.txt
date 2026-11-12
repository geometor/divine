:type: construction
:order: 3
:excerpt: Place segment A1B1 perpendicular to line L at A1, lean equal segment B2A2 from midpoint B2 of A1B1 onto L, and lean a third equal segment B3A3 from midpoint B3 of B2A2 onto L. Then A2 divides A1A3 in the golden ratio: A1A2/A2A3 = φ.
:categories: 04-right-and-345
:tags: field-q-sqrt3-phi, jo-niemeyer

GC-04.03 · Jo Niemeyer's Three Equal Leaning Segments
=====================================================

**Discoverer(s)**: :person:`Jo Niemeyer <jo-niemeyer>` | **Date**: 2011 | **Field**: :math:`\mathbb{Q}(\sqrt{3}, \phi)` | **Loci**: 3 (:term:`Lemoine <geometrographie>` :math:`S = 9`)

.. enunciation::

   Place segment :g:`A1B1` perpendicular to line :g:`L` at :g:`A1`, lean equal segment :g:`B2A2` from midpoint :g:`B2` of :g:`A1B1` onto :g:`L`, and lean a third equal segment :g:`B3A3` from midpoint :g:`B3` of :g:`B2A2` onto :g:`L`. Then :g:`A2` divides :g:`A1A3` in the golden ratio: :math:`|A1A2|/|A2A3| = \phi`.

.. picture:: 03-niemeyer-three-segments.svg
   :alt: GC-04.03 — Jo Niemeyer's Three Equal Leaning Segments

Given & Constructive Steps
--------------------------

**Given**: Segment :g:`A1B1` of length :math:`2` from :g:`A1` :math:`= (0,0)` to :g:`B1` :math:`= (2,0)` perpendicular to vertical line :g:`L` (:math:`x = 0`).

.. step::

   Bisect :g:`A1B1` at :g:`B2` :math:`= (1,0)` and swing circle :g:`cB2` of radius :math:`2` to meet :g:`L` at :g:`A2` :math:`= (0, \sqrt{3})`.

.. step::

   Bisect :g:`B2A2` at :g:`B3` :math:`= (\tfrac{1}{2}, \tfrac{\sqrt{3}}{2})`.

.. step::

   Swing circle :g:`cB3` of radius :math:`2` centered at :g:`B3` to meet :g:`L` above :g:`A2` at :g:`A3`.

Exact Symbolic Proof & Certificate
----------------------------------

Right triangle :math:`\triangle A1B2A2` has hypotenuse :math:`2` and leg :math:`1`, so :math:`|A1A2| = \sqrt{3}` and :g:`B3` :math:`= (\tfrac{1}{2}, \tfrac{\sqrt{3}}{2})`. Circle :g:`cB3` satisfies :math:`(x - \tfrac{1}{2})^2 + (y - \tfrac{\sqrt{3}}{2})^2 = 4`; at :math:`x = 0`, :math:`(y - \tfrac{\sqrt{3}}{2})^2 = \frac{15}{4}`, giving :math:`y_{A3} = \frac{\sqrt{3} + \sqrt{15}}{2} = \sqrt{3}\,\phi`. Hence :math:`|A1A2| = \sqrt{3}` and :math:`|A2A3| = \sqrt{3}(\phi - 1) = \sqrt{3}/\phi`, proving :math:`|A1A2|/|A2A3| = \phi`.

.. list-table:: Machine-Verified Symbolic Certificate
   :widths: 30 70
   :header-rows: 1

   * - Invariant
     - Exact Symbolic Value
   * - Primary Golden Ratio
     - :g:`A1A2` :math:`/` :g:`A2A3` :math:`= \frac{1}{2} + \frac{\sqrt{5}}{2}` on collinear triple (:g:`A1`, :g:`A2`, :g:`A3`)
   * - Exact Segment Lengths
     - :math:`|A1A2| = \sqrt{3}`, :math:`|A2A3| = \frac{- \sqrt{3} + \sqrt{15}}{2}`
   * - Rational Trigonometry :term:`Quadrances <quadrance>`
     - :math:`Q(A1, A2) = 3`, :math:`Q(A2, A3) = \frac{9}{2} - \frac{3 \sqrt{5}}{2}`, :math:`Q_{\text{long}}/Q_{\text{short}} = \frac{\sqrt{5}}{2} + \frac{3}{2} = \phi^2`
   * - Algebraic Number Field
     - :math:`\mathbb{Q}(\sqrt{3}, \phi)`
   * - :term:`Géométrographie <geometrographie>` Loci
     - 2 given points · 1 lines · 2 circles · 0 polygons (elementary loci :math:`= 3`, Lemoine :math:`S = 9`)

Automated Divine Scan
---------------------

:mod:`geometor.divine.golden` detected **1** exact collinear golden section(s) and **0** connected golden chain(s) in this model:

- Section (:g:`A1`, :g:`A2`, :g:`A3`): long :math:`|A1A2|^2 = 3` vs. short :math:`|A2A3|^2 = \frac{9}{2} - \frac{3 \sqrt{5}}{2}`

Historical Commentary & Attribution
-----------------------------------

Concrete artist Jo Niemeyer designed minimal sculptures and reliefs built from this three-bar linkage, realizing :math:`\phi` mechanically with three identical rods.

- **Scholarly Citations**: :cite:`Cut-the-Knot: Golden Ratio and Midpoints (Jo Niemeyer) <bogomolny-niemeyer>`, :cite:`Cut-the-Knot: Golden Ratio in Geometry <bogomolny-golden-ratio>`
- **Curated Reference**: `Golden Ratio in Three Equal Segments <https://www.cut-the-knot.org/do_you_know/GoldenJo.shtml>`_ (curated by :person:`Alexander Bogomolny <alexander-bogomolny>`, *Cut-the-Knot*, © 1996–2018)
- **Concepts**: :term:`Golden Ratio (φ) <golden-ratio>` · :term:`Golden Section <golden-section>` · :term:`Quadrance <quadrance>`

.. toctree::
   :hidden:

   code
