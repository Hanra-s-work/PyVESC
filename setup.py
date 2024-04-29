"""
File containing the required information to successfully build a python package
"""

import setuptools

# with open("README.md", "r", encoding="utf-8", newline="\n") as fh:
#     long_description = fh.read()

long_description = """
# PyVESC [![Build Status](https://travis-ci.org/LiamBindle/PyVESC.svg?branch=master)](https://travis-ci.org/LiamBindle/PyVESC) [![Documentation Status](https://readthedocs.org/projects/pyvesc/badge/?version=latest)](http://pyvesc.readthedocs.io/en/latest/?badge=latest)

PyVESC is aimed at being a easy to use and robust python implementation of the
communication protocol used by the
[VESC - Open Source ESC](http://vedder.se/2015/01/vesc-open-source-esc/) by
Benjamin Vedder. Its a great project with a really great community and I'd urge
anyone interested in motor controllers to take a look at it.

That being said, if you're here you probably already know about it. This small
project was written by Liam Bindle for the
[University of Saskatchewan Space Design Team](https://usst.ca)
as our primary language for non-embedded system is Python. You might wonder why
you might need a library to handling packing and parsing VESC messages since
Pythons standard
[struct](https://docs.python.org/3.5/library/struct.html)
module is great for almost exaclty this. PyVESC's usefulness comes from the fact
that PyVESC is:

- Well tested
- Robust in handling corrupt packets in a buffer
- Messages are easily extensible so that PyVESC can be used as a generic
  message/codec protocol (ie. at the USST we use PyVESC for sending messages to
  all of our embedded systems)
- Implements a number of common-error catching exceptions to speed up your
  development

## Documentation

For the latest version of PyVESC's documentation [Read The Docs](http://pyvesc.readthedocs.io/en/latest/)

## Contributing

Obviously this is just a quick and dirty project; however, if you have any ideas,
critiques or changes just let me know or submit a pull request.

## License

Just like VESC, PyVESC is distributed under a
[Creative Commons ShareALike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/).
"""

VERSION = '1.0.0'

setuptools.setup(
    name='pyvesc_fix',
    version=VERSION,
    packages=setuptools.find_packages(),
    install_requires=[
        'pyserial==3.5',
        'crccheck>=0.6',
        'pythoncrc==1.21'
    ],
    author="Henry Letellier",
    author_email="henrysoftwarehouse@protonmail.com",
    description="This is a repackagin of a fork from the pyvesc library.",
    long_description=f"This is a repackaging of the (broken) package pyvesc\nThis package can be found here: https://pypi.org/project/pyvesc/\n{long_description}",
    long_description_content_type="text/markdown",
    url="https://github.com/Hanra-s-work/PyVESC",
    keywords=['vesc', 'VESC', 'communication', 'protocol', 'packet'],
    download_url='https://github.com/Hanra-s-work/PyVESC' + VERSION,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
