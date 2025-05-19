from factory.interfaces.DiagnosisInterface import DiagnosisFactory, PredictedDiagnosis, Option


def perform_diagnosis(factory: DiagnosisFactory, differential: Option, options: list[Option])->PredictedDiagnosis:
    diagnosis = factory.create_diagnosis()
    return diagnosis.make_diagnosis(differential, options)