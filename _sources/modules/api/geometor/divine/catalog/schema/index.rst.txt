geometor.divine.catalog.schema
==============================

.. py:module:: geometor.divine.catalog.schema

.. autoapi-nested-parse::

   Data schemas and exact symbolic certification for the Golden Ratio Catalog.

   Every cataloged construction in :mod:`geometor.divine.catalog` returns an exact
   symbolic :class:`~geometor.model.Model` together with a verified
   :class:`GoldenCertificate` recording exact SymPy lengths, Rational Trigonometry
   quadrances, Lemoine *Géométrographie* step metrics, algebraic number field
   membership, and all golden sections and chains discovered automatically by
   :mod:`geometor.divine.golden`.



Classes
-------

.. autoapisummary::

   geometor.divine.catalog.schema.GeometrographieStats
   geometor.divine.catalog.schema.DetectedSection
   geometor.divine.catalog.schema.DetectedChain
   geometor.divine.catalog.schema.GoldenCertificate
   geometor.divine.catalog.schema.ConstructionResult
   geometor.divine.catalog.schema.FamilySpec
   geometor.divine.catalog.schema.ConstructionSpec


Functions
---------

.. autoapisummary::

   geometor.divine.catalog.schema.count_geometrographie
   geometor.divine.catalog.schema.certify_construction


Module Contents
---------------

.. py:class:: GeometrographieStats

   Constructive step metrics in the tradition of Émile Lemoine's *Géométrographie*.


   .. py:attribute:: given_points
      :type:  int


   .. py:attribute:: constructed_lines
      :type:  int


   .. py:attribute:: constructed_circles
      :type:  int


   .. py:attribute:: constructed_segments
      :type:  int


   .. py:attribute:: constructed_polygons
      :type:  int


   .. py:attribute:: elementary_loci
      :type:  int


   .. py:attribute:: lemoine_simplicity
      :type:  int


.. py:class:: DetectedSection

   An exact collinear golden section discovered by :mod:`geometor.divine.golden`.


   .. py:attribute:: points
      :type:  tuple[str, str, str]


   .. py:attribute:: long_segment
      :type:  tuple[str, str]


   .. py:attribute:: short_segment
      :type:  tuple[str, str]


   .. py:attribute:: q_long
      :type:  sympy.Expr


   .. py:attribute:: q_short
      :type:  sympy.Expr


.. py:class:: DetectedChain

   A connected chain of exact collinear golden sections.


   .. py:attribute:: points
      :type:  tuple[str, ...]


   .. py:attribute:: section_count
      :type:  int


   .. py:attribute:: flow
      :type:  str


.. py:class:: GoldenCertificate

   Machine-verified exact symbolic certificate for a cataloged construction.


   .. py:attribute:: slug
      :type:  str


   .. py:attribute:: catalog_code
      :type:  str


   .. py:attribute:: family_slug
      :type:  str


   .. py:attribute:: title
      :type:  str


   .. py:attribute:: primary_long
      :type:  tuple[str, str]


   .. py:attribute:: primary_short
      :type:  tuple[str, str]


   .. py:attribute:: primary_collinear
      :type:  tuple[str, str, str]


   .. py:attribute:: length_long
      :type:  sympy.Expr


   .. py:attribute:: length_short
      :type:  sympy.Expr


   .. py:attribute:: ratio_expr
      :type:  sympy.Expr


   .. py:attribute:: q_long
      :type:  sympy.Expr


   .. py:attribute:: q_short
      :type:  sympy.Expr


   .. py:attribute:: quadrance_ratio
      :type:  sympy.Expr


   .. py:attribute:: number_field
      :type:  str


   .. py:attribute:: number_field_text
      :type:  str


   .. py:attribute:: stats
      :type:  GeometrographieStats


   .. py:attribute:: detected_sections
      :type:  tuple[DetectedSection, ...]


   .. py:attribute:: detected_chains
      :type:  tuple[DetectedChain, ...]


.. py:class:: ConstructionResult

   Raw output returned by an individual symbolic construction builder.


   .. py:attribute:: model
      :type:  geometor.model.Model


   .. py:attribute:: primary_long
      :type:  tuple[str, str]


   .. py:attribute:: primary_short
      :type:  tuple[str, str]


   .. py:attribute:: primary_collinear
      :type:  tuple[str, str, str]


.. py:class:: FamilySpec

   Metadata describing one of the seven geometric families in the catalog.


   .. py:attribute:: slug
      :type:  str


   .. py:attribute:: code_prefix
      :type:  str


   .. py:attribute:: order
      :type:  int


   .. py:attribute:: title
      :type:  str


   .. py:attribute:: short_title
      :type:  str


   .. py:attribute:: subtitle
      :type:  str


   .. py:attribute:: summary
      :type:  str


   .. py:attribute:: overview_rst
      :type:  str


.. py:class:: ConstructionSpec

   Complete catalog specification for a single Golden Ratio construction or theorem.


   .. py:attribute:: slug
      :type:  str


   .. py:attribute:: catalog_code
      :type:  str


   .. py:attribute:: family_slug
      :type:  str


   .. py:attribute:: order
      :type:  int


   .. py:attribute:: title
      :type:  str


   .. py:attribute:: short_title
      :type:  str


   .. py:attribute:: discoverers
      :type:  tuple[str, ...]


   .. py:attribute:: year
      :type:  str


   .. py:attribute:: citations
      :type:  tuple[str, ...]


   .. py:attribute:: ctk_url
      :type:  str


   .. py:attribute:: ctk_title
      :type:  str


   .. py:attribute:: number_field
      :type:  str


   .. py:attribute:: number_field_text
      :type:  str


   .. py:attribute:: enunciation
      :type:  str


   .. py:attribute:: given_prose
      :type:  str


   .. py:attribute:: steps_prose
      :type:  tuple[str, ...]


   .. py:attribute:: proof_prose
      :type:  str


   .. py:attribute:: notes_prose
      :type:  str


   .. py:attribute:: terms
      :type:  tuple[str, ...]


   .. py:attribute:: builder
      :type:  collections.abc.Callable[[], ConstructionResult]


   .. py:attribute:: svg_bbox
      :type:  tuple[float, float, float, float] | None
      :value: None



.. py:function:: count_geometrographie(model: geometor.model.Model) -> GeometrographieStats

   Compute Euclidean locus counts and Lemoine simplicity metrics for ``model``.


.. py:function:: certify_construction(spec: ConstructionSpec) -> tuple[geometor.model.Model, GoldenCertificate]

   Execute ``spec.builder()`` and verify its exact symbolic golden certificate.


