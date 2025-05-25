from django.apps import AppConfig
from django.db.utils import OperationalError


class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'

    # def ready(self):
    #     from django.contrib.auth import get_user_model
    #     from django.db import ProgrammingError
    #     User = get_user_model()

    #     try: # Create default user if it does not exist yet
    #         if not User.objects.filter(username='admin').exists():
    #             User.objects.create_superuser(
    #                 username='watchdxg',
    #                 password='watchdxg'
    #             )
    #             print("Created default user")
    #     except (OperationalError, ProgrammingError):
    #         # Database might not be ready yet during initial migration
    #         pass