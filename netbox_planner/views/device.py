from dcim.models import Device
from netbox_planner.models import Impact
from django.contrib.contenttypes.models import ContentType
from netbox.views import generic
from utilities.views import ViewTab, register_model_view


@register_model_view(Device, name='impact', path='impact')
class DeviceImpactsInfoView(generic.ObjectView):
    queryset = Device.objects.all()
    template_name = "netbox_planner/device_impacts_tab.html"
    tab = ViewTab(
        label='Impact Info', 
        permission='dcim.view_device', 
        badge=lambda obj: 1 if (obj.impact_assessment.count() == 1) else 0,
        weight=1200,
        hide_if_empty=True
    )
    
    child_model = Impact
    
    def get_extra_context(self, request, instance):

        content_type = ContentType()
        content_type = ContentType.objects.get(app_label="dcim", model="device")

        return {
            "impact": self.child_model.objects.filter(
                assigned_object_id=instance.id,
                assigned_object_type_id=content_type.id
                ).values()[0]
        }
    