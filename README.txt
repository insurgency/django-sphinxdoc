
Django and Sphinx documentation
===============================

This Django application allows you to integrate any `Sphinx
<http://sphinx.pocoo.org/>`_ documentation directly into your Django powered
website instead of just serving the static files.

It’s based on `Django’s documentation app
<http://code.djangoproject.com/browser/djangoproject.com/djangodocs>`_ and
makes it more widely usable.

django-sphinxdoc can handle multiple Sphinx projects (called “apps” from now
on). It takes the static body of the documentation from the JSON files Sphinx
creates and embeds them in the content block of your site.


Requirements
------------

This app is tested with Django 1.1. It might also work with older versions, but
I haven’t tested it.

There are no other requirements.


Installation
------------

If you read this, you have probably managed to extract the archive containing
these files. Next, open a Terminal and `cd` to the directory containing this
file (e.g. ``cd ~/Downloads/django-sphinxdoc``). Then execute::

    python setup.py install
    
If you checked out the repository and always want to use the newest version,
type::

    pip install -e path/to/django-sphinxdoc
    

Usage
-----

The Documentation can be found in the *docs/* directory or
`online <http://stefan.sofa-rockers.org/docs/django-sphinxdoc/>`_.
