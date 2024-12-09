from ..interfaces.DiagnosisInterface import Diagnosis, Fields


class IAMDiagnosis(Diagnosis):
    code: str = 'IAM'
    def make_diagnosis(self, options: Fields)-> float:
        print('IAM: ', options)
        return 1.0