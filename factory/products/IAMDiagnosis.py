from factory.interfaces.DiagnosisInterface import Diagnosis, Factors, Options, Rules


class IAMDiagnosis(Diagnosis):
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
    
    def make_diagnosis(self, options: Options)-> float:
        rules = self.get_rules()
        factors = self.get_factors()
        selected_codes = [ option.code for option in options.options]
        selected_factors = [ factor for factor in factors if factor['code'] in selected_codes]
        count = sum(selected_factor["points"] for selected_factor in selected_factors)
        diagnose = 0
        for rule in rules:
            if rule["count"] >= count:
                diagnose = rule["percentage"]
                break
        return diagnose