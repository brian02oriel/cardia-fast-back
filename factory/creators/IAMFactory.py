
from factory.interfaces.DiagnosisInterface import Diagnosis, DiagnosisFactory, Options
from factory.products.IAMDiagnosis import IAMDiagnosis


class IAMFactory(DiagnosisFactory):
    def create_diagnosis(self) -> Diagnosis:
        return IAMDiagnosis()