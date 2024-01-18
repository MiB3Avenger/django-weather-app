from .base import *

# Prod server site id seeing as we are using same DB for stage and prod
SITE_ID = 2

# Set email port to regular port to make sure that emails go out
EMAIL_PORT = 25

DATABASES['default']['HOST'] = env.str("DATABASE_HOST", default="")
DATABASES['default']['NAME'] = env.str("DATABASE_NAME", default="weather_app")
DATABASES['default']['USER'] = env.str("DATABASE_USER", default="")
DATABASES['default']['PASSWORD'] = env.str("DATABASE_PASSWORD", default="")

SERVE_MEDIA_FILES = True
SERVE_STATIC_FILES = True

DJANGO_VITE_STATIC_URL_PREFIX = "vite"

USE_X_FORWARDED_HOST = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')