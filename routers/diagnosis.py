from fastapi import APIRouter
from TAGS import TAGS
from factory.interfaces.DiagnosisInterface import DiagnosisBody
from repositories.diagnosis.model import DiagnosisModel
from services.diagnosis import DiagnosisService

diagnosis_router = APIRouter()

# Register Entity
@diagnosis_router.post('/api/diagnosis', tags=TAGS['DIAGNOSIS'])
async def create(body: DiagnosisBody)->DiagnosisModel:
    diagnosis = DiagnosisService()
    res = await diagnosis.create_diagnosis(body=body)
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