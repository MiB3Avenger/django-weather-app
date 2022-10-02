from django.urls import include, path
from django.conf import settings
from django.contrib import admin


admin.autodiscover()

urlpatterns = [
    path(r'^admin/', admin.site.urls),
    path(r'', include('core.urls')),
]

if getattr(settings, "DEBUG", False):
    import debug_toolbar
    urlpatterns += [
        path(r'^__debug__/', include(debug_toolbar.urls)),
    ]
