from setuptools import setup, find_packages
import os

here = os.path.dirname(__file__)

readme = open(os.path.join(here, 'README.txt')).read()

setup(
    name="nosecolor",
    version="0.0",
    author="Atsushi Odagiri",
    author_email="aodagx@gmail.com",
    long_description=readme,
    install_requires=[
        "termcolor",
        "nose",
    ],
    test_suite="nosecolor",
    packages=find_packages(exclude=['tests', 'examples']),
)
