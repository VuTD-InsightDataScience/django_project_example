from django.apps import AppConfig


class ExampleConfig(AppConfig):
    name = 'example_app'

    def ready(self):
        import example_app.signals # noqa
