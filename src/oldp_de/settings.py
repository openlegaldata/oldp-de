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
