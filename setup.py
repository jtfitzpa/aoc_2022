#!/usr/bin/env python
"""aoc distutils configuration."""
from setuptools import setup

version = "0.0.0"

with open('README.md', encoding='utf-8') as readme_file:
    readme = readme_file.read()

requirements = [
    'binaryornot>=0.4.4',
    'click>=7.0,<8.0.0',
    'pyyaml>=5.3.1',
    'python-slugify>=4.0.0',
    'requests>=2.23.0',
]

setup(
    name='aoc_2022',
    version=version,
    description=(
        'A command-line utility that creates projects from project '
        'templates, e.g. creating a Python package project from a '
        'Python package project template.'
    ),
    long_description=readme,
    long_description_content_type='text/markdown',
    author='Josh Fitzpatrick',
    author_email='jtfitzpa@umich.edu',
    url='https://github.com/jtfitzpa/aoc_2022',
    packages=['aoc_2022'],
    package_dir={'aoc_2022': 'aoc_2022'},
    entry_points={'console_scripts': []},
    include_package_data=True,
    python_requires='>=3.6',
    install_requires=requirements,
    license='BSD',
    zip_safe=False,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Programming Language :: Python",
        "Topic :: Software Development",
    ],
    keywords=[],
)
