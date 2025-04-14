from pydantic import BaseModel

from factory.interfaces.DiagnosisInterface import DiagnosisBody, DiagnosisResponse


class DiagnosisModel(DiagnosisBody):
    id: str
    diagnosis: list[DiagnosisResponse]

class CreateDiagnosisModel(BaseModel):
    diagnosis: list[DiagnosisResponse]

