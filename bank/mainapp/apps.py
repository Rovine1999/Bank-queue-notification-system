from django.apps import AppConfig

#Configuring the app for the project
class AssetsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mainapp'

    def ready(self):
        import mainapp.customsignals