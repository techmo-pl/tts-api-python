# tts-service-api-python

Python gRPC stubs for Techmo TTS Service API v3.

This package provides generated Python stubs for the
[tts-service-api](https://github.com/techmo-pl/tts-service-api) proto
definitions, along with a convenience re-export layer.

## Installation

```bash
./setup.sh   # initialise submodules
./install.sh # create venv and install
```

## Usage

```python
# Direct import from the generated namespace:
from techmo.tts.api.v3 import techmo_tts_pb2, techmo_tts_pb2_grpc

# Or via the convenience re-export layer:
from tts_service_api import v3
```

## Versioning

The major version of this package tracks the TTS Service API major version.
