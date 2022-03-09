from extras.plugins import PluginMenuItem, PluginMenuButton
from utilities.choices import ButtonColorChoices

menu_items = (
    PluginMenuItem(
        link="plugins:netbox_example_plugin:animals_list",
        link_text="Example Plugin",
        buttons=(
            PluginMenuButton(
                link="plugins:netbox_example_plugin:add_animal",
                title="Add",
                icon_class="mdi mdi-plus-thick",
                color=ButtonColorChoices.GREEN,
            ),
        )
    ),
)
