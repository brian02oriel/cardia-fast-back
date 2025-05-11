from factory.interfaces.DiagnosisInterface import Diagnosis, PredictedDiagnosis, ESeverity, Factors, Option, Rules


class IAMDiagnosis(Diagnosis):
    name = "Infarto Agudo del Miocardio"
    code = "IAM"
    def get_rules(self)-> list[Rules]:
        return [
                {
                    'count': 1,
                    'percentage': 4.7
                },
                {
                    'count': 2,
                    'percentage': 8.3
                },
                {
                    'count': 3,
                    'percentage': 13.2
                },
                {
                    'count': 4,
                    'percentage': 19.9
                },
                {
                    'count': 5,
                    'percentage': 26.2
                },
                {
                    'count': 6,
                    'percentage': 40.9
                },
            ]
    
    def get_factors(self)->list[Factors]:
        return [
                {
                    'code': 'olderThan65',
                    'points': 1
                },
                {
                    'code': 'hypertension',
                    'points': 0.33
                },
                {
                    'code': 'diabetes',
                    'points': 0.33
                },
                {
                    'code': 'hyperlipidemia',
                    'points': 0.33
                },
                {
                    'code': 'smoker',
                    'points': 0.33
                },
                {
                    'code': 'historyOfHeartDisease',
                    'points': 1
                },
                {
                    'code': 'historyOfCoronaryStenosis',
                    'points': 1
                },
                {
                    'code': 'anginaEpisodes',
                    'points': 1
                },
                {
                    'code': 'aspirinUsage',
                    'points': 1
                },
                {
                    'code': 'segmentSTChanges',
                    'points': 1
                },
                {
                    'code': 'necrosisMarkers',
                    'points': 1
                },
            ]
    
    def get_severity(self, diagnosis: float)-> ESeverity:
        if diagnosis <= 10:
            return ESeverity.LOW
        elif diagnosis < 40:
            return ESeverity.MEDIUM
        else:
            return ESeverity.HIGH
    
    def make_diagnosis(self, differential: list[Option], options: list[Option])-> PredictedDiagnosis:
        rules = self.get_rules()
        factors = self.get_factors()
        selected_values = [ option.value for option in options]
        selected_factors = [ factor for factor in factors if factor['code'] in selected_values]
        count = sum(selected_factor["points"] for selected_factor in selected_factors)
        diagnose = 0
        symptoms = [ Option(value= option.value, label= option.label) for option in options if option.value in [ factor["code"] for factor in selected_factors]]
        if not count:
            return PredictedDiagnosis(diagnosis=diagnose, severity= self.get_severity(diagnose), symptoms= symptoms, differential= differential, name= self.name, code= self.code)
        for rule in rules:
            if rule["count"] >= count:
                diagnose = rule["percentage"]
                break
        return PredictedDiagnosis(diagnosis= round(diagnose, 2), severity= self.get_severity(diagnose), symptoms= symptoms, differential= differential, name= self.name, code= self.code)