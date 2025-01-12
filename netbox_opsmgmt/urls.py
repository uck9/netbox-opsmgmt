from django.urls import path

from netbox.views.generic import ObjectChangeLogView
from . import views
from netbox_opsmgmt.models import Impact, OpsTask

app_name = 'netbox_opsmgmt'
urlpatterns = [
    path('impact/', views.ImpactListView.as_view(), name='impact_list'),
    path('impact/add/', views.ImpactEditView.as_view(), name='impact_add'),
    path('impact/<int:pk>/', views.ImpactView.as_view(), name='impact'),
    path('impact/<int:pk>/edit/', views.ImpactEditView.as_view(), name='impact_edit'),
    path('impact/<int:pk>/delete/', views.ImpactDeleteView.as_view(), name='impact_delete'),
    path('impact/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='impact_changelog', kwargs={'model': Impact}),

    path('ops-task/', views.OpsTaskListView.as_view(), name='ops-task_list'),
    path('ops-task/add/', views.OpsTaskEditView.as_view(), name='ops-task_add'),
    path('ops-task/<int:pk>/', views.OpsTaskView.as_view(), name='ops-task'),
    path('ops-task/<int:pk>/edit/', views.OpsTaskEditView.as_view(), name='ops-task_edit'),
    path('ops-task/<int:pk>/delete/', views.OpsTaskDeleteView.as_view(), name='ops-task_delete'),
    path('ops-task/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='ops-task_changelog', kwargs={'model': OpsTask}),
]
