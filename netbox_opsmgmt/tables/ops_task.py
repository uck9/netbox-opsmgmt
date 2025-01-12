import django_tables2 as tables

from django.utils.translation import gettext as _
from netbox.tables import NetBoxTable, ChoiceFieldColumn, columns

from netbox_opsmgmt.models import OpsTask


__all__ = (
    'OpsTaskTable',
)


class OpsTaskTable(NetBoxTable):
    name = tables.Column(
        linkify=True,
        accessor='name',
        orderable=False,
    )
    assigned_object = tables.Column(
        linkify=True,
        verbose_name=_('Object'),
        orderable=False,
    )

    bus_impact_details = columns.MarkdownColumn(
        verbose_name=_('Business Impact Details'),
    )

    impact_rating = columns.ChoiceFieldColumn()

    class Meta(NetBoxTable.Meta):
        model = OpsTask
        fields = ('pk', 'name', 'assigned_object', 'tags')

        default_columns = (
            'pk', 'name', 'assigned_object',
        )
