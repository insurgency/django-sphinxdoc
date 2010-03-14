#! /usr/bin/env python
# encoding: utf-8

from distutils.core import setup


setup(
    name='django-sphinxdoc',
    version='0.3.2',
    author='Stefan Scherfke',
    author_email='stefan at sofa-rockers.org',
    description='Easily integrate Sphinx documentation into your website.',
    # long_description=open('README.txt').read(),
    url='http://stefan.sofa-rockers.org/django-sphinxdoc/',
    download_url='http://bitbucket.org/scherfke/django-sphinxdoc/downloads/',
    license='BSD',
    packages=[
        'sphinxdoc', 
        # 'sphinxdoc.templatetags',
    ],
    package_data={
        'sphinxdoc': ['templates/sphinxdoc/*'],
    },
    classifiers=[
        'Development Status :: 4 - Beta',
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
