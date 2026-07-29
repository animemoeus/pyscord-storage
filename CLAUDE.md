# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

```bash
# Install dependencies
uv sync

# Run all tests
uv run pytest

# Run a single test
uv run pytest tests/test_pyscord_storage.py::test_upload_from_file

# Lint and format check
uv run ruff check .
uv run ruff format --check .

# Install pre-commit hooks (once, locally)
uv run pre-commit install
```

## Architecture

**pyscord-storage** is a minimal Python library that wraps an external Discord-based file storage API (`https://discord-storage.animemoe.us/`), providing free file hosting via Discord's CDN infrastructure.

### Core module: [pyscord_storage/__init__.py](pyscord_storage/__init__.py)

Two public functions:
- `upload_from_file(file)` — reads a local file and POSTs it as multipart/form-data
- `upload_from_url(filename, file_url)` — POSTs a JSON body with a remote URL for the backend to fetch

Both return `{"status": <http_status_code>, "data": <json_response>}`.

A spoofed Chrome User-Agent header is set on all requests to avoid server-side rejection.

### Tests: [tests/test_pyscord_storage.py](tests/test_pyscord_storage.py)

Plain pytest-style test functions (not `unittest.TestCase`), run via `pytest-asyncio` in auto mode. Tests run against the live external API (no mocking). A real PNG file at [tests/temp/takagi.png](tests/temp/takagi.png) is used for `test_upload_from_file`.

### CI: [.github/workflows/python-app.yml](.github/workflows/python-app.yml)

Runs `ruff check`, `ruff format --check`, and `pytest` via `uv` on push/PR to master, across Python 3.9–3.13.
