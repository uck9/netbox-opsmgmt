from utilities.choices import ChoiceSet

class ImpactRatingChoices(ChoiceSet):
    key = 'ImpactAssessment.rating'

    OUTAGE = 'OUTAGE'

    CHOICES = [
        ('NO-IMPACT', 'NO-IMPACT', 'green'),
        ('REDUCED-REDUNDANCY', 'REDUCED-REDUNDANCY', 'blue'),
        ('DEGRADED', 'DEGRADED','orange'),
        ('OUTAGE', 'OUTAGE', 'red'),
    ]
    