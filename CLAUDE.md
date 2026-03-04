# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

```bash
# Install dependencies
poetry install
# or: pip install -r requirements.txt

# Run all tests
python -m unittest

# Run a single test method
python -m unittest tests.TestPyscordStorage.test_upload_from_file
```

There is no build, lint, or type-check step configured.

## Architecture

**pyscord-storage** is a minimal Python library that wraps an external Discord-based file storage API (`https://discord-storage.animemoe.us/`), providing free file hosting via Discord's CDN infrastructure.

### Core module: [pyscord_storage/__init__.py](pyscord_storage/__init__.py)

Two public functions:
- `upload_from_file(file)` — reads a local file and POSTs it as multipart/form-data
- `upload_from_url(filename, file_url)` — POSTs a JSON body with a remote URL for the backend to fetch

Both return `{"status": <http_status_code>, "data": <json_response>}`.

A spoofed Chrome User-Agent header is set on all requests to avoid server-side rejection.

### Tests: [tests/__init__.py](tests/__init__.py)

Uses Python's `unittest` module. Tests run against the live external API (no mocking). A real PNG file at [tests/temp/takagi.png](tests/temp/takagi.png) is used for `test_upload_from_file`.

### CI: [.github/workflows/python-app.yml](.github/workflows/python-app.yml)

Runs `python -m unittest` on push/PR to master using Python 3.10.
