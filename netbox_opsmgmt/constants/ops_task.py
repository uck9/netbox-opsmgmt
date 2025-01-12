from django.db.models import Q

__all__ = (
    'OPS_TASK_ASSIGNMENT_MODELS',
)

OPS_TASK_ASSIGNMENT_MODELS = Q(
    Q(app_label='dcim', model='device') |
    Q(app_label='circuits', model='circuit')
)