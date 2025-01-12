from netbox.filtersets import NetBoxModelFilterSet
from netbox_opsmgmt.models.impact import Impact


class ImpactfilterSet(NetBoxModelFilterSet):
    class Meta:
        model = Impact
        fields = ['name', 'impact_rating' ]
    
    def search(self, queryset, name, value):
        return queryset.filter(impact_rating__icontains=value)
