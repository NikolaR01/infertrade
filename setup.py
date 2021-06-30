#!/usr/bin/env python3
"""
infertrade setup.py file

   Copyright 12th March 2021 InferStat Ltd

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.

"""

# Python standard library
import re

from os import walk
from pathlib import Path    

# Third library (not InferStat)
from setuptools import find_packages, setup

# Hardcoded variables
PROJECT_NAME = "infertrade"
PROJECT_DESCRIPTION = "Pandas and SciKit Learn compatible open source interface for algorithmic trading functions."
BLACKLIST_DIRS = ["example_scripts"]

this_directory = Path(__file__).cwd()   


def get_long_description(filename: str = "README.md") -> str:
    """Returns a long repository description read from file."""
    try:
        with open(Path.joinpath(this_directory, filename)) as f:
            long_description = "\n" + f.read()
    except FileNotFoundError:
        long_description = ""
    return long_description



def get_version(filename: str = "_version.py") -> str:
    """Returns the package version number as a string by searching and reading the _version.py file."""
    for dirpath, _, filenames in walk(".", topdown=True):
        if ".gitignore" in filenames:
            with open(".gitignore") as _f:
                gitignore = [file.strip() for file in _f.readlines() if not re.search(r"\#|\*", file)]

        if any(pattern for pattern in gitignore + BLACKLIST_DIRS if re.search(pattern, dirpath)):
            continue
        for file in filenames:
            if filename in file:
                file_path = Path().joinpath(dirpath, filename)
    try:
        assert file_path.is_file()
        with open(file_path) as f:
            _version_info = "".join([i.strip() for i in f.readlines() if i.startswith("_")])
            _version_info = _version_info.replace(" ", "").replace('"', "").replace('"', "")
            about = dict([_version_info.split("=")])  # noqa: C406
    except FileNotFoundError:  # TODO - probably should be expected error types.
        raise RuntimeError(f"Unable to find version information in '{file_path}'.")
    else:  # TODO - currently this can't trigger as prior exception catches all errors.
        return about["__version__"]


# List of requirements as in requirements.txt
PACKAGE_REQUIREMENTS = ['pandas>=1.2.4', 'numpy>=1.20.1', 'ta>=0.7.0', 'scikit-learn>=0.23.1', 'matplotlib>=3.3.4', 'typing_extensions>=3.7.4.3']
DEV_REQUIREMENTS = 'pytest==6.2.2'

# Setting up basic parameters of infertrade library
setup(
    name=PROJECT_NAME,
    version=get_version(),
    description=PROJECT_DESCRIPTION,
    license="Apache License 2.0",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    url=f"https://github.com/ta-oliver/infertrade",
    author="Thomas Oliver",
    author_email="support@infertrade.com",
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    install_requires=PACKAGE_REQUIREMENTS,
    extras_require={"dev": DEV_REQUIREMENTS},
    tests_require=["pytest"],
    python_requires=">=3.7.0,<3.8.0",
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Development Status :: 2 - Pre-Alpha",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Intended Audience :: Financial and Insurance Industry",
        "Intended Audience :: Information Technology",
        "Intended Audience :: Science/Research",
        "Topic :: Software Development :: Libraries",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Natural Language :: English",
    ],
    zip_safe=False,
)
