from fastapi import APIRouter
import TAGS
from factory.implementations.diagnosis import perform_diagnosis
from factory.interfaces.DiagnosisInterface import EPADiagnosisFactory, IAMDiagnosisFactory


diagnosis_router = APIRouter

# Register Entity
@diagnosis_router.post('/diagnosis', tags=TAGS['DIAGNOSIS'])
def create():
    # TODO: Calculate new diagnosis
    iam_factory = IAMDiagnosisFactory()
    print(perform_diagnosis(iam_factory))
    epa_factory = EPADiagnosisFactory()
    print(perform_diagnosis(epa_factory))
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