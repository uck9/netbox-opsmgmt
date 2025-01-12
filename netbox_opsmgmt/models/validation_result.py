from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.urls import reverse
from django.conf import settings

from dcim.models import Device
from circuits.models import Circuit
from netbox.models import PrimaryModel
from utilities.choices import ChoiceSet

from netbox_opsmgmt.constants.validation_result import VALIDATION_RESULT_ASSIGNMENT_MODELS
from netbox_opsmgmt.choices.validation_result import ValidationTypeChoices

__all__ = (
    'OpsTask',
)


class ValidationResult(PrimaryModel):
    # Configure Model Colums
    validation_type = models.CharField(max_length=50, choices=ValidationTypeChoices)
    date_last_run = models.DateField(blank=True, null=True)
    result_score = models.IntegerField(blank=False, null=False)
    result_is_ok = models.BooleanField(blank=False, default=False)    
    comments = models.TextField(blank=True, default="", verbose_name="Validation Comments")
    details_url = models.URLField(blank=True)

    assigned_object_type = models.ForeignKey(
        to=ContentType,
        limit_choices_to=VALIDATION_RESULT_ASSIGNMENT_MODELS,
        on_delete=models.CASCADE,
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

    class Meta:
        ordering = ['validation_type']

    @property
    def name(self):
        return self
    
    def __str__(self):
        if not self.assigned_object:
            return f'{self.pk}'
        elif isinstance(self.assigned_object, Circuit):
            return f'Circuit: {self.assigned_object.cid}'
        return f'Device: {self.assigned_object.name}'

    def get_task_outcome_color(self):
        if self.outcome_status is None:
            return
        return OpsTaskOutcomeChoices.colors.get(self.outcome_status)

    def get_absolute_url(self):
        return reverse('plugins:netbox_opsmgmt:ops-task', args=[self.pk])
    