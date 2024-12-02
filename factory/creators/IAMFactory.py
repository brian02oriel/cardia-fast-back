from factory.interfaces.DiagnosisInterface import DiagnosisFactory, Diagnosis
from factory.products import IAMDiagnosis


class EPAFactory(DiagnosisFactory):
    def create_diagnosis(self) -> Diagnosis:
        return IAMDiagnosis()