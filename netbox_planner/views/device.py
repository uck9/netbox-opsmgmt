import logging

from dcim.models import Device
from netbox_planner.models import Impact
from netbox_planner.tables import ImpactTable
from netbox.views import generic
from utilities.views import ViewTab, register_model_view


logger = logging.getLogger(__name__)


@register_model_view(Device, name='impact', path='impact')
class DeviceImpactsInfoView(generic.ObjectView):

    template_name = "netbox_planner/device_impacts_tab.html"
    tab = ViewTab(
        label='Impact Info', 
        permission='dcim.view_device', 
        badge=lambda obj: 1 if (obj.impact_assessment.count() == 1) else 0,
        weight=1200,
        hide_if_empty=True
    )
    queryset = Device.objects.all()
    child_model = Impact
    
    def get_extra_context(self, request, instance):

        return {
            "object": self.child_model.objects.filter(
                assigned_object_id=instance.id,
                ).values()[0]
        }
    