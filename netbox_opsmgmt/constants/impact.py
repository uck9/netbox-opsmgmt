from django.db.models import Q

__all__ = (
    'IMPACT_ASSIGNMENT_MODELS',
)

IMPACT_ASSIGNMENT_MODELS = Q(
    Q(app_label='dcim', model='device') |
    Q(app_label='circuits', model='circuit')
)