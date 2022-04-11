#!/bin/bash

python3 -m twine upload -u $PYPI_USERNAME -p $PYPI_TOKEN dist/* --verbose