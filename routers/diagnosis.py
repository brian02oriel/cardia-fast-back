from fastapi import APIRouter
import TAGS
from factories.DiagnosisFactory import EPADiagnosisFactory, IAMDiagnosisFactory


diagnosis_router = APIRouter

# Register Entity
@diagnosis_router.post('/diagnosis', tags=TAGS['DIAGNOSIS'])
def create():
    # TODO: Calculate new diagnosis
    iam = IAMDiagnosisFactory().create_diagnosis().make_diagnosis()
    epa = EPADiagnosisFactory().create_diagnosis().make_diagnosis()
    # TODO: Save patient and diagnosis
    return ''

@diagnosis_router.get('/diagnosis', tags=TAGS['DIAGNOSIS'])
def get():
    # Pass filters as params
    # TODO: Get every register
    return ''

@diagnosis_router.post('/diagnosis', tags=TAGS['DIAGNOSIS'])
def delete():
    # TODO: Add logical delete
    return ''