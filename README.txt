
Django and Sphinx documentation
===============================

This Django application allows you to integrate any `Sphinx
<http://sphinx.pocoo.org/>`_ documentation directly into your Django powered
website instead of just serving the static files.

It’s based on `Django’s documentation app
<http://code.djangoproject.com/browser/djangoproject.com/djangodocs>`_ and
makes it more widely usable.

django-sphinxdoc can handle multiple Sphinx projects. It takes the static body
of the documentation from the JSON files Sphinx creates and embeds them in the
content block of your site.


Requirements
------------

This app is tested with Django 1.1 and 1.2. It might also work with older
versions, but I haven’t tested it. You should also have Sphinx >= 1.0.


Installation
------------

You can either install this app with `PIP <http://pypi.python.org/pypi/pip>`_ 
(or ``easy_install``):

.. sourcecode:: bash

    $ pip install django-sphinxdoc
    $ # or:
    $ easy_install django-sphinxdoc

or download and install it manually:

.. sourcecode:: bash

    $ cd where/you/put/django-sphinxdoc/
    $ python setup.py install
    
Use `this URL <http://bitbucket.org/scherfke/django-sphinxdoc/>`_ for cloning if
you want to install this app in development mode.
    

Usage
-----

The Documentation can be found in the *docs/* directory or
`online <http://stefan.sofa-rockers.org/docs/django-sphinxdoc/>`_.
