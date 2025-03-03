from ..interfaces.DiagnosisInterface import DiagnosisFactory, Diagnosis
from factory.products.EPADiagnosis import EPADiagnosis


class EPAFactory(DiagnosisFactory):
    def create_diagnosis(self) -> Diagnosis:
        return EPADiagnosis()