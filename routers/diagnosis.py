from fastapi import APIRouter
from TAGS import TAGS
from factory.creators.IAMFactory import IAMFactory
from factory.creators.EPAFactory import EPAFactory
from factory.implementations.diagnosis import perform_diagnosis
from factory.interfaces.DiagnosisInterface import DiagnosisBody, DiagnosisResponse

diagnosis_router = APIRouter()

# Register Entity
@diagnosis_router.post('/api/diagnosis', tags=TAGS['DIAGNOSIS'])
def create(body: DiagnosisBody)->list[DiagnosisResponse]:
    iam_factory = IAMFactory()
    epa_factory = EPAFactory()
    
    res: list[DiagnosisResponse] = [
        perform_diagnosis(factory=iam_factory, differential=body.differential, options=body.symptoms),
        perform_diagnosis(factory=epa_factory, differential=body.differential, options=body.symptoms)
    ]

    return res

@diagnosis_router.get('/api/diagnosis', tags=TAGS['DIAGNOSIS'])
def get():
    # Pass filters as params
    # TODO: Get every register
    return ''

@diagnosis_router.delete('/api/diagnosis', tags=TAGS['DIAGNOSIS'])
def delete():
    # TODO: Add logical delete
    return ''