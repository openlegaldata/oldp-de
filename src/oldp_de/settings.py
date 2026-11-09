from pathlib import Path

from configurations import importer
from configurations import values

from oldp.settings import BaseConfiguration, DevConfiguration, ProdConfiguration

from oldp_de.courts_de.apps import CourtTypesDE

importer.install()

_PACKAGE_DIR = Path(__file__).resolve().parent


class BaseDEConfiguration(BaseConfiguration):
    """
    Settings for the German OLDP Theme

    - We basically just add a template directory such that we can override the original template files.
    - You can also add Germany-specific apps or processing steps.

    """

    COURT_JURISDICTIONS = {  # name: regex
        'Arbeitsgerichtsbarkeit': 'arbeitsgericht',
        'Sozialgerichtsbarkeit': 'sozialgericht',
        'Ordentliche Gerichtsbarkeit': 'amtsgericht|landgericht|schifffahrtsgericht|dienstgericht|patentgericht',
        'Berufsgerichtsbarkeit': 'berufsgericht',
        'Finanzgerichtsbarkeit': 'finanzgericht',
        'Verwaltungsgerichtsbarkeit': 'verwaltungsgericht',
        'Verfassungsgerichtsbarkeit': 'verfassungsgericht|staatsgerichtshof'
    }

    COURT_LEVELS_OF_APPEAL = {  # name: regex
        'Amtsgericht': 'amtsgericht',
        'Oberlandesgericht': 'oberlandesgericht|oberstes landes',
        'Landgericht': 'landgericht',
        'Bundesgericht': 'bund',
    }

    COURT_TYPES = CourtTypesDE()

    LANGUAGE_CODE = 'de'

    # German legal/info pages (Impressum, Datenschutz, AGB) served as markdown
    # at /pages/<slug>/ by oldp.apps.pages. Overrides the base placeholder dir;
    # a DJANGO_MARKDOWN_PAGES_DIR env var still wins (e.g. to load the texts from
    # a private deployment repo mounted into the container).
    MARKDOWN_PAGES_DIR = values.Value(str(_PACKAGE_DIR / 'content' / 'pages'))

    # Listing in the official MCP Registry, rendered into server.json by OLDP's
    # ``manage.py mcp_server_json`` (version and URLs come from OLDP / SITE_URL).
    # The registry name cannot be changed after the first publish; title and
    # description are limited to 100 characters each.
    MCP_REGISTRY_NAME = values.Value('io.openlegaldata/de', environ_name='MCP_REGISTRY_NAME')
    MCP_REGISTRY_TITLE = values.Value('Open Legal Data (Germany)', environ_name='MCP_REGISTRY_TITLE')
    MCP_REGISTRY_DESCRIPTION = values.Value(
        'German court decisions (Rechtsprechung) and laws (Gesetze) with citation graph and citation checks.',
        environ_name='MCP_REGISTRY_DESCRIPTION',
    )

    @classmethod
    def post_setup(cls):
        super().post_setup()

        # Add oldp_de templates at the beginning of list
        cls.TEMPLATES[0]['DIRS'].insert(0, str(_PACKAGE_DIR / 'assets' / 'templates'))
        cls.STATICFILES_DIRS.insert(0, str(_PACKAGE_DIR / 'assets' / 'static'))


class DevDEConfiguration(BaseDEConfiguration, DevConfiguration):
    DEBUG = True

    INSTALLED_APPS = DevConfiguration.INSTALLED_APPS
    MIDDLEWARE = DevConfiguration.MIDDLEWARE


class ProdDEConfiguration(BaseDEConfiguration, ProdConfiguration):
    DEBUG = False

    ALLOWED_HOSTS = values.ListValue(['de.openlegaldata.io', 'localhost'])
