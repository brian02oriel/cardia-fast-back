from fastapi import APIRouter
from fastapi.responses import JSONResponse
from TAGS import TAGS
from factory.creators.IAMFactory import IAMFactory
from factory.creators.EPAFactory import EPAFactory
from factory.implementations.diagnosis import perform_diagnosis
from factory.interfaces.DiagnosisInterface import DiagnosisBody

diagnosis_router = APIRouter()

# Register Entity
@diagnosis_router.post('/api/diagnosis', tags=TAGS['DIAGNOSIS'])
def create(body: DiagnosisBody):
    iam_factory = IAMFactory()
    epa_factory = EPAFactory()
    res = {
        "IAM": perform_diagnosis(factory=iam_factory, options=body.symptoms),
        "EPA": perform_diagnosis(factory=epa_factory, options=body.symptoms)
    }
    return JSONResponse(res, status_code=200) 

@diagnosis_router.get('/api/diagnosis', tags=TAGS['DIAGNOSIS'])
def get():
    # Pass filters as params
    # TODO: Get every register
    return ''

@diagnosis_router.delete('/api/diagnosis', tags=TAGS['DIAGNOSIS'])
def delete():
    # TODO: Add logical delete
    return ''