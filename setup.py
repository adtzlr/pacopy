import os

from setuptools import find_packages, setup

# https://packaging.python.org/single_source_version/
base_dir = os.path.abspath(os.path.dirname(__file__))
about = {}
with open(os.path.join(base_dir, "pacopy", "__about__.py"), "rb") as f:
    exec(f.read(), about)


setup(
    name="pacopy",
    version=about["__version__"],
    packages=find_packages(),
    url="https://github.com/nschloe/pacopy",
    author=about["__author__"],
    author_email=about["__email__"],
    install_requires=[],
    python_requires=">=3.6",
    description="Numerical continuation in Python",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    license=about["__license__"],
    classifiers=[
        about["__license__"],
        about["__status__"],
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Mathematics",
    ],
)
