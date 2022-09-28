from django.apps import AppConfig


class UserloginConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'userLogin'


    def ready(self):
        from .import views
        views.start()