import os

from configurations import importer
from configurations import values

from oldp.settings import Base, Dev, Prod

importer.install()

# TODO path does not work if installed as package
DE_BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class BaseDE(Base):
    """
    Settings for the German OLDP Theme

    - We basically just add a template directory such that we can override the original template files.
    - You can also add Germany-specific apps or processing steps.

    """

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
