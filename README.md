django-sphinxdoc – Embed your Sphinx docs into your Django site
===============================================================

This Django application allows you to integrate any
[Sphinx](http://www.sphinx-doc.org/en/master/) documentation directly into your
Django powered website instead of just serving the static files.

Django-sphinxdoc can handle multiple Sphinx projects and offers
a [Haystack](http://haystacksearch.org/) powered search.


Requirements
------------

This app requires Python ≥ 3.6, Django ≥ 2.0, Sphinx ≥ 1.0 and
Haystack ≥ 2.8.0.


Installation
------------

Just use [PIP](https://pip.pypa.io/en/stable/):

```console
$ pip install django-sphinxdoc
```

If you want the latest development version:

```console
$ git clone git@gitlab.com:sscherfke/django-sphinxdoc.git
$ cd django-sphinxdoc
$ mkvirtualenv django-sphinxdoc
$ pip install -e .
```


Usage
-----

The documentation can be found in the `docs/` directory or at
https://django-sphinxdoc.readthedocs.io/en/latest/.
