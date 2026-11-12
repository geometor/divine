:type: construction
:order: 1
:excerpt: Let ABC be an equilateral triangle inscribed in circle cO, and let L and M be the midpoints of sides AB and AC. Extending midline LM to meet circumcircle cO at X and Y divides the chord in the golden ratio: LM/MY = LY/LM = φ.
:categories: 02-equilateral-hexagon
:tags: field-q-sqrt3-phi, golden-chain, george-odom, h-s-m-coxeter

GC-02.01 · George Odom's Equilateral Midline & Circumcircle Chord (1983)
========================================================================

**Discoverer(s)**: :person:`George Odom <george-odom>`, :person:`H. S. M. Coxeter <h-s-m-coxeter>` | **Date**: 1983 | **Field**: :math:`\mathbb{Q}(\sqrt{3}, \phi)` | **Loci**: 2 (:term:`Lemoine <geometrographie>` :math:`S = 6`)

.. enunciation::

   Let :g:`ABC` be an equilateral triangle inscribed in circle :g:`cO`, and let :g:`L` and :g:`M` be the midpoints of sides :g:`AB` and :g:`AC`. Extending midline :g:`LM` to meet circumcircle :g:`cO` at :g:`X` and :g:`Y` divides the chord in the golden ratio: :math:`|LM|/|MY| = |LY|/|LM| = \phi`.

.. picture:: 01-odom-equilateral.svg
   :alt: GC-02.01 — George Odom's Equilateral Midline & Circumcircle Chord (1983)

Given & Constructive Steps
--------------------------

**Given**: Equilateral triangle :g:`ABC` with vertices :g:`A` :math:`= (0, 2)`, :g:`B` :math:`= (-\sqrt{3}, -1)`, :g:`C` :math:`= (\sqrt{3}, -1)` on circumcircle :g:`cO` of radius :math:`2`.

.. step::

   Inscribe equilateral triangle :g:`ABC` of side :math:`2\sqrt{3}` in circle :g:`cO`.

.. step::

   Mark midpoints :g:`L` :math:`= (-\tfrac{\sqrt{3}}{2}, \tfrac{1}{2})` of :g:`AB` and :g:`M` :math:`= (\tfrac{\sqrt{3}}{2}, \tfrac{1}{2})` of :g:`AC`.

.. step::

   Draw line :g:`LM` parallel to :g:`BC`, intersecting circumcircle :g:`cO` at :g:`X` :math:`= (-\tfrac{\sqrt{15}}{2}, \tfrac{1}{2})` and :g:`Y` :math:`= (\tfrac{\sqrt{15}}{2}, \tfrac{1}{2})`.

Exact Symbolic Proof & Certificate
----------------------------------

Let :math:`a = |LM| = |AM| = |MC| = \sqrt{3}` and :math:`b = |XL| = |MY|`. By Euclid's Intersecting Chords Theorem (III.35) applied to chords :g:`XY` and :g:`AC` at :g:`M`, :math:`|XM| \cdot |MY| = |AM| \cdot |MC|`, hence :math:`(a + b)b = a^2`. Dividing by :math:`b^2` yields :math:`(a/b)^2 - (a/b) - 1 = 0`, proving :math:`|LM|/|MY| = a/b = \phi` and forming a symmetric 4-point golden chain :math:`(X, L, M, Y)`.

.. list-table:: Machine-Verified Symbolic Certificate
   :widths: 30 70
   :header-rows: 1

   * - Invariant
     - Exact Symbolic Value
   * - Primary Golden Ratio
     - :g:`LM` :math:`/` :g:`MY` :math:`= \frac{1}{2} + \frac{\sqrt{5}}{2}` on collinear triple (:g:`L`, :g:`M`, :g:`Y`)
   * - Exact Segment Lengths
     - :math:`|LM| = \sqrt{3}`, :math:`|MY| = \frac{- \sqrt{3} + \sqrt{15}}{2}`
   * - Rational Trigonometry :term:`Quadrances <quadrance>`
     - :math:`Q(L, M) = 3`, :math:`Q(M, Y) = \frac{9}{2} - \frac{3 \sqrt{5}}{2}`, :math:`Q_{\text{long}}/Q_{\text{short}} = \frac{\sqrt{5}}{2} + \frac{3}{2} = \phi^2`
   * - Algebraic Number Field
     - :math:`\mathbb{Q}(\sqrt{3}, \phi)`
   * - :term:`Géométrographie <geometrographie>` Loci
     - 3 given points · 1 lines · 1 circles · 1 polygons (elementary loci :math:`= 2`, Lemoine :math:`S = 6`)

Automated Divine Scan
---------------------

:mod:`geometor.divine.golden` detected **2** exact collinear golden section(s) and **1** connected golden chain(s) in this model:

- Section (:g:`X`, :g:`L`, :g:`M`): long :math:`|LM|^2 = 3` vs. short :math:`|XL|^2 = \frac{9}{2} - \frac{3 \sqrt{5}}{2}`
- Section (:g:`L`, :g:`M`, :g:`Y`): long :math:`|LM|^2 = 3` vs. short :math:`|MY|^2 = \frac{9}{2} - \frac{3 \sqrt{5}}{2}`

**Connected Golden Chains**:

- Chain (:g:`X` — :g:`L` — :g:`M` — :g:`Y`) spanning 2 overlapping golden sections (progression ``< >``)

Historical Commentary & Attribution
-----------------------------------

Discovered in the early 1980s by artist and amateur geometer :person:`George Odom <george-odom>` at the Hudson River Psychiatric Center and communicated to :person:`H. S. M. Coxeter <h-s-m-coxeter>`, who posed it as Problem E3007 in the *American Mathematical Monthly* (:cite:`Odom & Coxeter 1983 <odom-coxeter-1983>`), Odom's construction sparked an entire modern genre of equilateral-triangle golden sections.

- **Scholarly Citations**: :cite:`Elementary Problem E3007 <odom-coxeter-1983>`, :cite:`Cut-the-Knot: Golden Ratio in Geometry <bogomolny-golden-ratio>`
- **Curated Reference**: `Golden Ratio in Geometry — George Odom's Construction <https://www.cut-the-knot.org/do_you_know/GoldenRatio.shtml#Odom>`_ (curated by :person:`Alexander Bogomolny <alexander-bogomolny>`, *Cut-the-Knot*, © 1996–2018)
- **Concepts**: :term:`Intersecting Chords Theorem <intersecting-chords-theorem>` · :term:`Golden Section <golden-section>` · :term:`Golden Chain <golden-chain>`

.. toctree::
   :hidden:

   code
