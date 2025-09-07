from factory.interfaces.DiagnosisInterface import Diagnosis, PredictedDiagnosis, ESeverity, Factors, Option, Rules


class DADiagnosis(Diagnosis):
    name = "Disección Aórtica"
    code = "DA"
    def get_rules(self) -> list[Rules]:
        return [
            {
                'count': 0,
                'percentage': 0
            },
            {
                'count': 1,
                'percentage': 50.0
            },
            {
                'count': 2,
                'percentage': 90.0
            },
            {
                'count': 3,
                'percentage': 90.0
            },
        ]
    # The key finding is that using ADD-RS ≥ 2 instead of ADD-RS ≥ 1 as your cutoff increases your miss rate from 0.8% to 3% 
    # - this represents a nearly 4-fold increase in the chance of missing an aortic dissection, which could be fatal.
    def get_factors(self) -> list[Factors]:
        high_risk_conditions = ['marfanSyndrome', 'aorticValveDisease', 'familyHistoryOfAorticDisease']
        high_risk_pain_features = ['chestPain', 'backPain', 'abdominalPain']
        high_risk_exam_features = ['pulseDeficit', 'systolicBloodPressureDifference', 'focalNeurologicDeficit']
        return [
            {
                'code': high_risk_conditions,
                'points': 1
            },
            {
                'code': high_risk_pain_features,
                'points': 1
            },
            {
                'code': high_risk_exam_features,
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

    def make_diagnosis(self, differential: Option, options: list[Option])-> float:
        rules = self.get_rules()
        factors = self.get_factors()
        selected_values = [ option.value for option in options]
        selected_factors = []
        symptoms = []
        count = 0
        for factor in factors:
            if isinstance(factor['code'], list):
                if any(code in selected_values or [differential] for code in factor['code']):
                    selected_factors.append(factor)
                    count += factor['points']
    
        all_factors = [ factor['code'] for factor in factors if isinstance(factor['code'], list)]
        flat_factors = [factor for sublist_factors in all_factors for factor in sublist_factors]
        symptoms = [option for option in options if option.value in flat_factors]
        diagnose = 0
        if not count:
            return PredictedDiagnosis(diagnosis=diagnose, severity= self.get_severity(diagnose), symptoms= symptoms, differential= differential, name= self.name, code= self.code)
        for rule in rules:
            if rule["count"] >= count:
                diagnose = rule["percentage"]
                break
        return PredictedDiagnosis(diagnosis= round(diagnose, 2), severity= self.get_severity(diagnose), symptoms= symptoms, differential= differential, name= self.name, code= self.code)