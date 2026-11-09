# OLDP DE: German Theme for Open Legal Data

[![PyPI version](https://img.shields.io/pypi/v/oldp-de.svg)](https://pypi.org/project/oldp-de/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## Getting Started

Install from PyPI:

```bash
pip install oldp-de
```

Or install the latest development version directly from GitHub:

```bash
pip install git+https://github.com/openlegaldata/oldp-de.git
```

For local development:

```bash
git clone https://github.com/openlegaldata/oldp-de.git
cd oldp-de
pip install -e ".[dev]"
```

## Configuration

Tell OLDP to use the OLDP-DE settings file and development configuration:

```bash
export DJANGO_SETTINGS_MODULE=oldp_de.settings
export DJANGO_CONFIGURATION=DevDEConfiguration  # For production use `ProdDEConfiguration`
```

Start OLDP as always (from OLDP directory):

```bash
python manage.py runserver
```

## How does it work?

By loading another settings file, we basically just tell Django to use assets (templates, images, ...) from the German theme if they exist.
As a result, we can modify the layout etc. without touching the original OLDP code.

## MCP Registry listing

The German deployment is listed in the official MCP Registry as
`io.openlegaldata/de`. Name, title and description are set in
`src/oldp_de/settings.py` (`MCP_REGISTRY_*`); version and URLs come from OLDP.
Generate `server.json` from the OLDP directory and publish it with
`mcp-publisher` (see OLDP's `docs/mcp.md`, "Official MCP Registry"):

```bash
export DJANGO_SETTINGS_MODULE=oldp_de.settings DJANGO_CONFIGURATION=ProdDEConfiguration
python manage.py mcp_server_json --output server.json
mcp-publisher publish server.json
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
