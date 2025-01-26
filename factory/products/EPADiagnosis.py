from factory.interfaces.DiagnosisInterface import Diagnosis, Factors, Options, Rules


class EPADiagnosis(Diagnosis):
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
                'code': 'tvp',
                'points': 3
            },
            {
                'code': 'ep',
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

    def make_diagnosis(self, options: Options)-> float:
        rules = self.get_rules()
        factors = self.get_factors()
        selected_codes = [ option.code for option in options.options]
        selected_factors = [ factor for factor in factors if factor['code'] in selected_codes]
        count = sum(selected_factor["points"] for selected_factor in selected_factors)
        diagnose = 0
        if not count:
            return 0
        for rule in rules:
            if rule["count"] >= count:
                diagnose = rule["percentage"]
                break
        return diagnose