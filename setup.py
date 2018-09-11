from io import open
from setuptools import setup
from axsemantics_sphinx_theme import __version__


setup(
    name='axsemantics_sphinx_theme',
    version=__version__,
    url='https://github.com/axsemantics/sphinx_theme/',
    license='MIT',
    author='AX Semantics',
    description='Sphinx theme used on AX Semantics internal documentation',
    long_description=open('README.rst', encoding='utf-8').read(),
    packages=['axsemantics_sphinx_theme'],
    package_data={'axsemantics_sphinx_theme': [
        'theme.conf',
        '*.html',
        'static/css/*.css',
        'static/js/*.js',
        'static/font/*.*'
    ]},
    include_package_data=True,
    # See http://www.sphinx-doc.org/en/stable/theming.html#distribute-your-theme-as-a-python-package
    entry_points = {
        'sphinx.html_themes': [
            'axsemantics_sphinx_theme = axsemantics_sphinx_theme',
        ]
    },
    install_requires=[
       'sphinx'
    ],
    classifiers=[
        'Framework :: Sphinx',
        'Framework :: Sphinx :: Theme',
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Operating System :: OS Independent',
        'Topic :: Documentation',
        'Topic :: Software Development :: Documentation',
    ],
)
