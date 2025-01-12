from django.contrib.contenttypes.models import ContentType
from circuits.models import Circuit
from netbox_opsmgmt.models import Impact
from netbox.views import generic
from utilities.views import ViewTab, register_model_view


@register_model_view(Circuit, name='impact', path='impact')
class CircuitImpactInfoView(generic.ObjectView):

    template_name = "netbox_opsmgmt/circuit_impacts_tab.html"
    tab = ViewTab(
        label='Impact Info', 
        permission='dcim.view_circuits',
        badge=lambda obj: 1 if (obj.impact_assessment.count() == 1) else 0,
        weight=1200,
        hide_if_empty=True
    )
    queryset = Circuit.objects.all()
    child_model = Impact
    
    def get_extra_context(self, request, instance):

        content_type = ContentType()
        content_type = ContentType.objects.get(app_label="circuits", model="circuit")

        return {
            "impact": self.child_model.objects.filter(
                assigned_object_id=instance.id,
                assigned_object_type_id=content_type.id
                ).values()[0],
        }
    