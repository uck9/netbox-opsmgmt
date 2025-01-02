from netbox.filtersets import NetBoxModelFilterSet
from netbox_planner.models.impact import Impact


class ImpactfilterSet(NetBoxModelFilterSet):
    class Meta:
        model = Impact
        fields = ['name', 'impact_Rating' ]
    
    def search(self, queryset, name, value):
        return queryset.filter(impact_rating__icontains=value)
