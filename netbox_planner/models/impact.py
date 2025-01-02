from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.urls import reverse
from django.conf import settings

from dcim.models import Device
from circuits.models import Circuit
from netbox.models import PrimaryModel
from utilities.choices import ChoiceSet

from netbox_planner.constants.impact import IMPACT_ASSIGNMENT_MODELS
from netbox_planner.choices.impact import ImpactRatingChoices

__all__ = (
    'Impact',
)


class Impact(PrimaryModel):
    # Configure Model Colums    
    assigned_object_type = models.ForeignKey(
        to=ContentType,
        limit_choices_to=IMPACT_ASSIGNMENT_MODELS,
        on_delete=models.PROTECT,
        related_name='+',
        blank=True,
        null=True
    )
    assigned_object_id = models.PositiveBigIntegerField(
        blank=True,
        null=True
    )
    assigned_object = GenericForeignKey(
        ct_field='assigned_object_type',
        fk_field='assigned_object_id'
    )
    crit_ep_impacted = models.BooleanField(default=False)
    impact_rating = models.CharField(max_length=30, choices=ImpactRatingChoices, default=ImpactRatingChoices.OUTAGE)
    bus_impact_assess = models.TextField(blank=True, default="", verbose_name="Business Impact Assessment")
    tech_impact_assess = models.TextField(blank=True, default="", verbose_name="Technical Impact Assessment")
    last_review_date = models.DateField(blank=True, null=True)

    class Meta:
        ordering = ['assigned_object_type']
        constraints = (
            models.UniqueConstraint(
                'assigned_object_type', 'assigned_object_id',
                name='%(app_label)s_%(class)s_unique_object',
                violation_error_message="Objects must be unique."
            ),
        )

    @property
    def name(self):
        return self
    
    def __str__(self):
        if not self.assigned_object:
            return f'{self.pk}'
        elif isinstance(self.assigned_object, Circuit):
            return f'Circuit: {self.assigned_object.cid}'
        return f'Device: {self.assigned_object.name}'

    def get_impact_rating_color(self):
        if self.impact_rating is None:
            return
        return ImpactRatingChoices.colors.get(self.impact_rating)

    def get_absolute_url(self):
        return reverse('plugins:netbox_planner:impact', args=[self.pk])
    