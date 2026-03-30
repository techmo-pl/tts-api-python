# AGENTS.md — tts-api-python

## Project Summary

Python gRPC stub package for the Techmo TTS Service API v3. Generates Python bindings from the proto definitions in the `tts-api` submodule and publishes them as a pip-installable package.

**PyPI package name:** `tts-api` (import namespace: `tts_service_api`)
**Distribution:** GitHub tagged releases — `git+https://github.com/techmo-pl/tts-api-python.git@vX.Y.Z`
**Version:** `tts_service_api/VERSION.py`
**Python support:** 3.8–3.13

## Repo Layout

```
tts_service_api/
  __init__.py        # re-exports everything from techmo.tts.api.v3
  v3.py              # same re-export (explicit v3 alias)
  VERSION.py         # single version source (__version__)
techmo/tts/api/v3/   # generated — never committed
  techmo_tts_pb2.py
  techmo_tts_pb2_grpc.py
submodules/
  tts-service-api/   # git submodule → github.com/techmo-pl/tts-api
shim/
  pyproject.toml     # deprecated tts-service-api==999.0.0 shim package
  README.md
setup.py             # drives protoc via grpcio-tools at build time
pyproject.toml       # build backend + grpcio-tools constraint
setup.sh             # one-time: init submodule + pre-commit hooks
install.sh           # create .venv + uv pip install -e .
```

## Import Paths

```python
# Canonical (generated namespace):
from techmo.tts.api.v3 import techmo_tts_pb2, techmo_tts_pb2_grpc

# Convenience re-export:
from tts_service_api import v3
from tts_service_api.v3 import TTSStub, SynthesizeRequest  # etc.

# Top-level wildcard (everything from v3):
import tts_service_api
```

## Environment Setup

```bash
./setup.sh     # one-time: init submodule + pre-commit hooks
./install.sh   # create .venv, install package (triggers stub generation)
source .venv/bin/activate
```

Stub generation runs automatically during `uv pip install -e .` via `setup.py`. Generated files (`techmo_tts_pb2.py`, `techmo_tts_pb2_grpc.py`) are **never committed**.

## Building & Releasing

```bash
uv build                        # produces dist/tts_api-X.Y.Z.tar.gz
git tag vX.Y.Z && git push origin vX.Y.Z
```

When a new proto version lands in `tts-api`:
1. Pull the submodule update
2. Regenerate stubs (reinstall or run `python setup.py build_grpc` in tts-api-python)
3. Bump `tts_service_api/VERSION.py`
4. Update `CHANGELOG.md`
5. Tag and release

## Deprecation Shim

`shim/` contains a metadata-only `tts-service-api==999.0.0` package that depends on `tts-api`. Build and release alongside main package releases. It exists solely for backwards compatibility — install it the same way.

## Dependency Constraints

Python 3.8 requires tighter bounds (grpcio 1.71.0 dropped Python 3.8):
- `grpcio>=1.70.0,<1.71.0` (3.8) vs `grpcio>=1.70.0` (3.9+)
- `protobuf>=5.29.0,<6.0` (3.8) vs `protobuf>=5.29.0` (3.9+)
- `grpcio-tools>=1.70.0,<1.71.0` in `pyproject.toml` build deps

Do not widen these without verifying Python 3.8 compatibility.

## CI — GitHub Actions

`.github/workflows/test.yml` tests Python 3.8–3.13. Each job: checkout with submodules → install uv → `uv pip install -e .` → verify `from tts_service_api import VERSION`.

## Commit Conventions

`feat:`, `fix:`, `chore:`, `ci:`, `docs:` — conventional commits. Never commit `*_pb2.py` or `*_pb2_grpc.py`. No Claude attribution in commit messages.
