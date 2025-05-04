from fastapi import APIRouter
from TAGS import TAGS
from factory.interfaces.DiagnosisInterface import DiagnosisBody
from repositories.diagnosis.model import DiagnosisFilters, DiagnosisModel
from services.diagnosis import DiagnosisService

diagnosis_router = APIRouter()

# Register Entity
@diagnosis_router.post('/api/diagnosis', tags=TAGS['DIAGNOSIS'])
async def create(body: DiagnosisBody)->DiagnosisModel:
    diagnosis = DiagnosisService()
    res: DiagnosisModel = await diagnosis.create_diagnosis(body=body)
    return res

@diagnosis_router.get('/api/diagnosis', tags=TAGS['DIAGNOSIS'])
def get(filters: DiagnosisFilters):
    diagnosis = DiagnosisService()
    res: DiagnosisModel = diagnosis.get_diagnosis(filters=filters)
    return res

@diagnosis_router.delete('/api/diagnosis', tags=TAGS['DIAGNOSIS'])
def delete():
    # TODO: Add logical delete
    return ''