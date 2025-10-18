================
GEOMETOR • divine
================

.. image:: https://img.shields.io/pypi/v/geometor-divine.svg
   :target: https://pypi.python.org/pypi/geometor-divine
.. image:: https://img.shields.io/github/license/geometor/divine.svg
   :target: https://github.com/geometor/divine/blob/main/LICENSE

A Python library for analyzing geometor.model constructions.

Overview
--------

The `divine` library provides tools to identify golden sections, harmonic ranges, and other geometric relationships within a `geometor.model` construction. It is used by the Explorer to provide real-time analysis.

Key Features
------------

- **Golden Section Analysis:** Identifies points that divide segments into the golden ratio.
- **Harmonic Range Analysis:** Analyzes harmonic ranges within lines.
- **Chain and Group Analysis:** Finds chains of connected golden sections and groups them by various criteria.

Key Files
---------

-   `divine.py`: Main module containing the core analysis functions.
-   `golden/`: A sub-package for finding and analyzing golden sections.
-   `events.py`: Manages the event handling for analysis updates.

Usage
-----

The `divine` library is typically used in conjunction with `geometor.model` and `geometor.explorer`. The `explorer` application automatically calls the `divine` analysis functions when a model is updated.

Contributing
------------

Contributions are welcome! Please see our `GitHub issues <https://github.com/geometor/divine/issues>`_ for ways to contribute.

License
-------

**geometor-divine** is licensed under the MIT License. See the `LICENSE` file for more details.