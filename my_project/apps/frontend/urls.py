from django.urls import path

from .views import (
    frontend
)

app_name = 'frontend'
urlpatterns = [
    path('', frontend, name="default"),
]