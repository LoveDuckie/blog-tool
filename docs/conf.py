# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Blog Tool'
copyright = '2024, Luc Shelton'
author = 'Luc Shelton'
release = '0.1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']

# Sphinx extensions
extensions = [
    'sphinx.ext.autodoc',     # Automatic documentation generation from docstrings
    'sphinx.ext.napoleon',    # Google and NumPy style docstring support
    'sphinx.ext.viewcode',    # Links to highlighted source code
]

# HTML Theme
html_theme = 'sphinx_rtd_theme'

# Path setup
import os
import sys
sys.path.insert(0, os.path.abspath('../src'))  # Modify to point to your source directory if different
