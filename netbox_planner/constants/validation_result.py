from django.db.models import Q

__all__ = (
    'VALIDATION_RESULT',
)

VALIDATION_RESULT_ASSIGNMENT_MODELS = Q(
    Q(app_label='dcim', model='device')
)