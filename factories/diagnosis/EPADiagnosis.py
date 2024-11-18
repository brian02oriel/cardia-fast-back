from factories.diagnosis import Diagnosis


class EPADiagnosis(Diagnosis):
    def __init__(self, code):
        self.code = code
    
    def make_diagnosis(self, code)-> float:
        return 1.0