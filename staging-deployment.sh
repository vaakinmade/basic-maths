#!/bin/bash

python3 -m twine upload -u $PYPI_USERNAME -p $PYPI_TOKEN --repository-url https://test.pypi.org/legacy/ dist/*