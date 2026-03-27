#!/bin/bash
#
# usage: ./install.sh [VENV_PATH]
#
# VENV_PATH: Optional path for the virtual environment (default: ./.venv).
#
# Creates a virtualenv with uv and installs the package (including proto stub
# generation) with test dependencies.

set -euo pipefail

if ! command -v uv &> /dev/null; then
    echo "Error: 'uv' is required but not installed." >&2
    echo "Install it with:  curl -LsSf https://astral.sh/uv/install.sh | sh" >&2
    echo "After installing, open a new shell or run: source ~/.bashrc  (or ~/.zshrc)" >&2
    exit 1
fi

PROTO_SENTINEL="submodules/tts-service-api/proto/techmo_tts.proto"
if [ ! -f "${PROTO_SENTINEL}" ]; then
    echo "Error: submodule 'tts-service-api' is not initialised." >&2
    echo "Run ./setup.sh first, then re-run ./install.sh." >&2
    exit 1
fi

VENV_PATH="${1:-.venv}"

if [ ! -d "${VENV_PATH}" ]; then
    uv venv "${VENV_PATH}"
fi

# shellcheck disable=SC1091
source "${VENV_PATH}/bin/activate"
uv pip install -e "."
