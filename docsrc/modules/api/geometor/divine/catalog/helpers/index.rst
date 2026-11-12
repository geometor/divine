geometor.divine.catalog.helpers
===============================

.. py:module:: geometor.divine.catalog.helpers

.. autoapi-nested-parse::

   Shared exact symbolic construction helpers for :mod:`geometor.divine.catalog`.



Functions
---------

.. autoapisummary::

   geometor.divine.catalog.helpers.new_catalog_model
   geometor.divine.catalog.helpers.make_result


Module Contents
---------------

.. py:function:: new_catalog_model(name: str) -> geometor.model.Model

   Create a deterministic, exact symbolic :class:`~geometor.model.Model`.


.. py:function:: make_result(model: geometor.model.Model, primary_long: tuple[str, str], primary_short: tuple[str, str], primary_collinear: tuple[str, str, str]) -> geometor.divine.catalog.schema.ConstructionResult

   Register ``primary_collinear`` on ``model`` and bundle a :class:`ConstructionResult`.


