from django.test import TestCase
from .models import Usuario
import django


# Create your tests here.
def create_su():
    django.setup()
    admin_email = "admin@email.com"
    admin_user = 'admin'
    admin_senha = 'admin'

    usuarios = Usuario.objects.filter(email=admin_email)
    if not usuarios:
        Usuario.objects.create_superuser(username=admin_user, email=admin_email, password=admin_senha,
                                         is_active=True, is_staff=True)
    usuarios = Usuario.objects.filter(email=admin_email)
    print(usuarios)