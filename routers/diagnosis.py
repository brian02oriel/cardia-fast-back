from fastapi import APIRouter
from TAGS import TAGS
from factory.creators.IAMFactory import IAMFactory
from factory.creators.EPAFactory import EPAFactory
from factory.implementations.diagnosis import perform_diagnosis
from factory.interfaces.DiagnosisInterface import DiagnosisBody, DiagnosisResponse
from repositories.diagnosis.model import DiagnosisModel
from services.diagnosis import DiagnosisService

diagnosis_router = APIRouter()

# Register Entity
@diagnosis_router.post('/api/diagnosis', tags=TAGS['DIAGNOSIS'])
def create(body: DiagnosisBody)->DiagnosisModel:
    diagnosis = DiagnosisService()
    return diagnosis.create_diagnosis(data=body)

@diagnosis_router.get('/api/diagnosis', tags=TAGS['DIAGNOSIS'])
def get():
    # Pass filters as params
    # TODO: Get every register
    return ''

@diagnosis_router.delete('/api/diagnosis', tags=TAGS['DIAGNOSIS'])
def delete():
    # TODO: Add logical delete
    return ''