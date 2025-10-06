from pydantic import BaseModel
from datetime import datetime
from factory.interfaces.DiagnosisInterface import PredictedDiagnosis, Option

class DiagnosisBody(BaseModel):
    firstName: str
    lastName: str
    age: int | None = None
    personId: str
    email: str
    differential: Option
    symptoms: list[Option]


class DiagnosisResponse(BaseModel):
    id: str
    diagnosis: list[PredictedDiagnosis]

class CreateDiagnosisModel(DiagnosisBody):
    diagnosis: list[PredictedDiagnosis]
    createdAt: datetime | None = None

class DiagnosisFilters(BaseModel):
    personId: list[str] | None = None
    firstName: list[str] | None = None
    lastName: list[str] | None = None
    email: list[str] | None = None
    search: str = ''

class PatientDiagnosisSummaryModel(BaseModel):
    id: str
    firstName: str
    lastName: str
    age: int | None = None
    email: str
    higherDiagnosis: PredictedDiagnosis
    mostFrequentSymptoms: Option

class PatientDiagnosisSummary(BaseModel):
    personId: str
    firstName: str
    lastName: str
    age: int | None = None
    email: str
    differential: Option
    count: int

class PatientDiagnosisResponse(BaseModel):
    personId: str
    firstName: str
    lastName: str
    age: int | None = None
    email: str
    differential: Option
    diagnosis: list[PredictedDiagnosis]
    symptoms: list[Option]
    createdAt: datetime

