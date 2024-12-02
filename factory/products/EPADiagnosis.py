from factory.interfaces.DiagnosisInterface import Diagnosis


class EPADiagnosis(Diagnosis):
    def make_diagnosis(self)-> float:
        return 1.0