from django.contrib.contenttypes.models import ContentType
from drf_spectacular.utils import extend_schema_field
from rest_framework import serializers

from netbox.api.fields import ContentTypeField
from netbox.api.serializers import NetBoxModelSerializer
from netbox_opsmgmt.models import Impact
from utilities.api import get_serializer_for_model


__all__ = (
    'ImpactSerializer',
)


class ImpactSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='plugins-api:netbox_opsmgmt-api:impact-detail')
    assigned_object_type = ContentTypeField(
        queryset=ContentType.objects.all()
    )

    last_review_date = serializers.DateField(required=False)

    class Meta:
        model = Impact
        fields = (
            'url', 'id', 'display', 'assigned_object_type', 'assigned_object_id', 'crit_ep_impacted',
            'impact_rating', 'bus_impact_assess', 'tech_impact_assess', 'last_review_date',
            'description', 'comments', 'tags', 'custom_fields',
            
        )
        brief_fields = (
            'url', 'id', 'display', 'assigned_object_type', 'assigned_object_id', 'end_of_sale', 'assigned_object_count',
        )

    @extend_schema_field(serializers.JSONField(allow_null=True))
    def get_assigned_object(self, instance):
        serializer = get_serializer_for_model(instance.assigned_object)
        context = {'request': self.context['request']}
        return serializer(instance.assigned_object, context=context, nested=True).data