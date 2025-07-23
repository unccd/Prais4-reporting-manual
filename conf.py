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

# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = "PRAIS4 Reporting Manual"
copyright = "2025, UNCCD"
author = "United Nations Convention to Combat Desertification (UNCCD)"


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "myst_parser",
    "sphinx.ext.autosummary",
    "sphinxnotes.strike",
    "linuxdoc.rstFlatTable",  # https://return42.github.io/linuxdoc/linuxdoc-howto/table-markup.html#flat-table
    # 'sphinx.ext.mathjax',  # https://www.sphinx-doc.org/en/master/usage/extensions/math.html#module-sphinx.ext.mathjax
    "sphinx.ext.ifconfig",  # https://www.sphinx-doc.org/en/master/usage/extensions/ifconfig.html
    "docxbuilder",  # https://docxbuilder.readthedocs.io/en/latest/docxbuilder.html
]

myst_enable_extensions = [
    "deflist",  # https://myst-parser.readthedocs.io/en/latest/syntax/optional.html#definition-lists
    "dollarmath",  # https://myst-parser.readthedocs.io/en/stable/syntax/optional.html#dollar-delimited-math
    "html_image",  # https://myst-parser.readthedocs.io/en/latest/syntax/optional.html#images
    "linkify",  # https://myst-parser.readthedocs.io/en/latest/syntax/optional.html#linkify
    "replacements",  # https://myst-parser.readthedocs.io/en/latest/syntax/optional.html#typography
    "smartquotes",  # https://myst-parser.readthedocs.io/en/latest/syntax/optional.html#typography
    "substitution",  # https://myst-parser.readthedocs.io/en/latest/syntax/optional.html#substitutions-with-jinja2
    "tasklist",  # https://myst-parser.readthedocs.io/en/latest/syntax/optional.html#task-lists
]

myst_substitutions = {
    "br": r"""
  ```{raw} html
  <br>
  ```
  ```{raw} latex
  \mbox{}\newline
  ```
  """,
    "pagebreak": r"""
  ```{raw} latex
  \newpage
  ```
  """,
    "smallertext": r"""
  ```{rst-class} smaller-text
  ```

  ```{raw} latex
    \small
  ```
  """,
    "smalltext": r"""
  ```{rst-class} small-text
  ```

  ```{raw} latex
    \scriptsize
  ```
  """,
}

# See also https://pypi.org/project/cloud_sptheme/

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = [
    "_build",
    "build",
    "Thumbs.db",
    ".DS_Store",
    ".venv",
    "README.md",
    "backstopjs",
]
# see https://github.com/sphinx-doc/sphinx/issues/2066#issuecomment-474587560

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

html_css_files = ["css/custom.css", "css/rtl.css"]

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
html_theme_options = {
    "style_nav_header_background": "#ff7100",
    "collapse_navigation": False,
    "version_selector": False,
    "language_selector": True,
    "logo_only": True,
    "prev_next_buttons_location": "top",
    "vcs_pageview_mode": "edit",
    "style_external_links": True,
}

html_context = {
    "display_github": True,
    "github_user": "unccd",
    "github_repo": "Prais4-reporting-manual",
    "github_version": "master",
    "conf_py_path": "/",
    "current_version": "latest",
}

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
html_title = "PRAIS4 Reporting Manual"

# A shorter title for the navigation bar.  Default is the same as html_title.
html_short_title = "PRAIS4"

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = "img/unccd_logo.png"

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = "img/favicon.ico"

# see https://docs.readthedocs.io/en/stable/guides/pdf-non-ascii-languages.html
latex_engine = "xelatex"

FONT_DIR = "_fonts"
fonts = [file for file in os.listdir(FONT_DIR)]
latex_additional_files = [f"{FONT_DIR}/{font}" for font in fonts]
latex_additional_files.append("latex_preamble.tex.txt")

# latex_toplevel_sectioning='chapter'
latex_use_modindex = False

latex_elements = {
    "papersize": "a4paper",
    "pointsize": "10pt",
    "fncychap": "\\usepackage[Bjarne]{fncychap}",
    # alternative styles: Bjarne (default), Rejne, Lenny, Glenn, Conny, Bjornstrup, Sonny.
    "fontenc": "\\usepackage{fontspec}",
    "figure_align": "H",
    "sphinxsetup": "hmargin=0.5in, vmargin={1in,1in}, marginpar=0.5in",
    "preamble": r"\input{latex_preamble.tex.txt}",
}

pdf_documents = [
    ("index", "PRAIS4_user_manual", "PRAIS4 User Manual", "UNCCD", "2021-06-15"),
]

# Enable numfig for automatic numbering of table
# Also adjust captionsetup in latex_elements for the PDF output
numfig = False

numfig_format = {
    "table": "Table %s",
}
