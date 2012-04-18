#! /usr/bin/env python
from distutils.core import setup
import sys
reload(sys).setdefaultencoding('Utf-8')


setup(
    name='django-sphinxdoc',
    version='1.1',
    author='Stefan Scherfke',
    author_email='stefan at sofa-rockers.org',
    description='Easily integrate Sphinx documentation into your website.',
    long_description=open('README.txt').read(),
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
