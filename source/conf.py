project = u'Posten signering documentation'
copyright = u'2019, Posten Norge AS'
author = u'Posten Norge AS'

version = u''
release = u'1'

extensions = ['sphinx_tabs.tabs']
templates_path = ['_templates']

from recommonmark.parser import CommonMarkParser

source_parsers = {
    '.md': CommonMarkParser,
}

source_suffix = ['.rst', '.md']
master_doc = 'index'

language = None
exclude_patterns = []
pygments_style = None

html_theme = 'sphinx_rtd_theme'
html_static_path = ['../build/html/_static']
htmlhelp_basename = 'Postensigneringdocumentationdoc'
latex_elements = {
}

latex_documents = [
    (master_doc, 'Postensigneringdocumentation.tex', u'Posten signering documentation Documentation',
     u'Posten Norge AS', 'manual'),
]

man_pages = [
    (master_doc, 'postensigneringdocumentation', u'Posten signering documentation Documentation',
     [author], 1)
]

texinfo_documents = [
    (master_doc, 'Postensigneringdocumentation', u'Posten signering documentation Documentation',
     author, 'Postensigneringdocumentation', 'One line description of project.',
     'Miscellaneous'),
]
epub_title = project
epub_exclude_files = ['search.html']
todo_include_todos = True
