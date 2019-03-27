from django.apps import AppConfig
from oldp.apps.courts.apps import CourtTypes, CourtLocationLevel

class CourtsDEConfig(AppConfig):
    name = 'oldp_de.apps.courts_de'


class CourtTypesDE(CourtTypes):
    def get_types(self):
        return {
            'AG': {
                'name': 'Amtsgericht',
                'levels': [CourtLocationLevel.CITY]
            },
            'ARBG': {
                'name': 'Arbeitsgericht',
                'levels': [CourtLocationLevel.CITY]
            },
            'BAG': {
                'name': 'Bundesarbeitsgericht',
                'levels': []
            },
            'BGH': {
                'name': 'Bundesgerichtshof',
                'levels': []
            },
            'BFH': {
                'name': 'Bundesfinanzhof',
                'levels': []
            },
            'BSG': {
                'name': 'Bundessozialgericht',
                'levels': []
            },
            'BVerfG': {
                'name': 'Bundesverfassungsgericht',
                'levels': []
            },
            'BVerwG': {
                'name': 'Bundesverwaltungsgericht',
                'levels': []
            },
            'BPatG': {
                'name': 'Bundespatentgericht',
                'levels': []
            },
            # 'BGH': {
            #     'name': 'Berufsgericht für Heilberufe',
            #     'levels': [CourtLocationLevel.CITY]
            # },
            # 'DG': {
            #     'name': 'Dienstgericht für Richter'
            # }
            'FG': {
                'name': 'Finanzgericht',
                'levels': [CourtLocationLevel.CITY]
            },
            'LAG': {
                'name': 'Landesarbeitsgericht',
                'levels': [CourtLocationLevel.STATE]
            },
            'LSG': {
                'name': 'Landessozialgericht',
                'levels': [CourtLocationLevel.STATE]
            },
            'LVG': {
                'name': 'Landesverfassungsgericht',
                'levels': [CourtLocationLevel.STATE]
            },
            'LBGH': {
                'name': 'Landesberufsgericht',
                'levels': [CourtLocationLevel.STATE]
            },
            'LG': {
                'name': 'Landgericht',
                'levels': [CourtLocationLevel.CITY, CourtLocationLevel.STATE]
            },
            'OLG': {
                'name': 'Oberlandesgericht',
                'levels': [CourtLocationLevel.STATE]
            },
            'OBLG': {
                'name': 'Oberstes Landesgericht',
                'levels': [CourtLocationLevel.STATE]
            },
            'OVG': {
                'name': 'Oberverwaltungsgericht',
                'levels': [CourtLocationLevel.STATE]
            },
            'SG': {
                'name': 'Sozialgericht',
                'levels': [CourtLocationLevel.CITY]
            },
            'STGH': {
                'name': 'Staatsgerichtshof',
                'levels': [CourtLocationLevel.STATE]
            },
            'SCHG': {
                'name': 'Schifffahrtsgericht',
                'levels': [CourtLocationLevel.CITY]
            },
            'SCHOG': {
                'name': 'Schifffahrtsobergericht',
                'levels': [CourtLocationLevel.CITY]
            },
            'VERFG': {
                'name': 'Verfassungsgerichtshof',
                'aliases': ['Verfassungsgericht'],
                'levels': [CourtLocationLevel.STATE]
            },
            'VG': {
                'name': 'Verwaltungsgericht',
                'levels': [CourtLocationLevel.CITY, CourtLocationLevel.STATE]
            },
            'VGH': {
                'name': 'Verwaltungsgerichtshof',
                'levels': [CourtLocationLevel.STATE]
            },
            'KG': {
                'name': 'Kammergericht',
                'levels': [CourtLocationLevel.CITY]
            },
            'EuGH': {
                'name': 'Europäischer Gerichtshof',
                'levels': []
            },
            'AWG': {
                'name': 'Anwaltsgericht',
                'aliases': ['Anwaltsgerichtshof'],
                'levels': [CourtLocationLevel.STATE],
            },
            'MSCHOG': {
                'name': 'Moselschifffahrtsobergericht',
                'levels': [CourtLocationLevel.CITY]
            },
            'RSCHGD': {
                'name': 'Rheinschifffahrtsgericht',
                'levels': [CourtLocationLevel.CITY]
            },
            'RSCHOG': {
                'name': 'Rheinschifffahrtsobergericht',
                'levels': [CourtLocationLevel.CITY]
            }
            # TODO add more
        }