from factory.interfaces.DiagnosisInterface import DiagnosisFactory

def diagnose(factory: DiagnosisFactory)-> float:
    diagnosis = factory.create_diagnosis()
    return diagnosis.make_diagnosis()
