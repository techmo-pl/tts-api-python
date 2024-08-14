**Table of contents**

[[_ToC_]]

# TTS Service API (Python)

The collection of gRPC APIs for TTS Service solutions from the [tts-service-api](https://gitlab.devtechmo.pl/tts/tts-service-api) repository supplied as a Python package.

## Setup

The project setup is not mandatory; it will work as is. The installation of all required packages for preparing the package will take place in a virtual environment.

### Requirements

- [Python](https://www.python.org/) >=3.10

## Installation

### Virtual environment

Example:

```sh
python3 -m venv .venv
source .venv/bin/activate
pip install --require-virtualenv --upgrade pip
pip install --require-virtualenv .
```

_For basic development use, consider convenient `./install.sh`._

## Usage

### Import

The package provides a precompiled collection of .proto files. These can be imported directly or through the alias modules.

Example:

- direct import

```python
>>> import techmo_tts_pb2 as api
>>> hasattr(api, "SynthesizeRequest")
True
```

- import from an alias module

```python
>>> from tts_service_api import techmo_tts_api as api
>>> hasattr(api, "SynthesizeRequest")
True
```

### Invoke RPC

Invoking RPC simply requires to call a desired method on a [_stub_](https://grpc.io/docs/what-is-grpc/core-concepts/#using-the-api) object dedicated to a specific _service_.

## Docker

The project provides a Dockerfile for a preconfigured development environment, rather used by the CI pipeline.
