from setuptools import setup, find_packages
from codecs import open
from os import path

# The directory containing this file
PWD = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(PWD, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# This call to setup() does all the work
setup(
    name="basic-maths",
    version="0.1.20",
    description="Basic maths library for multiplication and division",
    long_description=long_description,
    long_description_content_type="text/markdown",
    # url="https://medium-multiply.readthedocs.io/",
    author="Victor Akinmade",
    author_email="victor@email.com",
    license="MIT",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent"
    ],
    packages=find_packages(exclude=["*tests*"]),
    include_package_data=True,
    install_requires=["numpy"]
)
