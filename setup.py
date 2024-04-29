"""
File containing the required information to successfully build a python package
"""

import setuptools

with open("README.md", "r", encoding="utf-8", newline="\n") as fh:
    long_description = fh.read()

VERSION = '1.0.0'

setuptools.setup(
    name='pyvesc_fix',
    version=VERSION,
    packages=setuptools.find_packages(),
    install_requires=[
        'pythoncrc==1.21',
        'crccheck>=0.6'
    ],
    author="Henry Letellier",
    author_email="henrysoftwarehouse@protonmail.com",
    description="This is a repackagin of a fork from the pyvesc library.",
    long_description=f"This is a repackaging of the (broken) package pyvesc\nThis package can be found here: https://pypi.org/project/pyvesc/\n{long_description}",
    long_description_content_type="text/markdown",
    url="https://github.com/Hanra-s-work/PyVESC",
    keywords=['vesc', 'VESC', 'communication', 'protocol', 'packet'],
    download_url='https://github.com/LiamBindle/PyVESC/tarball/' + VERSION,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
