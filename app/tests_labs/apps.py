from django.apps import AppConfig


class TestsLabsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tests_labs'

    def ready(self):
        import tests_labs.signals
