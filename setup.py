from __future__ import annotations

import shutil
from pathlib import Path

import setuptools

_PROTO_SRC = Path("submodules/tts-service-api/proto")
_STAGING = Path("_proto_staging")
_STAGING_TARGET = _STAGING / "techmo" / "tts" / "api" / "v3"


def _update_submodule(submodule_path: str) -> None:
    import subprocess

    if (Path(submodule_path) / ".git").exists():
        return
    if (
        subprocess.call(
            ("git", "submodule", "update", "--init", "--depth", "1", "--", submodule_path)
        )
        != 0
    ):
        raise Exception(f"error: git submodule update failed for {submodule_path}")


def _protoc(*args: str) -> None:
    import grpc_tools
    from grpc_tools import protoc

    well_known = str(Path(grpc_tools.__file__).parent / "_proto")
    if (
        protoc.main(
            command := ("grpc_tools.protoc", f"--proto_path={well_known}") + args
        )
        != 0
    ):
        raise Exception(f"error: {command} failed")


def _build_protos() -> None:
    _update_submodule("submodules/tts-service-api")

    if not (_PROTO_SRC / "techmo_tts.proto").exists():
        raise FileNotFoundError(
            f"Proto source not found: {_PROTO_SRC / 'techmo_tts.proto'}\n"
            "The 'tts-service-api' submodule is not initialised.\n"
            "Run ./setup.sh first, then re-run ./install.sh."
        )

    shutil.rmtree(_STAGING, ignore_errors=True)
    _STAGING_TARGET.mkdir(parents=True)

    try:
        shutil.copy(_PROTO_SRC / "techmo_tts.proto", _STAGING_TARGET)

        _protoc(
            f"--proto_path={_STAGING}",
            "--python_out=.",
            "--grpc_python_out=.",
            "techmo/tts/api/v3/techmo_tts.proto",
        )
    finally:
        shutil.rmtree(_STAGING, ignore_errors=True)


_build_protos()

setuptools.setup()
