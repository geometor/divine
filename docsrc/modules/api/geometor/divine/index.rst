geometor.divine
===============

.. py:module:: geometor.divine

.. autoapi-nested-parse::

   Tools and symbolic catalog for analyzing divine proportions in geometric models.

   **Key Components**
   - **Analysis Hook**: :func:`register_divine_hook` automatically analyzes points as they are added to a model.
   - **Golden Sections & Chains**: Exact Rational Trigonometry discovery tools (:mod:`geometor.divine.golden`).
   - **Catalog of Golden Ratio Constructions**: 45 exact symbolic constructions and theorems across 7 families (:mod:`geometor.divine.catalog`).
   - **Events**: Listeners that trigger real-time analysis on model updates.

   **Usage**
   Register the divine hook with a :class:`~geometor.model.Model` instance or build a certified catalog construction via :func:`~geometor.divine.catalog.build_construction`.



Submodules
----------

.. toctree::
   :maxdepth: 1

   /modules/api/geometor/divine/__main__/index
   /modules/api/geometor/divine/catalog/index
   /modules/api/geometor/divine/divine/index
   /modules/api/geometor/divine/events/index
   /modules/api/geometor/divine/golden/index


Attributes
----------

.. autoapisummary::

   geometor.divine.CATALOG
   geometor.divine.FAMILIES


Functions
---------

.. autoapisummary::

   geometor.divine.build_construction
   geometor.divine.get_construction
   geometor.divine.register_divine_hook


Package Contents
----------------

.. py:data:: CATALOG
   :type:  tuple[geometor.divine.catalog.schema.ConstructionSpec, ...]

.. py:data:: FAMILIES
   :type:  tuple[geometor.divine.catalog.schema.FamilySpec, ...]

.. py:function:: build_construction(identifier: str) -> tuple[geometor.model.Model, geometor.divine.catalog.schema.GoldenCertificate]

   Build and symbolically certify a cataloged construction by identifier.


.. py:function:: get_construction(identifier: str) -> geometor.divine.catalog.schema.ConstructionSpec

   Look up a :class:`ConstructionSpec` by catalog code, ``family/slug``, or ``slug``.


.. py:function:: register_divine_hook(model: geometor.model.Model) -> None

   Initialize the divine analysis by registering the listener with the model's hook.

   :param model: The model to attach the analysis hook to.


