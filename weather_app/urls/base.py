from django.urls import include, re_path, path
from django.views.generic import RedirectView
from django.conf import settings
from django.contrib import admin


admin.autodiscover()
admin.site.site_header = 'Project Dashboard'
admin.site.index_title = 'Welcome to Project Dashboard'

urlpatterns = [
    # List all admin paths
    path('admin', RedirectView.as_view(url='admin/', permanent=False)),
    path('admin/', admin.site.urls),
    
    path('api', RedirectView.as_view(url='/api/v1/', permanent=False)),
    path('api/', RedirectView.as_view(url='/api/v1/', permanent=False)),

    # List all api paths
    re_path(r'api/v1/?', include('api.v1.urls')),
]

if getattr(settings, "DEBUG", False):
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
