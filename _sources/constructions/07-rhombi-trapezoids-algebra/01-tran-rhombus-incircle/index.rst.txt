:type: construction
:order: 1
:excerpt: Let ABCD be a rhombus whose diagonals satisfy DB = 2AC, and let cO be its inscribed circle. Circle cO intersects long diagonal DB at E and F to form a 4-point golden chain: EF/FB = EB/EF = φ.
:categories: 07-rhombi-trapezoids-algebra
:tags: field-q-phi, golden-chain, tran-quang-hung

GC-07.01 · Tran Quang Hung's 2:1 Rhombus & Incircle Diagonal Division
=====================================================================

**Discoverer(s)**: :person:`Tran Quang Hung <tran-quang-hung>` | **Date**: 2015 | **Field**: :math:`\mathbb{Q}(\phi)` | **Loci**: 2 (:term:`Lemoine <geometrographie>` :math:`S = 6`)

.. enunciation::

   Let :g:`ABCD` be a rhombus whose diagonals satisfy :math:`|DB| = 2|AC|`, and let :g:`cO` be its inscribed circle. Circle :g:`cO` intersects long diagonal :g:`DB` at :g:`E` and :g:`F` to form a 4-point golden chain: :math:`|EF|/|FB| = |EB|/|EF| = \phi`.

.. picture:: 01-tran-rhombus-incircle.svg
   :alt: GC-07.01 — Tran Quang Hung's 2:1 Rhombus & Incircle Diagonal Division

Given & Constructive Steps
--------------------------

**Given**: Rhombus :g:`ABCD` centered at :g:`O` :math:`= (0,0)` with :g:`B` :math:`= (2\sqrt{5}, 0)` and :g:`A` :math:`= (0, \sqrt{5})`.

.. step::

   Construct rhombus :g:`ABCD` of side :math:`5` with semi-diagonals :math:`|OB| = 2\sqrt{5}` and :math:`|OA| = \sqrt{5}`.

.. step::

   Inscribe circle :g:`cO` of radius :math:`r = 2` tangent to all four sides of :g:`ABCD`.

.. step::

   Mark intersections :g:`E` :math:`= (-2,0)` and :g:`F` :math:`= (2,0)` of :g:`cO` with diagonal :g:`DB`.

Exact Symbolic Proof & Certificate
----------------------------------

Right triangle :math:`\triangle AOB` has legs :math:`\sqrt{5}` and :math:`2\sqrt{5}`, hypotenuse :math:`|AB| = 5`, and altitude (inradius) :math:`r = \frac{\sqrt{5}\cdot 2\sqrt{5}}{5} = 2`. Thus diameter :math:`|EF| = 4`, while :math:`|FB| = 2\sqrt{5} - 2 = 2(\sqrt{5}-1) = 4/\phi`, giving :math:`|EF|/|FB| = \phi`.

.. list-table:: Machine-Verified Symbolic Certificate
   :widths: 30 70
   :header-rows: 1

   * - Invariant
     - Exact Symbolic Value
   * - Primary Golden Ratio
     - :g:`EF` :math:`/` :g:`FB` :math:`= \frac{1}{2} + \frac{\sqrt{5}}{2}` on collinear triple (:g:`E`, :g:`F`, :g:`B`)
   * - Exact Segment Lengths
     - :math:`|EF| = 4`, :math:`|FB| = -2 + 2 \sqrt{5}`
   * - Rational Trigonometry :term:`Quadrances <quadrance>`
     - :math:`Q(E, F) = 16`, :math:`Q(F, B) = 24 - 8 \sqrt{5}`, :math:`Q_{\text{long}}/Q_{\text{short}} = \frac{\sqrt{5}}{2} + \frac{3}{2} = \phi^2`
   * - Algebraic Number Field
     - :math:`\mathbb{Q}(\phi)`
   * - :term:`Géométrographie <geometrographie>` Loci
     - 2 given points · 1 lines · 1 circles · 1 polygons (elementary loci :math:`= 2`, Lemoine :math:`S = 6`)

Automated Divine Scan
---------------------

:mod:`geometor.divine.golden` detected **2** exact collinear golden section(s) and **1** connected golden chain(s) in this model:

- Section (:g:`D`, :g:`E`, :g:`F`): long :math:`|EF|^2 = 16` vs. short :math:`|DE|^2 = 24 - 8 \sqrt{5}`
- Section (:g:`E`, :g:`F`, :g:`B`): long :math:`|EF|^2 = 16` vs. short :math:`|FB|^2 = 24 - 8 \sqrt{5}`

**Connected Golden Chains**:

- Chain (:g:`D` — :g:`E` — :g:`F` — :g:`B`) spanning 2 overlapping golden sections (progression ``< >``)

Historical Commentary & Attribution
-----------------------------------

Scaling the semi-diagonals by :math:`\sqrt{5}` makes both the rhombus side (:math:`5`) and the inradius (:math:`2`) pure rational integers.

- **Scholarly Citations**: :cite:`Cut-the-Knot: Golden Ratio in Rhombus <bogomolny-buratino8>`, :cite:`Cut-the-Knot: Golden Ratio in Geometry <bogomolny-golden-ratio>`
- **Curated Reference**: `Golden Ratio in Rhombus <https://www.cut-the-knot.org/do_you_know/Buratino8.shtml>`_ (curated by :person:`Alexander Bogomolny <alexander-bogomolny>`, *Cut-the-Knot*, © 1996–2018)
- **Concepts**: :term:`Golden Ratio (φ) <golden-ratio>` · :term:`Golden Section <golden-section>` · :term:`Golden Chain <golden-chain>`

.. toctree::
   :hidden:

   code
