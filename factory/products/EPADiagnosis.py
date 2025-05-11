from factory.interfaces.DiagnosisInterface import Diagnosis, PredictedDiagnosis, ESeverity, Factors, Option, Rules


class EPADiagnosis(Diagnosis):
    name = "Embolia Pulmonar Aguda"
    code = "EPA"
    def get_rules(self) -> list[Rules]:
        return [
            {
                'count': 2,
                'percentage': 10.0
            },
            {
                'count': 6,
                'percentage': 50.0
            },
            {
                'count': 7,
                'percentage': 75.0
            }
        ]
    def get_factors(self) -> list[Factors]:
        return [
            {
                'code': 'deepVeinThrombosis',
                'points': 3
            },
            {
                'code': 'alternativeToEP',
                'points': 3
            },
            {
                'code': 'beatsPerMinutesOverHundred',
                'points': 1.5
            },
            {
                'code': 'previousSurgery',
                'points': 1.5
            },
            {
                'code': 'previousTVPOrEp',
                'points': 1.5
            },
            {
                'code': 'hemoptisis',
                'points': 1
            },
            {
                'code': 'activeCancer',
                'points': 1
            }
        ]

    def get_severity(self, diagnosis: float)-> ESeverity:
        if diagnosis <= 10:
            return ESeverity.LOW
        elif diagnosis < 50:
            return ESeverity.MEDIUM
        else:
            return ESeverity.HIGH

    def make_diagnosis(self, differential: list[Option], options: list[Option])-> float:
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