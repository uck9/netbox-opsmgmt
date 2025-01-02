from importlib.metadata import metadata

from netbox.plugins import PluginConfig

metadata = metadata('netbox_planner')

__author__ = """Nathan Reeves"""
__email__ = ""
__version__ = "0.1.0"


class PlannerConfig(PluginConfig):
    name = "netbox_planner"
    verbose_name = "NetBox Planner Plugin"
    description = "NetBox Planned Plugin"
    version = "0.1.0"
    base_url = "planner"

    def ready(self):

        super().ready()

        from django.contrib.contenttypes.fields import GenericRelation
        from dcim.models import Device
        from circuits.models import Circuit
        from netbox_planner.models import Impact

        # Add Generic Relations to appropriate models
        GenericRelation(
            to=Impact,
            content_type_field='assigned_object_type',
            object_id_field='assigned_object_id',
            related_name='circuit',
            related_query_name='circuit'
        ).contribute_to_class(Circuit, 'impact_assessment')
        GenericRelation(
            to=Impact,
            content_type_field='assigned_object_type',
            object_id_field='assigned_object_id',
            related_name='device',
            related_query_name='device'
        ).contribute_to_class(Device, 'impact_assessment')


config = PlannerConfig
