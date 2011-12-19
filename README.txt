
Django and Sphinx documentation
===============================

This Django application allows you to integrate any `Sphinx
<http://sphinx.pocoo.org/>`_ documentation directly into your Django powered
website instead of just serving the static files.

Django-sphinxdoc can handle multiple Sphinx projects and offers a `Haystack
<http://haystacksearch.org/>`_ powered search. Future versions will enable
comments and add RSS feeds.


Requirements
------------

This app is tested with Django >= 1.1. You also need `Sphinx
<http://sphinx.pocoo.org/>`_ >= 1.0 and `Haystack
<http://haystacksearch.org/>`_.


Installation
------------

You can either install this app with `PIP <http://pypi.python.org/pypi/pip>`_::

    $ pip install django-sphinxdoc

or download and install it manually::

    $ cd where/you/put/django-sphinxdoc/
    $ python setup.py install

Use `this URL <http://bitbucket.org/scherfke/django-sphinxdoc/>`_ for cloning
if you want to install this app in development mode.


Usage
-----

The Documentation can be found in the *docs/* directory or
`online <http://stefan.sofa-rockers.org/docs/django-sphinxdoc/>`_.
