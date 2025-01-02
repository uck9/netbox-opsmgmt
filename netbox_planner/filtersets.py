from netbox.filtersets import NetBoxModelFilterSet
from netbox_planner.models.impact import Impact


class ImpactilterSet(NetBoxModelFilterSet):
    class Meta:
        model = Impact
        fields = ['name', 'impact_Rating' ]
    
    def search(self, queryset, name, value):
        return queryset.filter(impact_rating__icontains=value)
