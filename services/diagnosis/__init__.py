from factory.creators.DAFactory import DAFactory
from factory.creators.EPAFactory import EPAFactory
from factory.creators.IAMFactory import IAMFactory
from factory.implementations.diagnosis import perform_diagnosis
from repositories.diagnosis import DiagnosisRepository
from repositories.diagnosis.model import CreateDiagnosisModel, DiagnosisBody, DiagnosisFilters, DiagnosisResponse, PatientDiagnosisResponse, PatientDiagnosisSummary
from datetime import datetime

class DiagnosisService:
    def __init__(self):
        pass
    async def create_diagnosis(self, body: DiagnosisBody)-> DiagnosisResponse:
        iam_factory = IAMFactory()
        epa_factory = EPAFactory()
        da_factory = DAFactory()
        diagnosis: list[dict] = [
            perform_diagnosis(factory=iam_factory, differential=body.differential, options=body.symptoms).model_dump(),
            perform_diagnosis(factory=epa_factory, differential=body.differential, options=body.symptoms).model_dump(),
            perform_diagnosis(factory=da_factory, differential=body.differential, options=body.symptoms).model_dump(),
        ]
        diagnosis.sort(key=lambda x: x['diagnosis'], reverse=True)
        data: CreateDiagnosisModel = {
            **body.model_dump(),
            'diagnosis': diagnosis,
            'createdAt': datetime.now(),
        }
        repository = DiagnosisRepository()
        id: str = await repository.create_diagnosis(data=data)

        res: DiagnosisResponse = {
            'diagnosis': diagnosis,
            'id': id,
        }
        return res
    
    async def get_diagnosis(self, personId: str)-> list[PatientDiagnosisResponse]:
        repository = DiagnosisRepository()
        res: PatientDiagnosisResponse = await repository.get_diagnosis(personId=personId)
        return res
    
    async def get_diagnosis_summary(self, filters: DiagnosisFilters | None = None)-> list[PatientDiagnosisSummary]:
        repository = DiagnosisRepository()
        res: DiagnosisResponse = await repository.get_diagnosis_summary(filters=filters)
        return res


