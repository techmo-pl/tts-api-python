# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).
The major version of this package tracks the TTS Service API major version.

## [Unreleased]

## [3.2.2] - 2026-04-01

### Fixed
- Raised `grpcio` lower bound to `>=1.80.0` for Python 3.9+ (grpcio skips 1.79.x;
  grpcio 1.78.x causes runtime failures when combined with livekit-agents>=1.5.1).
  No stub regeneration required — generated stubs (GRPC_GENERATED_VERSION='1.70.0')
  are forward-compatible with grpcio 1.80.0.

## [3.2.1+1] - 2026-03-30

### Added
- `AGENTS.md`: AI assistant context document describing the repo layout, import paths, stub generation workflow, shim package, and dependency constraints.

## [3.2.1] - 2026-03-30

### Changed
- PyPI package renamed from `tts-service-api` to `tts-api` (ASR naming convention).
  Import name `tts_service_api` is unchanged.
- Deprecation shim published separately as `tts-service-api==999.0.0`
  (pulls in `tts-api` as dependency).

## [3.2.0] - 2026-03-27

### Added
- Initial release: Python stub package for Techmo TTS Service API v3.
- Generated gRPC stubs in `techmo.tts.api.v3` namespace.
- Convenience re-export module `tts_service_api.v3`.
