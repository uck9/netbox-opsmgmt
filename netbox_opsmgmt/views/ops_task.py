from netbox.views.generic import (ObjectListView, ObjectEditView, ObjectDeleteView, ObjectView, BulkEditView,
                                  BulkDeleteView)

# from netbox_opsmgmt.forms.model_forms import TaskForm
from netbox_opsmgmt.models import OpsTask
from netbox_opsmgmt.tables import OpsTaskTable
from utilities.views import register_model_view

__all__ = (
    'OpsTaskListView',
    'OpsTaskView',
    'OpsTaskEditView',
    'OpsTaskBulkEditView',
    'OpsTaskDeleteView',
    'OpsTaskBulkDeleteView',
)

@register_model_view(OpsTask, name='list')
class OpsTaskListView(ObjectListView):
    queryset = OpsTask.objects.all()
    table = OpsTaskTable
    #filterset = OpsTaskFilterSet
    #filterset_form = OpsTaskFilterForm


@register_model_view(OpsTask)
class OpsTaskView(ObjectView):
    queryset = OpsTask.objects.all()


@register_model_view(OpsTask, 'edit')
class OpsTaskEditView(ObjectEditView):
    template_name = 'netbox_opsmgmt/OpsTask_edit.html'
    queryset = OpsTask.objects.all()
    #form = OpsTaskForm


@register_model_view(OpsTask, 'bulk_edit')
class OpsTaskBulkEditView(BulkEditView):
    queryset = OpsTask.objects.all()
    #filterset = OpsTaskFilterSet
    table = OpsTaskTable
    #form = OpsTaskBulkEditForm


@register_model_view(OpsTask, 'delete')
class OpsTaskDeleteView(ObjectDeleteView):
    queryset = OpsTask.objects.all()


@register_model_view(OpsTask, 'bulk_delete')
class OpsTaskBulkDeleteView(BulkDeleteView):
    queryset = OpsTask.objects.all()
    #filterset = OpsTaskFilterSet
    table = OpsTaskTable
