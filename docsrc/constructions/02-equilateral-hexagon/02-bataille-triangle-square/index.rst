:type: construction
:order: 2
:excerpt: Erect equilateral triangle ABC and external square BCDE on opposite sides of shared base BC. Circle cCE centered at C through opposite square vertex E cuts ray AB beyond B at F so that AF/AB = AB/BF = φ.
:categories: 02-equilateral-hexagon
:tags: field-q-sqrt3-phi, michel-bataille

GC-02.02 · Michel Bataille's Equilateral Triangle & External Square
===================================================================

**Discoverer(s)**: :person:`Michel Bataille <michel-bataille>` | **Date**: 2011 | **Field**: :math:`\mathbb{Q}(\sqrt{3}, \phi)` | **Loci**: 2 (:term:`Lemoine <geometrographie>` :math:`S = 6`)

.. enunciation::

   Erect equilateral triangle :g:`ABC` and external square :g:`BCDE` on opposite sides of shared base :g:`BC`. Circle :g:`cCE` centered at :g:`C` through opposite square vertex :g:`E` cuts ray :g:`AB` beyond :g:`B` at :g:`F` so that :math:`|AF|/|AB| = |AB|/|BF| = \phi`.

.. picture:: 02-bataille-triangle-square.svg
   :alt: GC-02.02 — Michel Bataille's Equilateral Triangle & External Square

Given & Constructive Steps
--------------------------

**Given**: Shared base :g:`BC` from :g:`B` :math:`= (0, 0)` to :g:`C` :math:`= (2, 0)` of length :math:`2`.

.. step::

   Construct equilateral triangle :g:`ABC` above :g:`BC` with apex :g:`A` :math:`= (1, \sqrt{3})`.

.. step::

   Construct square :g:`BCDE` below :g:`BC` with :g:`D` :math:`= (2, -2)` and :g:`E` :math:`= (0, -2)`.

.. step::

   Draw circle :g:`cCE` centered at :g:`C` through :g:`E` (radius :math:`2\sqrt{2}`), intersecting line :g:`AB` beyond :g:`B` at :g:`F`.

Exact Symbolic Proof & Certificate
----------------------------------

Diagonal :g:`CE` of square :g:`BCDE` has quadrance :math:`Q(C, E) = 2^2 + 2^2 = 8`. Along ray :g:`AB` extended beyond :g:`B` by distance :math:`s = |BF|`, :math:`\angle CBF = 120^\circ`, so the Law of Cosines in :math:`\triangle CBF` gives :math:`s^2 + 2s + 4 = 8`, or :math:`s^2 + 2s - 4 = 0`. Thus :math:`|BF| = \sqrt{5} - 1 = 2/\phi` and :math:`|AF| = 2 + (\sqrt{5} - 1) = \sqrt{5} + 1 = 2\phi`, proving :math:`|AF|/|AB| = |AB|/|BF| = \phi`.

.. list-table:: Machine-Verified Symbolic Certificate
   :widths: 30 70
   :header-rows: 1

   * - Invariant
     - Exact Symbolic Value
   * - Primary Golden Ratio
     - :g:`AB` :math:`/` :g:`BF` :math:`= \frac{1}{2} + \frac{\sqrt{5}}{2}` on collinear triple (:g:`A`, :g:`B`, :g:`F`)
   * - Exact Segment Lengths
     - :math:`|AB| = 2`, :math:`|BF| = -1 + \sqrt{5}`
   * - Rational Trigonometry :term:`Quadrances <quadrance>`
     - :math:`Q(A, B) = 4`, :math:`Q(B, F) = 6 - 2 \sqrt{5}`, :math:`Q_{\text{long}}/Q_{\text{short}} = \frac{\sqrt{5}}{2} + \frac{3}{2} = \phi^2`
   * - Algebraic Number Field
     - :math:`\mathbb{Q}(\sqrt{3}, \phi)`
   * - :term:`Géométrographie <geometrographie>` Loci
     - 2 given points · 1 lines · 1 circles · 2 polygons (elementary loci :math:`= 2`, Lemoine :math:`S = 6`)

Automated Divine Scan
---------------------

:mod:`geometor.divine.golden` detected **1** exact collinear golden section(s) and **0** connected golden chain(s) in this model:

- Section (:g:`F`, :g:`B`, :g:`A`): long :math:`|BA|^2 = 4` vs. short :math:`|FB|^2 = 6 - 2 \sqrt{5}`

Historical Commentary & Attribution
-----------------------------------

Published by :person:`Michel Bataille <michel-bataille>` (:cite:`Bataille 2011 <bataille-2011>`, :cite:`Cut-the-Knot <ctk-bataille>`), this construction bridges the regular :math:`3`-gon and :math:`4`-gon directly to :math:`\phi`.

- **Scholarly Citations**: :cite:`Another Simple Construction of the Golden Section <bataille-2011>`, :cite:`Cut-the-Knot: From Equilateral Triangle and Square to Golden Ratio <ctk-bataille>`
- **Curated Reference**: `From Equilateral Triangle and Square to Golden Ratio <https://www.cut-the-knot.org/do_you_know/MBatailleGoldenRatio.shtml>`_ (curated by :person:`Alexander Bogomolny <alexander-bogomolny>`, *Cut-the-Knot*, © 1996–2018)
- **Concepts**: :term:`Golden Section <golden-section>` · :term:`Quadrance <quadrance>`

.. toctree::
   :hidden:

   code
