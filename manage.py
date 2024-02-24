#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
from food.models import Usuario
import sys


def main():
    """Run administrative tasks."""
    user = os.getenv("USER_ADMIN")
    email = os.getenv("EMAIL_ADMIN")
    senha = os.getenv("SENHA_ADMIN")

    usuarios = Usuario.objects.filter(email=email)
    if not usuarios:
        Usuario.objects.create_superuser(username=user, email=email, password=senha,
                                      is_active=True, is_staff=True)
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cardapio.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
