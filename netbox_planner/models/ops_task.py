from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.urls import reverse
from django.conf import settings

from dcim.models import Device
from circuits.models import Circuit
from netbox.models import PrimaryModel
from utilities.choices import ChoiceSet

from netbox_planner.constants.ops_task import OPS_TASK_ASSIGNMENT_MODELS
from netbox_planner.choices.ops_task import OpsTaskTypeChoices, OpsTaskOutcomeChoices

__all__ = (
    'OpsTask',
)


class OpsTask(PrimaryModel):
    # Configure Model Colums
    task_type = models.CharField(max_length=50, choices=TaskTypeChoices, default=TaskTypeChoices.CURRENCY_UPGRADE)
    date_start = models.DateField(blank=True, null=False)
    date_end_planned = models.DateField(blank=True, null=False)
    date_end_actual = models.DateField(blank=True, null=True)
    task_outcome = models.CharField(max_length=50, choices=TaskOutcomeChoices, default=TaskOutcomeChoices.NO_ISSUES)
    outcome_details = models.TextField(blank=True, default="", verbose_name="Outcome Details")
    task_completed = models.BooleanField(default=False)

    assigned_object_type = models.ForeignKey(
        to=ContentType,
        limit_choices_to=TASK_ASSIGNMENT_MODELS,
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
        ordering = ['date_start']

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
        return reverse('plugins:netbox_planner:ops-task', args=[self.pk])
    