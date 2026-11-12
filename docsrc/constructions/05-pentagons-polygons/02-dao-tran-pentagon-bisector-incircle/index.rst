:type: construction
:order: 2
:excerpt: In regular pentagon ABCDE, erect line EF perpendicular to side DE at vertex E. Line EF intersects opposite non-adjacent side AB internally at F such that FB/AF = AB/FB = φ.
:categories: 05-pentagons-polygons
:tags: field-pentagonal, dao-thanh-oai, tran-quang-hung

GC-05.02 · Dao Thanh Oai's Regular Pentagon Edge Perpendicular
==============================================================

**Discoverer(s)**: :person:`Dao Thanh Oai <dao-thanh-oai>`, :person:`Tran Quang Hung <tran-quang-hung>` | **Date**: 2015 | **Field**: :math:`\mathbb{Q}(\phi, \sqrt{10 - 2\sqrt{5}})` | **Loci**: 3 (:term:`Lemoine <geometrographie>` :math:`S = 9`)

.. enunciation::

   In regular pentagon :g:`ABCDE`, erect line :g:`EF` perpendicular to side :g:`DE` at vertex :g:`E`. Line :g:`EF` intersects opposite non-adjacent side :g:`AB` internally at :g:`F` such that :math:`|FB|/|AF| = |AB|/|FB| = \phi`.

.. picture:: 02-dao-tran-pentagon-bisector-incircle.svg
   :alt: GC-05.02 — Dao Thanh Oai's Regular Pentagon Edge Perpendicular

Given & Constructive Steps
--------------------------

**Given**: Regular pentagon :g:`ABCDE` of side :math:`2` on base :g:`A` :math:`= (-1,0)`, :g:`B` :math:`= (1,0)`.

.. step::

   Construct regular pentagon :g:`ABCDE` counterclockwise on base :g:`AB`.

.. step::

   Erect line :g:`EF` perpendicular to upper-left side :g:`DE` at vertex :g:`E`.

.. step::

   Mark intersection :g:`F` of :g:`EF` with base :g:`AB`.

Exact Symbolic Proof & Certificate
----------------------------------

Interior angle :math:`\angle DEA = 108^\circ`, while :math:`\angle DEF = 90^\circ`, leaving :math:`\angle AEF = 18^\circ`. Since :math:`\angle EAF = 108^\circ`, triangle :math:`\triangle EAF` has :math:`\angle EFA = 54^\circ`. By the Law of Sines on :math:`\triangle EAF` with :math:`|EA| = 2`, :math:`|AF| = \frac{2\sin 18^\circ}{\sin 54^\circ} = \frac{2(1/(2\phi))}{\phi/2} = \frac{2}{\phi^2}`, whence :math:`|FB| = 2 - \frac{2}{\phi^2} = \frac{2}{\phi}` and :math:`|FB|/|AF| = \phi`.

.. list-table:: Machine-Verified Symbolic Certificate
   :widths: 30 70
   :header-rows: 1

   * - Invariant
     - Exact Symbolic Value
   * - Primary Golden Ratio
     - :g:`FB` :math:`/` :g:`AF` :math:`= \frac{1}{2} + \frac{\sqrt{5}}{2}` on collinear triple (:g:`A`, :g:`F`, :g:`B`)
   * - Exact Segment Lengths
     - :math:`|FB| = -1 + \sqrt{5}`, :math:`|AF| = 3 - \sqrt{5}`
   * - Rational Trigonometry :term:`Quadrances <quadrance>`
     - :math:`Q(F, B) = 6 - 2 \sqrt{5}`, :math:`Q(A, F) = 14 - 6 \sqrt{5}`, :math:`Q_{\text{long}}/Q_{\text{short}} = \frac{\sqrt{5}}{2} + \frac{3}{2} = \phi^2`
   * - Algebraic Number Field
     - :math:`\mathbb{Q}(\phi, \sqrt{10 - 2\sqrt{5}})`
   * - :term:`Géométrographie <geometrographie>` Loci
     - 2 given points · 3 lines · 0 circles · 1 polygons (elementary loci :math:`= 3`, Lemoine :math:`S = 9`)

Automated Divine Scan
---------------------

:mod:`geometor.divine.golden` detected **1** exact collinear golden section(s) and **0** connected golden chain(s) in this model:

- Section (:g:`A`, :g:`F`, :g:`B`): long :math:`|FB|^2 = 6 - 2 \sqrt{5}` vs. short :math:`|AF|^2 = 14 - 6 \sqrt{5}`

Historical Commentary & Attribution
-----------------------------------

Tran Quang Hung discovered a dual regular-pentagon division via the incircle and radius midpoint (`AnotherGoldenRatioInRegularPentagon.shtml`), reflecting the ubiquitous :math:`18^\circ\text{-}54^\circ\text{-}72^\circ` cosine ratios.

- **Scholarly Citations**: :cite:`Cut-the-Knot: Golden Ratio in Regular Pentagon <bogomolny-pentagon-dao>`, :cite:`Cut-the-Knot: Another Golden Ratio in Regular Pentagon <bogomolny-pentagon-tqh>`, :cite:`Cut-the-Knot: Golden Ratio in Geometry <bogomolny-golden-ratio>`
- **Curated Reference**: `Golden Ratio in Regular Pentagon <https://www.cut-the-knot.org/do_you_know/GoldenRatioInRegularPentagon.shtml>`_ (curated by :person:`Alexander Bogomolny <alexander-bogomolny>`, *Cut-the-Knot*, © 1996–2018)
- **Concepts**: :term:`Golden Ratio (φ) <golden-ratio>` · :term:`Golden Section <golden-section>`

.. toctree::
   :hidden:

   code
