from django.contrib.postgres.fields import ArrayField
from django.db import models
from netbox.models import PrimaryModel

__all__ = (
    'MaintenanceTasks',
)


class MaintenanceTasks(PrimaryModel):
        
    # Configure Model Colums    
    device= models.ForeignKey(
        to="dcim.Device",
        on_delete=models.CASCADE,
        verbose_name="Device",
        blank=True,
        null=True,
    )
    maintenance_task = models.TextField(blank=True, default="", verbose_name="Business Impact")
    technical_impact = models.TextField(blank=True, default="", verbose_name="Technical Impact")
    last_review_date = models.DateField(blank=True, null=True)
    
    task_status = 



    def get_absolute_url(self):
        return reverse('plugins:netbox_pmm:maintenancetasks', args=[self.pk])