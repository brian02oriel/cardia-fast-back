from ..interfaces.DiagnosisInterface import Diagnosis, Fields


class EPADiagnosis(Diagnosis):
    code: str = 'EPA'
    def make_diagnosis(self, options: Fields)-> float:
        print("EPA: ", options)
        return 1.0