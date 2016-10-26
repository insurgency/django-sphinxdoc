from setuptools import setup, find_packages


setup(
    name='django-sphinxdoc',
    version='1.4.2',
    author='Stefan Scherfke',
    author_email='stefan at sofa-rockers.org',
    description='Easily integrate Sphinx documentation into your website.',
    long_description=(open('README.txt').read() + '\n\n' +
                      open('CHANGES.txt').read() + '\n\n' +
                      open('AUTHORS.txt').read()),
    url='https://bitbucket.org/sscherfke/django-sphinxdoc/',
    license='MIT',
    install_requires=[
        'Django>=1.6.0',
        'django-haystack>=2.1',
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
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
    ],
)
