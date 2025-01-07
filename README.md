# OLDP DE: German Theme for Open Legal Data

## Getting Started

Installation over `pip` directly from Github:

```bash
pip install git+https://github.com/openlegaldata/oldp-de.git
```

Alternatively, you could `git clone` this repository and install it locally:

```bash
git clone https://github.com/openlegaldata/oldp-de.git
cd oldp-de
python setup.py install
```

Tell OLDP to use the OLDP-DE settings file and development configuration:

```bash
export DJANGO_SETTINGS_MODULE=oldp_de.settings
export DJANGO_CONFIGURATION=DevDEConfiguration  # For production use `ProdDEConfiguration`
```

Start OLDP as always (from OLDP directory):

```bash
# Run from OLDP directory
python manage.py runserver
```

## How does it work?

By loading another settings file, we basically just tell Django to use assets (templates, images, ...) from the German theme if then exist.
As a result, we can modify the layout etc. without touching the original OLDP code.