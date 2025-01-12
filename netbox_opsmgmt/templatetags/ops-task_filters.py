from datetime import datetime, date
from dateutil.relativedelta import relativedelta
from django import template
from django.utils.safestring import mark_safe

register = template.Library()

def last_review_gt_six_months(value):
    return value < (date.today() - relativedelta(months=+6))


@register.filter(is_safe=True)
def last_review_date_badge_class(value):
    if not value:
        return

    if last_review_gt_six_months(value):
        return mark_safe('class="badge text-bg-danger"')
    else:
        return
    
@register.filter(is_safe=True)
def impact_rating_badge_class(value):
    if not value:
        return

    match value:
        case 'NO-IMPACT':
            return mark_safe('class="badge text-bg-success"')
        case 'REDUCED-REDUNDANCY':
            return mark_safe('class="badge text-bg-info"')
        case 'DEGRADED':
            return mark_safe('class="badge text-bg-warning"')
        case 'OUTAGE':
            return mark_safe('class="badge text-bg-danger"')
        case _:
            return mark_safe('class="badge text-bg-light"')

    
        