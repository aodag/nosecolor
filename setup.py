from setuptools import setup, find_packages
import os

here = os.path.dirname(__file__)

readme = open(os.path.join(here, 'README.txt')).read()
changes = open(os.path.join(here, 'CHANGES.txt')).read()

setup(
    name="nosecolor",
    version="0.1",
    author="Atsushi Odagiri",
    author_email="aodagx@gmail.com",
    description="nose plugin to display colored results.",
    keywords='nose test',
    url="https://github.com/aodag/nosecolor",
    long_description=readme + "\n" + changes,
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
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Environment :: Console",
        "Operating System :: POSIX",
        "Topic :: Software Development :: Testing",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Topic :: Software Development :: Testing",
    ],
)
