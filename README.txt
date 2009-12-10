
Django Last.fm access
=====================

This is a small Django application that allows you to access Last.fm and
embed e.g. your recently listened tracks or you top artists on your website.

Currently you can get your
* recently listened tracks
* weekly artist chart
* top artists (for a definable period)

The application consists of two main parts: The first one is a view, that
retrieves the data from Last.fm, processes it and returns it as a JSON encoded
dict. The second one is a template tag that embeds some AJAX code into your
website. This code will call the view and display the artist images or album
covers. This mechanism prevents the Last.fm servers from slowing down your
blazingly fast Django site … ;-)


Requirements
------------

This app is tested with Django 1.1. It might also work with older versions, but
I haven’t tested it. 
`Setuptools <http://pypi.python.org/pypi/setuptools>`_ is required to install this app.

If you want to run the tests, you’ll need to install `Mock <http://www.voidspace.org.uk/python/mock/>`_.

There are no other requirements.


Installation
------------

If you read this, you have probably managed to extract the archive containing
these files. Next, open a Terminal and `cd` to the directory containing this
file (e.g. ``cd ~/Downloads/django-lastfm``). Then execute::

    python setup.py install
    
If you checked out the repository and always want to use the newest version,
type::

    python setup.py develop
    

Usage
-----

Documentation on how to use this app can be found in the *docs/* directory.
