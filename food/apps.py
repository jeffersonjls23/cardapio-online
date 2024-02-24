from django.apps import AppConfig
from django.contrib.auth.models import AbstractUser
import os


class FoodConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'food'

    def ready(self):
        user = os.getenv("USER_ADMIN")
        email = os.getenv("EMAIL_ADMIN")
        senha = os.getenv("SENHA_ADMIN")

        usuarios = AbstractUser.objects.filter(email=email)
        if not usuarios:
            AbstractUser.objects.create_superuser(username=user, email=email, password=senha,
                                                  is_active=True, is_staff=True)
