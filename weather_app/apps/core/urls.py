from django.urls import re_path, path

from .views import (
    ping,
    Index,
)

app_name = 'core'
urlpatterns = [
    re_path(r'^ping/?$', ping, name="ping"),
    path('', Index.as_view(), name="index"),
]
