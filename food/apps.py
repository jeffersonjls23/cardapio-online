import os
from .models import User
from django.apps import AppConfig


class FoodConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'food'

    def ready(self):
        email = os.getenv("EMAIL_ADMIN")
        password = os.getenv("SENHA_ADMIN")

        user = User.objects.filter(email=email)
        if not user:
            User.objects.create_superuser(username='admin', email=email, password=password,
                                          is_active=True, is_staff=True)
