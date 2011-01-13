#! /usr/bin/env python
# encoding: utf-8

from distutils.core import setup


class UltraMagicString(object):
    # Catch-22:
    # - if I return Unicode, python setup.py --long-description as well
    #   as python setup.py upload fail with a UnicodeEncodeError
    # - if I return UTF-8 string, python setup.py sdist register
    #   fails with an UnicodeDecodeError

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return self.value

    def __unicode__(self):
        return self.value.decode('UTF-8')

    def __add__(self, other):
        return UltraMagicString(self.value + str(other))

    def split(self, *args, **kw):
        return self.value.split(*args, **kw)


setup(
    name='django-sphinxdoc',
    version='1.0',
    author='Stefan Scherfke',
    author_email='stefan at sofa-rockers.org',
    description='Easily integrate Sphinx documentation into your website.',
    long_description=UltraMagicString(open('README.txt').read()),
    url='http://stefan.sofa-rockers.org/django-sphinxdoc/',
    download_url='http://bitbucket.org/scherfke/django-sphinxdoc/downloads/',
    license='BSD',
    packages=[
        'sphinxdoc',
        'sphinxdoc.management',
        'sphinxdoc.management.commands',
    ],
    package_data={
        'sphinxdoc': ['templates/sphinxdoc/*'],
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
    ],
)
