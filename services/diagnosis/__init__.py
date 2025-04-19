from factory.creators.EPAFactory import EPAFactory
from factory.creators.IAMFactory import IAMFactory
from factory.implementations.diagnosis import perform_diagnosis
from factory.interfaces.DiagnosisInterface import DiagnosisBody, DiagnosisResponse
from repositories.diagnosis import DiagnosisRepository
from repositories.diagnosis.model import CreateDiagnosisModel, DiagnosisModel


class DiagnosisService:
    def __init__(self):
        pass
    async def create_diagnosis(self, body: DiagnosisBody)-> DiagnosisModel:
        iam_factory = IAMFactory()
        epa_factory = EPAFactory()
        diagnosis: list[DiagnosisResponse] = [
            perform_diagnosis(factory=iam_factory, differential=body.differential, options=body.symptoms),
            perform_diagnosis(factory=epa_factory, differential=body.differential, options=body.symptoms)
        ]
        data: CreateDiagnosisModel = {
            **body.model_dump(),
            'diagnosis': diagnosis
        }
        repository = DiagnosisRepository()
        id = await repository.create_diagnosis(data=data)
        res: DiagnosisModel = {
            **data,
            'id': str(id),
        }
        return res


