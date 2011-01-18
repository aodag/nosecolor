from setuptools import setup, find_packages
import os

here = os.path.dirname(__file__)

readme = open(os.path.join(here, 'README.txt')).read()

setup(
    name="nosecolor",
    version="0.0",
    author="Atsushi Odagiri",
    author_email="aodagx@gmail.com",
    description="nose plugin to display colored results.",
    url="https://github.com/aodag/nosecolor",
    long_description=readme,
    license="MIT",
    install_requires=[
        "termcolor",
        "nose",
    ],
    test_suite="nosecolor",
    packages=find_packages(exclude=['tests', 'examples']),
    entry_points={
        "nose.plugins.0.10":[
            "nosecolor=nosecolor:NoseColorPlugin",
        ],
    },
)
