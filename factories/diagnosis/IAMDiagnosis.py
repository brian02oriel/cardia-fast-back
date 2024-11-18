from factories.diagnosis import Diagnosis


class IAMDiagnosis(Diagnosis):
    def __init__(self, code):
        self.code = code
    
    def make_diagnosis(self, code)-> float:
        return 1.0