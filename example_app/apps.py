from django.apps import AppConfig


class ExampleConfig(AppConfig):
    name = 'example_app'

    def ready(self):
        import signals # noqa
