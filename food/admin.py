from django.contrib import admin
from .models import Food, Usuario
from django.contrib.auth.admin import UserAdmin

# Register your models here.
admin.site.register(Food)
admin.site.register(Usuario, UserAdmin)