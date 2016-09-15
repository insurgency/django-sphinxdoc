===============================================================
django-sphinxdoc – Embed your Sphinx docs into your Django site
===============================================================

This Django application allows you to integrate any `Sphinx
<http://sphinx.pocoo.org/>`_ documentation directly into your Django powered
website instead of just serving the static files.

Django-sphinxdoc can handle multiple Sphinx projects and offers a `Haystack
<http://haystacksearch.org/>`_ powered search.


Requirements
------------

This app requires Django >= 1.6, Sphinx >= 1.0 and Haystack >= 2.1.


Installation
------------

Just use `PIP <http://pypi.python.org/pypi/pip>`_:

.. sourcecode:: bash

    $ pip install django-sphinxdoc

If you want the latest development version, install it from Bitbucket
with:

.. sourcecode:: bash

    $ pip install https://ssc@bitbucket.org/sscherfke/django-sphinxdoc

or

.. sourcecode:: bash

    $ hg clone ssh://hg@bitbucket.org/sscherfke/django-sphinxdoc
    $ pip install -e django-sphinxdoc


Usage
-----

The documentation can be found in the *docs/* directory or at `<http://django-sphinxdoc.readthedocs.io/en/latest/>`_.