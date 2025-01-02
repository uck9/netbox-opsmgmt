from netbox.api.viewsets import NetBoxModelViewSet
from netbox_planner.api.serializers import ImpactSerializer
from netbox_planner.models import Impact


__all__ = (
    'ImpactViewSet',
)


class ImpactViewSet(NetBoxModelViewSet):
    queryset = Impact.objects.all()
    serializer_class = ImpactSerializer
