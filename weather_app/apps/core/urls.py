from django.urls import re_path, path

from .views import (
    Ping,
    Index,
)

app_name = 'core'
urlpatterns = [
    path('ping/', Ping.as_view(), name="ping"),
    re_path(r'.*', Index.as_view(), name="index"),
]
