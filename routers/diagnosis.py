from fastapi import APIRouter
from TAGS import TAGS
from factory.creators import EPAFactory, IAMFactory
from factory.implementations.diagnosis import perform_diagnosis
from factory.interfaces.DiagnosisInterface import CustomSelectOption

diagnosis_router = APIRouter()

# Register Entity
@diagnosis_router.post('/diagnosis', tags=TAGS['DIAGNOSIS'])
def create(options: list[CustomSelectOption]):
    iam_factory = IAMFactory(options)
    print(perform_diagnosis(iam_factory))
    epa_factory = EPAFactory(options)
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