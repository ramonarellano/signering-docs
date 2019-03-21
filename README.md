# signering-docs [![Documentation Status](https://readthedocs.org/projects/signering-docs/badge/?version=latest)](https://signering-docs.readthedocs.io/en/latest/?badge=latest)

## To build:
```
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
