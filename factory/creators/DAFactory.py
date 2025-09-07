from factory.products.DADiagnosis import DADiagnosis
from ..interfaces.DiagnosisInterface import DiagnosisFactory, Diagnosis


class DAFactory(DiagnosisFactory):
    def create_diagnosis(self) -> Diagnosis:
        return DADiagnosis()