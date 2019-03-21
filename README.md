# signering-docs [![Documentation Status](https://readthedocs.org/projects/signering-docs/badge/?version=latest)](https://signering-docs.readthedocs.io/en/latest/?badge=latest)

## To build:
```
brew install python #python 3
```

Link inn python3 (legg den inn i pathen som beskrevet på [Stackoverflow](https://stackoverflow.com/a/49711594/1765749)

```
pip install sphinx_rtd_theme
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

It is important to use `wrap=preserve` to .

A bunch of links may be wrong, but it is a good start!
