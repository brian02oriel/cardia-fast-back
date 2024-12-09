from factory.interfaces.DiagnosisInterface import DiagnosisFactory, Options


def perform_diagnosis(factory: DiagnosisFactory, options: Options)->float:
    diagnosis = factory.create_diagnosis()
    return diagnosis.make_diagnosis(options)