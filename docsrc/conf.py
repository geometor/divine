"""Sphinx configuration for GEOMETOR • divine."""

from __future__ import annotations

from pathlib import Path
import sys

_REPO_ROOT = Path(__file__).resolve().parents[1]
_WORKSPACE_ROOT = _REPO_ROOT.parent
for _extra_path in (
    _REPO_ROOT / "src",
    _WORKSPACE_ROOT / "model" / "src",
    _WORKSPACE_ROOT / "explorer" / "src",
    _WORKSPACE_ROOT / ".venv" / "lib" / "python3.13" / "site-packages",
):
    if _extra_path.exists() and str(_extra_path) not in sys.path:
        sys.path.insert(0, str(_extra_path))

from photon_platform.publish.global_conf import *  # noqa: E402, F403
import geometor.divine as module  # noqa: E402

version = module.__version__

org = "geometor"
org_name = "GEOMETOR"

repo = "divine"
repo_name = "divine"

setup_globals(org, org_name, repo, repo_name)  # noqa: F405

html_theme = "foundation"
html_static_path = ["_static"]
html_css_files = ["custom.css"]
html_logo = None
autoapi_add_toctree_entry = False
napoleon_use_ivar = True
if "overview/intro.rst" not in exclude_patterns:  # noqa: F405
    exclude_patterns.append("overview/intro.rst")  # noqa: F405
suppress_warnings = ["autoapi.python_import_resolution", "toc.not_included"]
