"""Sphinx configuration."""
project = "Pynequa"
author = "Anish Bhusal"
copyright = "2023, NASA-IMPACT"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_click"
]
autodoc_typehints = "description"
