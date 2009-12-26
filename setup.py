#! /usr/bin/env python
# encoding: utf-8

from setuptools import setup, find_packages


import lastfm


setup(name='django-sphinxdoc',
    version=lastfm.__version__,
    description='Easily integrate Sphinx documentation into your website.',
    author='Stefan Scherfke',
    author_email='',
    license='BSD',
    url='http://stefan.sofa-rockers.org/django-sphinxdoc/',
    download_url='http://bitbucket.org/scherfke/django-sphinxdoc/downloads/',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities'],
)
