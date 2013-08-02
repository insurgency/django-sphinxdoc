===============================================================
django-sphinxdoc – Embed your Sphinx docs into your Django site
===============================================================

This Django application allows you to integrate any `Sphinx
<http://sphinx.pocoo.org/>`_ documentation directly into your Django powered
website instead of just serving the static files.

Django-sphinxdoc can handle multiple Sphinx projects and offers a `Haystack
<http://haystacksearch.org/>`_ powered search. Future versions will enable
comments and add RSS feeds.


Requirements
------------

This app requires Django >= 1.4, `Sphinx <http://sphinx.pocoo.org/>`_ >= 1.0
and `Haystack <http://haystacksearch.org/>`_ >= 2.1.0.


Installation
------------

Just use `PIP <http://pypi.python.org/pypi/pip>`_:

.. sourcecode:: bash

    $ pip install django-sphinxdoc

If you want the lates development version, isntall it from Bitbucket:

.. sourcecode:: bash

    $ pip install https://ssc@bitbucket.org/ssc/django-sphinxdoc
    $ # or
    $ hg clone ssh://hg@bitbucket.org/ssc/django-sphinxdoc
    $ pip install -e django-sphinxdoc


Usage
-----

The Documentation can be found in the *docs/* directory or
`online <http://stefan.sofa-rockers.org/docs/django-sphinxdoc/>`_.
