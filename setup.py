#!/usr/bin/env

import setuptools

"""
>>> python setup.py bdist_wheel
>>> python -m pip install dist/confclass-<XX.XX>-py3-none-any.whl
>>> python -m twine upload dist/*
"""

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='confclass',
    version='0.1.2',
    provides=['confclass'],
    py_modules=['confclass'],
    author="Elad Nachmias",
    author_email="eladnah@gmail.com",
    description="A python package for working with program configuration parameters",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/eladn/confclass",
    packages=setuptools.find_packages(),
    install_requires=['pyyaml'],
    license='Apache-2.0',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
 )
