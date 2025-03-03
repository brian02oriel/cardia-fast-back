from factory.interfaces.DiagnosisInterface import DiagnosisFactory, Option


def perform_diagnosis(factory: DiagnosisFactory, options: list[Option])->float:
    diagnosis = factory.create_diagnosis()
    return diagnosis.make_diagnosis(options)