# signering-docs [![Documentation Status](https://readthedocs.org/projects/signering-docs/badge/?version=latest)](https://signering-docs.readthedocs.io/en/latest/?badge=latest)

## To build:

### 1. Installer Python
```
brew install python #python 3
```
### 2. Link Python 3

Link ``python3`` as described in [Stackoverflow](https://stackoverflow.com/a/49711594/1765749). By adding it first in path, it will be chosen before the really old one installed by default on macOS.

### 3. Install all dependencies needed for the documentation
```
pip install sphinx_rtd_theme
pip install recommonmark
pip install sphinx-tabs
pip install sphinx-autobuild
make html
```

To run with autobuild as webserver:
```
sphinx-autobuild source build/html
```

## To convert markdown to reStructuredText
```
brew install pandoc
pandoc manuell-portal-integrasjon.md --from gfm --to rst -s -o manuell-portal-integrasjon.rst --wrap=preserve
```

It is important to use `wrap=preserve` to avoid splitting one-liners into multiple lines.
