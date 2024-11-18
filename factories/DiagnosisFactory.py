from typing import Protocol

from factories import Diagnosis
from factories.diagnosis import EPADiagnosis, IAMDiagnosis

class DiagnosisFactory(Protocol):
    def create_diagnosis(self)-> Diagnosis:
        pass

class IAMDiagnosisFactory(DiagnosisFactory):
    def create_diagnosis(self)-> Diagnosis:
        return IAMDiagnosis()

class EPADiagnosisFactory(DiagnosisFactory):
    def create_diagnosis(self)-> Diagnosis:
        return EPADiagnosis()