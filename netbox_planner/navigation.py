from netbox.plugins import PluginMenu, PluginMenuButton, PluginMenuItem

impact_buttons = [
    PluginMenuButton(
        link="plugins:netbox_planner:impact_add",
        title="Add",
        icon_class="mdi mdi-plus-thick",
    )
]

impact_items = (
    PluginMenuItem(
        link="plugins:netbox_planner:impact_list",
        link_text="Impact Analyses",
        buttons=impact_buttons,
    ),
)

menu = PluginMenu(
    label=f'Operations Planning',
    groups=(
        ('Impacts', impact_items),
    ),
    icon_class='mdi mdi-wrench-outline'
)