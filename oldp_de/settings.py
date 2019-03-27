import os

from configurations import importer
from configurations import values

from oldp.settings import Base, Dev, Prod

from oldp_de.courts_de.apps import CourtTypesDE

importer.install()

# TODO path does not work if installed as package
DE_BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class BaseDE(Base):
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

    @classmethod
    def post_setup(cls):
        super().post_setup()

        # Add oldp_de templates in the begging of list
        cls.TEMPLATES[0]['DIRS'].insert(0, os.path.join(DE_BASE_DIR, 'oldp_de/assets/templates'))
        cls.STATICFILES_DIRS.insert(0, os.path.join(DE_BASE_DIR, 'oldp_de/assets/static'))


class DevDE(BaseDE, Dev):
    DEBUG = True


class ProdDE(BaseDE, Prod):
    DEBUG = False
