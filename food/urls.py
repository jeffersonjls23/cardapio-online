from .views import Homepage
from django.urls import path, include


urlpatterns = [
    path('', Homepage.as_view())
]
