#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    sys_env = os.environ.get("APP_ENV", "local")
    default_settings = f"weather_app.settings.{sys_env}"
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", default_settings)

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
