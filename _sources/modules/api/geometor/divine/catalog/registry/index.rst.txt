geometor.divine.catalog.registry
================================

.. py:module:: geometor.divine.catalog.registry

.. autoapi-nested-parse::

   Master registry of the 7 geometric families and 45 cataloged constructions.

   Provides :data:`FAMILIES`, :data:`CATALOG`, :data:`CATALOG_BY_SLUG`,
   :data:`CATALOG_BY_CODE`, :func:`get_construction`, :func:`build_construction`,
   and :func:`iter_catalog` for programmatic symbolic evaluation, codex generation,
   and automated regression testing.



Attributes
----------

.. autoapisummary::

   geometor.divine.catalog.registry.FAMILIES
   geometor.divine.catalog.registry.FAMILIES_BY_SLUG
   geometor.divine.catalog.registry.CATALOG
   geometor.divine.catalog.registry.CATALOG_BY_SLUG
   geometor.divine.catalog.registry.CATALOG_BY_SHORT_SLUG
   geometor.divine.catalog.registry.CATALOG_BY_CODE


Functions
---------

.. autoapisummary::

   geometor.divine.catalog.registry.get_family
   geometor.divine.catalog.registry.get_construction
   geometor.divine.catalog.registry.build_construction
   geometor.divine.catalog.registry.iter_catalog


Module Contents
---------------

.. py:data:: FAMILIES
   :type:  tuple[geometor.divine.catalog.schema.FamilySpec, ...]

.. py:data:: FAMILIES_BY_SLUG
   :type:  dict[str, geometor.divine.catalog.schema.FamilySpec]

.. py:data:: CATALOG
   :type:  tuple[geometor.divine.catalog.schema.ConstructionSpec, ...]

.. py:data:: CATALOG_BY_SLUG
   :type:  dict[str, geometor.divine.catalog.schema.ConstructionSpec]

.. py:data:: CATALOG_BY_SHORT_SLUG
   :type:  dict[str, geometor.divine.catalog.schema.ConstructionSpec]

.. py:data:: CATALOG_BY_CODE
   :type:  dict[str, geometor.divine.catalog.schema.ConstructionSpec]

.. py:function:: get_family(family_slug: str) -> geometor.divine.catalog.schema.FamilySpec

   Look up a :class:`FamilySpec` by its directory slug.


.. py:function:: get_construction(identifier: str) -> geometor.divine.catalog.schema.ConstructionSpec

   Look up a :class:`ConstructionSpec` by catalog code, ``family/slug``, or ``slug``.


.. py:function:: build_construction(identifier: str) -> tuple[geometor.model.Model, geometor.divine.catalog.schema.GoldenCertificate]

   Build and symbolically certify a cataloged construction by identifier.


.. py:function:: iter_catalog(family_slug: str | None = None) -> collections.abc.Iterator[geometor.divine.catalog.schema.ConstructionSpec]

   Iterate over catalog entries in canonical order, optionally filtered by family.


