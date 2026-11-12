geometor.divine.catalog
=======================

.. py:module:: geometor.divine.catalog

.. autoapi-nested-parse::

   Exact Symbolic Catalog of Golden Ratio Constructions & Theorems.

   Catalogs 45 geometric constructions and theorems across 7 families—curated from
   classical antiquity, *Forum Geometricorum*, *Mathematics Magazine*, *American
   Mathematical Monthly*, and Alexander Bogomolny's *Cut-the-Knot* archive—verified
   with 100% exact SymPy symbolic algebra, Rational Trigonometry quadrances, and
   automated :mod:`geometor.divine` golden-chain discovery.



Submodules
----------

.. toctree::
   :maxdepth: 1

   /modules/api/geometor/divine/catalog/apparatus/index
   /modules/api/geometor/divine/catalog/circles_sangaku/index
   /modules/api/geometor/divine/catalog/equilateral_hexagon/index
   /modules/api/geometor/divine/catalog/generate_codex/index
   /modules/api/geometor/divine/catalog/helpers/index
   /modules/api/geometor/divine/catalog/minimal_compass/index
   /modules/api/geometor/divine/catalog/pentagons_polygons/index
   /modules/api/geometor/divine/catalog/registry/index
   /modules/api/geometor/divine/catalog/render/index
   /modules/api/geometor/divine/catalog/rhombi_trapezoids_algebra/index
   /modules/api/geometor/divine/catalog/right_and_345/index
   /modules/api/geometor/divine/catalog/schema/index
   /modules/api/geometor/divine/catalog/squares_rectangles/index


Attributes
----------

.. autoapisummary::

   geometor.divine.catalog.CATALOG
   geometor.divine.catalog.CATALOG_BY_CODE
   geometor.divine.catalog.CATALOG_BY_SHORT_SLUG
   geometor.divine.catalog.CATALOG_BY_SLUG
   geometor.divine.catalog.FAMILIES
   geometor.divine.catalog.FAMILIES_BY_SLUG


Classes
-------

.. autoapisummary::

   geometor.divine.catalog.ConstructionResult
   geometor.divine.catalog.ConstructionSpec
   geometor.divine.catalog.DetectedChain
   geometor.divine.catalog.DetectedSection
   geometor.divine.catalog.FamilySpec
   geometor.divine.catalog.GeometrographieStats
   geometor.divine.catalog.GoldenCertificate


Functions
---------

.. autoapisummary::

   geometor.divine.catalog.build_construction
   geometor.divine.catalog.get_construction
   geometor.divine.catalog.get_family
   geometor.divine.catalog.iter_catalog
   geometor.divine.catalog.export_catalog_svg
   geometor.divine.catalog.render_catalog_svg
   geometor.divine.catalog.certify_construction
   geometor.divine.catalog.count_geometrographie


Package Contents
----------------

.. py:data:: CATALOG
   :type:  tuple[geometor.divine.catalog.schema.ConstructionSpec, ...]

.. py:data:: CATALOG_BY_CODE
   :type:  dict[str, geometor.divine.catalog.schema.ConstructionSpec]

.. py:data:: CATALOG_BY_SHORT_SLUG
   :type:  dict[str, geometor.divine.catalog.schema.ConstructionSpec]

.. py:data:: CATALOG_BY_SLUG
   :type:  dict[str, geometor.divine.catalog.schema.ConstructionSpec]

.. py:data:: FAMILIES
   :type:  tuple[geometor.divine.catalog.schema.FamilySpec, ...]

.. py:data:: FAMILIES_BY_SLUG
   :type:  dict[str, geometor.divine.catalog.schema.FamilySpec]

.. py:function:: build_construction(identifier: str) -> tuple[geometor.model.Model, geometor.divine.catalog.schema.GoldenCertificate]

   Build and symbolically certify a cataloged construction by identifier.


.. py:function:: get_construction(identifier: str) -> geometor.divine.catalog.schema.ConstructionSpec

   Look up a :class:`ConstructionSpec` by catalog code, ``family/slug``, or ``slug``.


.. py:function:: get_family(family_slug: str) -> geometor.divine.catalog.schema.FamilySpec

   Look up a :class:`FamilySpec` by its directory slug.


.. py:function:: iter_catalog(family_slug: str | None = None) -> collections.abc.Iterator[geometor.divine.catalog.schema.ConstructionSpec]

   Iterate over catalog entries in canonical order, optionally filtered by family.


.. py:function:: export_catalog_svg(model: geometor.model.Model, output_path: str | pathlib.Path, cert: geometor.divine.catalog.schema.GoldenCertificate | None = None, *, graphic_id: str = 'g1', title: str = 'Golden Ratio Construction', width: int = 680, height: int = 480, margin: float = 42.0, bbox: tuple[float, float, float, float] | None = None, include_guides: bool = False) -> pathlib.Path

   Write an interactive ``.euclid-graphic`` SVG for ``model`` to ``output_path``.


.. py:function:: render_catalog_svg(model: geometor.model.Model, cert: geometor.divine.catalog.schema.GoldenCertificate | None = None, *, graphic_id: str = 'g1', title: str = 'Golden Ratio Construction', width: int = 680, height: int = 480, margin: float = 42.0, bbox: tuple[float, float, float, float] | None = None, include_guides: bool = False) -> str

   Render ``model`` and optional ``cert`` into an interactive ``.euclid-graphic`` SVG.


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



.. py:class:: DetectedChain

   A connected chain of exact collinear golden sections.


   .. py:attribute:: points
      :type:  tuple[str, ...]


   .. py:attribute:: section_count
      :type:  int


   .. py:attribute:: flow
      :type:  str


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


.. py:function:: certify_construction(spec: ConstructionSpec) -> tuple[geometor.model.Model, GoldenCertificate]

   Execute ``spec.builder()`` and verify its exact symbolic golden certificate.


.. py:function:: count_geometrographie(model: geometor.model.Model) -> GeometrographieStats

   Compute Euclidean locus counts and Lemoine simplicity metrics for ``model``.


