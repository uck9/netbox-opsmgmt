from datetime import date, datetime

from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.urls import reverse
from netbox.models import PrimaryModel
from utilities.choices import ChoiceSet


__all__ = (
    'MaintenanceTasks',
)

class TaskStatusChoices(ChoiceSet):
    key = 'Task.status'

    CHOICES = [
        ('001', 'Planned'),
        ('002', 'Completed'),
        ('003', 'Not Completed'),
        ('004', 'Deferred'),
    ]
STATUS_DEFAULT = TaskStatusChoices.CHOICES[0][0]

class MaintenanceTask(PrimaryModel):

    YEAR_CHOICES = [(y,y) for y in range(2024, date.today().year+1)]
    MONTH_CHOICE = [(m,m) for m in range(1,13)]

    def start_date(self):
        if self.start_year and self.start_month:
            return date(self.start_year, self.start_month, 1)
        elif self.start_year:
            # return Jan 1st
            return date(self.start_year, 1, 1)
        else:
            return None
        
    # Configure Model Colums    
    device= models.ForeignKey(
        to="dcim.Device",
        on_delete=models.CASCADE,
        verbose_name="Device",
        blank=True,
        null=True,
    )
    maintenance_task = models.TextField(blank=True, default="", verbose_name="")
    technical_impact = models.TextField(blank=True, default="", verbose_name="")
    last_review_date = models.DateField(blank=True, null=True)
    year = models.IntegerField(choices=YEAR_CHOICES, default=datetime.now().year,)
    month = models.IntegerField(choices=MONTH_CHOICE, default=datetime.now().month,)
    task_status =  models.CharField(max_length=10, choices=TaskStatusChoices, default=STATUS_DEFAULT)
    task_notes = models.CharField(max_length=512, blank=True)


    def get_absolute_url(self):
        return reverse('plugins:netbox_pmm:maintenancetask', args=[self.pk])