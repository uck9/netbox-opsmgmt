from netbox.views.generic import (ObjectListView, ObjectEditView, ObjectDeleteView, ObjectView, BulkEditView,
                                  BulkDeleteView)

from netbox_opsmgmt.forms.model_forms import ImpactForm
from netbox_opsmgmt.models import Impact
from netbox_opsmgmt.tables import ImpactTable
from utilities.views import register_model_view

__all__ = (
    'ImpactListView',
    'ImpactView',
    'ImpactEditView',
    'ImpactBulkEditView',
    'ImpactDeleteView',
    'ImpactBulkDeleteView',
)

@register_model_view(Impact, name='list')
class ImpactListView(ObjectListView):
    queryset = Impact.objects.all()
    table = ImpactTable
    #filterset = ImpactFilterSet
    #filterset_form = ImpactFilterForm


@register_model_view(Impact)
class ImpactView(ObjectView):
    queryset = Impact.objects.all()


@register_model_view(Impact, 'edit')
class ImpactEditView(ObjectEditView):
    template_name = 'netbox_opsmgmt/impact_edit.html'
    queryset = Impact.objects.all()
    form = ImpactForm


@register_model_view(Impact, 'bulk_edit')
class ImpactBulkEditView(BulkEditView):
    queryset = Impact.objects.all()
    #filterset = ImpactFilterSet
    table = ImpactTable
    #form = ImpactBulkEditForm


@register_model_view(Impact, 'delete')
class ImpactDeleteView(ObjectDeleteView):
    queryset = Impact.objects.all()


@register_model_view(Impact, 'bulk_delete')
class ImpactBulkDeleteView(BulkDeleteView):
    queryset = Impact.objects.all()
    #filterset = ImpactFilterSet
    table = ImpactTable
