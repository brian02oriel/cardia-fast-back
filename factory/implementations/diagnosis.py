from factory.interfaces.DiagnosisInterface import DiagnosisFactory, DiagnosisResponse, Option


def perform_diagnosis(factory: DiagnosisFactory, differential: list[Option], options: list[Option])->DiagnosisResponse:
    diagnosis = factory.create_diagnosis()
    return diagnosis.make_diagnosis(differential, options)