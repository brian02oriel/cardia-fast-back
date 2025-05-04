from pydantic import BaseModel

from factory.interfaces.DiagnosisInterface import DiagnosisBody, DiagnosisResponse, Option


class DiagnosisModel(BaseModel):
    id: str
    diagnosis: list[DiagnosisResponse]

class CreateDiagnosisModel(DiagnosisBody):
    diagnosis: list[DiagnosisResponse]

class DiagnosisFilters(BaseModel):
    personId: list[str] = []
    firstName: list[str] = []
    lastName: list[str] = []
    email: list[str] = []
    search: str = ''

class PatientDiagnosisModel(BaseModel):
    id: str
    firstName: str
    lastName: str
    email: str
    higherDiagnosis: DiagnosisResponse
    mostFrequentSymptoms: Option