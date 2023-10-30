from django.apps import AppConfig


class AssetsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mainapp'

    def ready(self):
        import mainapp.customsignals