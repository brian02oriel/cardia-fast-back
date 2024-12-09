from ..interfaces.DiagnosisInterface import DiagnosisFactory, Diagnosis, Fields
from factory.products.EPADiagnosis import EPADiagnosis


class EPAFactory(DiagnosisFactory):
    def create_diagnosis(self, options: Fields) -> Diagnosis:
        return EPADiagnosis(options)