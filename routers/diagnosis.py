from fastapi import APIRouter
from fastapi.responses import JSONResponse
from TAGS import TAGS
from factory.creators.IAMFactory import IAMFactory
from factory.creators.EPAFactory import EPAFactory
from factory.implementations.diagnosis import perform_diagnosis
from factory.interfaces.DiagnosisInterface import Options

diagnosis_router = APIRouter()

# Register Entity
@diagnosis_router.post('/diagnosis', tags=TAGS['DIAGNOSIS'])
def create(options: Options):
    iam_factory = IAMFactory()
    res = {
        "IAM": perform_diagnosis(iam_factory, options)
    }
    return JSONResponse(res, status_code=200) 

@diagnosis_router.get('/diagnosis', tags=TAGS['DIAGNOSIS'])
def get():
    # Pass filters as params
    # TODO: Get every register
    return ''

@diagnosis_router.delete('/diagnosis', tags=TAGS['DIAGNOSIS'])
def delete():
    # TODO: Add logical delete
    return ''