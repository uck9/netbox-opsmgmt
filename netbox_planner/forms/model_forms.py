from django import forms
from django.utils.translation import gettext as _

from dcim.models import Device
from circuits.models import Circuit
from netbox.forms import NetBoxModelForm

from netbox_planner.models.impact import Impact

from utilities.forms.fields import CommentField, DynamicModelChoiceField, DynamicModelMultipleChoiceField
from utilities.forms.widgets import DatePicker

__all__ = (
    'ImpactForm',
)

class ImpactForm(NetBoxModelForm):

    circuit = DynamicModelChoiceField(
        queryset=Circuit.objects.all(),
        required=False,
        selector=True,
        label=_('Circuit'),
    )
    device = DynamicModelChoiceField(
        queryset=Device.objects.all(),
        required=False,
        selector=True,
        label=_('Device'),
    )

    bus_impact_assess = CommentField()
    tech_impact_assess = CommentField()

    class Meta:
        model = Impact

        fields = (
            'crit_ep_impacted', 'impact_rating', 'bus_impact_assess', 'tech_impact_assess', 'last_review_date', 'tags', 'comments',
        )

        widgets = {
            'last_review_date': DatePicker(),
        }

    def __init__(self, *args, **kwargs):
        # Initialize helper selectors
        instance = kwargs.get('instance')
        initial = kwargs.get('initial', {}).copy()
        if instance:
            if (instance.id == None):
                kwargs['initial'] = initial
            elif (instance.assigned_object_type.name == 'circuit'):
                initial['circuit'] = instance.assigned_object
            elif type(instance.assigned_object_type.name == 'device'):
                initial['device'] = instance.assigned_object
        kwargs['initial'] = initial

        super().__init__(*args, **kwargs)

    def clean(self):
        super().clean()

        # Handle object assignment
        selected_objects = [
            field for field in ('circuit', 'device') if self.cleaned_data[field]
        ]

        if len(selected_objects) > 1:
            raise forms.ValidationError({
                selected_objects[1]: "You can only have a impact assessment for a circuit or device"
            })
        elif selected_objects:
            self.instance.assigned_object = self.cleaned_data[selected_objects[0]]
        else:
            self.instance.assigned_object = None
            