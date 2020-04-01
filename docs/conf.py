import os
import sys

sys.path.insert(0, os.path.abspath("../"))

project = "neo-cli"
copyright = "2019, BiznetGio"
author = "BiznetGio"
version = ""
templates_path = ["_templates"]
extensions = ["sphinx.ext.autodoc", "sphinx.ext.doctest"]
source_suffix = ".rst"
master_doc = "index"
pygments_style = "sphinx"
html_theme = "alabaster"
pygments_style = "sphinx"
