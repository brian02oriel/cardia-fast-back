from fastapi import APIRouter, Depends
from TAGS import TAGS
from repositories.diagnosis.model import DiagnosisBody, DiagnosisFilters, DiagnosisResponse, PatientDiagnosisResponse, PatientDiagnosisSummaryResponse
from services.diagnosis import DiagnosisService

diagnosis_router = APIRouter()

# Register Entity
@diagnosis_router.post('/api/diagnosis', tags=TAGS['DIAGNOSIS'])
async def create(body: DiagnosisBody)->DiagnosisResponse:
    diagnosis = DiagnosisService()
    res: DiagnosisResponse = await diagnosis.create_diagnosis(body=body)
    return res

@diagnosis_router.get('/api/diagnosis', tags=TAGS['DIAGNOSIS'])
async def get(personId: str = Depends())->list[PatientDiagnosisResponse]:
    diagnosis = DiagnosisService()
    res: list[PatientDiagnosisResponse] = await diagnosis.get_diagnosis(personId=personId)
    return res


@diagnosis_router.get('/api/diagnosis/summary', tags=TAGS['DIAGNOSIS'])
async def get(filters: DiagnosisFilters = Depends())->list[PatientDiagnosisSummaryResponse]:
    diagnosis = DiagnosisService()
    res: list[PatientDiagnosisSummaryResponse] = await diagnosis.get_diagnosis_summary(filters=filters)
    return res


@diagnosis_router.delete('/api/diagnosis', tags=TAGS['DIAGNOSIS'])
def delete():
    # TODO: Add logical delete
    return ''