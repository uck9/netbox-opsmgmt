from netbox.plugins import PluginMenu, PluginMenuButton, PluginMenuItem

impact_buttons = [
    PluginMenuButton(
        link="plugins:netbox_opsmgmt:impact_add",
        title="Add",
        icon_class="mdi mdi-plus-thick",
    )
]

impact_items = (
    PluginMenuItem(
        link="plugins:netbox_opsmgmt:impact_list",
        link_text="Impact Analyses",
        buttons=impact_buttons,
    ),
)

ops_task_buttons = [
    PluginMenuButton(
        link="plugins:netbox_opsmgmt:impact_add",
        title="Add",
        icon_class="mdi mdi-plus-thick",
    )
]

ops_task_items = (
    PluginMenuItem(
        link="plugins:netbox_opsmgmt:impact_list",
        link_text="Ops Tasks",
        buttons=ops_task_buttons,
    ),
)

menu = PluginMenu(
    label=f'Operations Management',
    groups=(
        ('Impacts', impact_items),
        #('Ops Tasks', ops_task_items),
    ),
    icon_class='mdi mdi-wrench-outline'
)