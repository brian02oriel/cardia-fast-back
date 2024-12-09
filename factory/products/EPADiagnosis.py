from factory.interfaces.DiagnosisInterface import Diagnosis, Options


class EPADiagnosis(Diagnosis):
    code: str = 'EPA'
    def make_diagnosis(self, options: Options)-> float:
        print("EPA: ", options)
        return 1.0