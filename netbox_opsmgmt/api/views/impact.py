from netbox.api.viewsets import NetBoxModelViewSet
from netbox_opsmgmt.api.serializers import ImpactSerializer
from netbox_opsmgmt.models import Impact


__all__ = (
    'ImpactViewSet',
)


class ImpactViewSet(NetBoxModelViewSet):
    queryset = Impact.objects.all()
    serializer_class = ImpactSerializer
