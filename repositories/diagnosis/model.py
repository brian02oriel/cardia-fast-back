from pydantic import BaseModel

from factory.interfaces.DiagnosisInterface import PredictedDiagnosis, Option

class DiagnosisBody(BaseModel):
    firstName: str
    lastName: str
    personId: str
    email: str
    differential: list[Option]
    symptoms: list[Option]


class DiagnosisResponse(BaseModel):
    id: str
    diagnosis: list[PredictedDiagnosis]

class CreateDiagnosisModel(DiagnosisBody):
    diagnosis: list[PredictedDiagnosis]

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
    higherDiagnosis: PredictedDiagnosis
    mostFrequentSymptoms: Option