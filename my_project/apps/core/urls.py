from django.urls import re_path

from .views import (
    ping,
    WelcomeView,
    ViteExample,
)

app_name = 'core'
urlpatterns = [
    re_path(r'^ping/?$', ping, name="ping"),
    re_path(r'^/?$', WelcomeView.as_view(), name="welcome"),
    re_path(r'^vite/?$', ViteExample.as_view(), name="vite_example"),
]
