from factory.interfaces.DiagnosisInterface import DiagnosisFactory


def perform_diagnosis(factory: DiagnosisFactory)->float:
    diagnosis = factory.create_diagnosis()
    return diagnosis.make_diagnosis()