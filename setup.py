from setuptools import setup, find_packages


setup(
    name='django-sphinxdoc',
    version='2.0.0',
    author='Stefan Scherfke',
    author_email='stefan at sofa-rockers.org',
    description='Easily integrate Sphinx documentation into your website.',
    long_description=(open('README.txt').read() + '\n\n' +
                      open('CHANGES.txt').read() + '\n\n' +
                      open('AUTHORS.txt').read()),
    url='https://bitbucket.org/sscherfke/django-sphinxdoc/',
    license='MIT',
    python_requires='>=3.6',
    install_requires=[
        'Django>=2.0',
        'django-haystack>=2.8.0',
    ],
    packages=find_packages(exclude=['*.tests', '*.tests.*']),
    include_package_data=True,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
    ]
)
