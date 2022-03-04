from extras.plugins import PluginConfig


class ExamplePluginConfig(PluginConfig):
    name = "netbox_example_plugin"
    verbose_name = "NetBox Example Plugin"
    description = "Basic plugin example"
    version = "0.1"
    author = "Nastassia Yarotskas"
    author_email = ""
    base_url = "example-plugin"
    min_version = "2.9"
    required_settings = []
    default_settings = {}


config = ExamplePluginConfig
