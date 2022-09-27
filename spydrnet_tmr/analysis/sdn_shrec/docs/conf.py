# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.insert(0, os.path.abspath('..'))
import spydrnet_shrec as sdn_shrec


# -- Project information -----------------------------------------------------

project = 'SpyDrNet SHREC'
copyright = '2020, BYU Configurable Computing Lab'
author = 'BYU Configurable Computing Lab'

# The full version, including alpha/beta/rc tags
release = sdn_shrec.__release__
# The short X.Y version
version = sdn_shrec.__version__

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.todo',
    'sphinx_gallery.gen_gallery',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = None


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# -- Options for TODO --------------------------------------------------------

todo_include_todos = True
# If this is True, todo and todolist produce output, else they produce nothing. The default is False.

todo_emit_warnings = False
# If this is True, todo emits a warning for each TODO entries. The default is False.

todo_link_only = False
#If this is True, todolist produce output without file path and line, The default is False.

# -- Options for Sphinx-Gallery ----------------------------------------------

sphinx_gallery_conf = {
     'examples_dirs': os.path.join('..', 'examples'),   # path to your example scripts
     'gallery_dirs': 'auto_examples',  # path to where to save gallery generated output
}
