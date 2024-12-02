from factory.interfaces.DiagnosisInterface import Diagnosis


class IAMDiagnosis(Diagnosis):
    def make_diagnosis(self)-> float:
        return 1.0