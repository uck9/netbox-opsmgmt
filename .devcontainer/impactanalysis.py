from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.urls import reverse
from django.conf import settings

from netbox.forms import NetBoxModelForm

__all__ = (
    'ImpactAnalysis',
)


class ImpactAnalysis(NetBoxModelForm):
        
    # Configure Model Colums    
    device= models.ForeignKey(
        to="dcim.Device",
        on_delete=models.CASCADE,
        verbose_name="Device",
        blank=True,
        null=True,
    )
    business_impact = models.TextField(blank=True, default="", verbose_name="Business Impact")
    technical_impact = models.TextField(blank=True, default="", verbose_name="Technical Impact")
    last_review_date = models.DateField(blank=True, null=True)
    estimated_duration = models.TextField(blank=True, default="", verbose_name="Estimated Impact Duration")

    def get_absolute_url(self):
        return reverse('plugins:netbox_pmm:impactanalysis', args=[self.pk])