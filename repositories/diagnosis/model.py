from pydantic import BaseModel

from factory.interfaces.DiagnosisInterface import PredictedDiagnosis, Option

class DiagnosisBody(BaseModel):
    firstName: str
    lastName: str
    personId: str
    email: str
    differential: Option
    symptoms: list[Option]


class DiagnosisResponse(BaseModel):
    id: str
    diagnosis: list[PredictedDiagnosis]

class CreateDiagnosisModel(DiagnosisBody):
    diagnosis: list[PredictedDiagnosis]

class DiagnosisFilters(BaseModel):
    personId: list[str] | None = None
    firstName: list[str] | None = None
    lastName: list[str] | None = None
    email: list[str] | None = None
    search: str = ''

class PatientDiagnosisModel(BaseModel):
    id: str
    firstName: str
    lastName: str
    email: str
    higherDiagnosis: PredictedDiagnosis
    mostFrequentSymptoms: Option

class PatientDiagnosisResponse(BaseModel):
    personId: str
    firstName: str
    lastName: str
    email: str
    differential: Option
    count: int