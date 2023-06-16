#!/bin/bash

# Step 1: Build the package
python setup.py sdist bdist_wheel

# Step 2: Install the package
PACKAGE_FILE=$(ls dist/*.tar.gz 2>/dev/null || ls dist/*.whl)
pip install $PACKAGE_FILE
