from django.urls import re_path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    re_path(r'', include('my_project.urls.base')),
]

if getattr(settings, "SERVE_MEDIA_FILES", False):
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )

if getattr(settings, "SERVE_STATIC_FILES", False):
    urlpatterns += static(
        settings.STATIC_URL,
        document_root=settings.STATIC_ROOT
    )
