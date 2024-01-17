from django.urls import path, include, re_path

from .views import (
    v1,
)

app_name = 'api.v1'
urlpatterns = [
    path('', v1, name="default"),
    re_path(r'frontend/?', include('frontend.urls')),
]
