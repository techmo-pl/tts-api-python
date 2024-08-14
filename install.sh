#!/bin/bash

# install.sh
#
# Usage:
#   install

set -e

python3 -m venv .venv
# shellcheck disable=SC1091
source .venv/bin/activate
pip install --require-virtualenv --upgrade pip
pip install --require-virtualenv --editable .

echo Remember to activate virtual environment
