# Create a manifest with every risk factor applied into diagnose calculation
from pydantic import BaseModel

class Rules(BaseModel):
    count: int
    percentage: float

class Factors(BaseModel):
    code: str
    points: int

class Props(BaseModel):
    name: str
    factors: list[Factors]
    rules: list[Rules]

class Diseases(BaseModel):
    IAM: Props



def get_rules(code: str):
    diseases: Diseases = {
        'IAM': {
            'name': 'Infarto Agudo el Miocardio',
            'factors': [
                {
                    'code': 'olderThan65',
                    'points': 1
                },
                {
                    'code': 'hypertension',
                    'points': 0.33
                },
                {
                    'code': 'diabetes',
                    'points': 0.33
                },
                {
                    'code': 'hyperlipidemia',
                    'points': 0.33
                },
                {
                    'code': 'smoker',
                    'points': 0.33
                },
                {
                    'code': 'historyOfHeartDisease',
                    'points': 1
                },
                {
                    'code': 'historyOfCoronaryStenosis',
                    'points': 1
                },
                {
                    'code': 'anginaEpisodes',
                    'points': 1
                },
                {
                    'code': 'aspirinUsage',
                    'points': 1
                },
                {
                    'code': 'segmentSTChanges',
                    'points': 1
                },
                {
                    'code': 'necrosisMarkers',
                    'points': 1
                },
            ],
            'rules': [
                {
                    'count': 1,
                    'percentage': 4.7
                },
                {
                    'count': 2,
                    'percentage': 8.3
                },
                {
                    'count': 3,
                    'percentage': 13.2
                },
                {
                    'count': 4,
                    'percentage': 19.9
                },
                {
                    'count': 5,
                    'percentage': 26.2
                },
                {
                    'count': 6,
                    'percentage': 40.9
                },
            ]
        },
        'EPA': {
            'name': 'Embolia Pulmonar Aguda',
            'factors': [
                {
                    'code': 'tvp',
                    'points': 3
                },
                {
                    'code': 'ep',
                    'points': 3
                },
                {
                    'code': 'beatsPerMinutesOverHundred',
                    'points': 1.5
                },
                {
                    'code': 'previousSurgery',
                    'points': 1.5
                },
                {
                    'code': 'previousTVPOrEp',
                    'points': 1.5
                },
                {
                    'code': 'hemoptisis',
                    'points': 1
                },
                {
                    'code': 'activeCancer',
                    'points': 1
                }
            ],
            'rules': [
                {
                    'count': 2,
                    'percentage': 10.0
                },
                {
                    'count': 6,
                    'percentage': 50.0
                },
                {
                    'count': 7,
                    'percentage': 75.0
                }
            ]
        }
    }

    return diseases[code]