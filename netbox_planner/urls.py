from django.urls import path

from netbox.views.generic import ObjectChangeLogView
from . import views
from netbox_planner.models import Impact, Task

app_name = 'netbox_planner'
urlpatterns = [
    path('impact/', views.ImpactListView.as_view(), name='impact_list'),
    path('impact/add/', views.ImpactEditView.as_view(), name='impact_add'),
    path('impact/<int:pk>/', views.ImpactView.as_view(), name='impact'),
    path('impact/<int:pk>/edit/', views.ImpactEditView.as_view(), name='impact_edit'),
    path('impact/<int:pk>/delete/', views.ImpactDeleteView.as_view(), name='impact_delete'),
    path('impact/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='impact_changelog', kwargs={'model': Impact}),

    path('ops-task/', views.TaskListView.as_view(), name='task_list'),
    path('ops-task/add/', views.TaskEditView.as_view(), name='task_add'),
    path('ops-task/<int:pk>/', views.TaskView.as_view(), name='task'),
    path('ops-task/<int:pk>/edit/', views.TaskEditView.as_view(), name='task_edit'),
    path('ops-task/<int:pk>/delete/', views.TaskDeleteView.as_view(), name='task_delete'),
    path('ops-task/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='task_changelog', kwargs={'model': Task}),
]
