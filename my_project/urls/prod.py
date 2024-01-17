from django.urls import re_path, include
from django.conf import settings
from django.conf.urls.static import static


app_prefix = getattr(settings, 'APP_PREFIX', "")
if app_prefix:
    if app_prefix.startswith("/"):
        app_prefix = app_prefix[1:]

    if app_prefix and app_prefix.endswith("/") is False:
        app_prefix += "/"

urlpatterns = [
    re_path(app_prefix, include(settings.APP_NAME + '.urls.base')),
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


urlpatterns += [
    # Else just open vue frontend
    re_path(r'.*', include('core.urls')),
]