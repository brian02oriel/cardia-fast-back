
from factory.interfaces.DiagnosisInterface import Diagnosis, DiagnosisFactory, Fields
from factory.products.IAMDiagnosis import IAMDiagnosis


class IAMFactory(DiagnosisFactory):
    def create_diagnosis(self, options: Fields) -> Diagnosis:
        return IAMDiagnosis(options)