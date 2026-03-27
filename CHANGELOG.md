# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).
The major version of this package tracks the TTS Service API major version.

## [Unreleased]

## [3.2.1] - 2026-03-27

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
