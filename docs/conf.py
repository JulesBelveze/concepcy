# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
import os

import sys

sys.path.insert(0, os.path.abspath('..'))

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'concepCy'
copyright = '2022, Jules Belveze'
author = 'Jules Belveze'
release = '0.1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "sphinxext.opengraph",
    "sphinx_copybutton",
    "sphinx.ext.githubpages",
    "myst_parser",
    "nbsphinx",
    "sphinxcontrib.autodoc_pydantic"
]
autoclass_content = 'both'
templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

autodoc_pydantic_model_show_field_summary = False
autodoc_pydantic_model_show_json = False
autodoc_pydantic_settings_show_json = False

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'
html_static_path = ['_static']

html_show_sourcelink = True

html_context = {
    "display_github": True,  # Add 'Edit on Github' link instead of 'View page source'
    "github_user": "JulesBelveze",
    "github_repo": project,
    "github_version": "master",
    "conf_py_path": "./",
}

source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}

html_favicon = "_static/concepcy.png"
html_theme_options = {
    "light_logo": "concepcy.png",
    "dark_logo": "concepcy.png",
    "light_css_variables": {
        "color-brand-primary": "#547fff",
        "color-brand-content": "#547fff",
    },
    "dark_css_variables": {
        "color-brand-primary": "#547fff",
        "color-brand-content": "#547fff",
    },
    "sidebar_hide_name": True,
    "navigation_with_keys": True,
}