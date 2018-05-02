#!/usr/bin/env python
import os
import sys


if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "virtual_library.settings")
    # import django.contrib.admin.apps
    # import django.contrib.auth
    # import django.contrib.contenttypes
    # import django.contrib.sessions
    # import django.contrib.messages
    # import django.contrib.staticfiles
    # import django.contrib.auth.apps
    # import django.contrib.contenttypes.apps
    # import django.contrib.sessions.apps
    # import django.contrib.messages.apps
    # import django.contrib.staticfiles.apps
    # import django
    # import books
    # import main_site
    # import online_shop
    # import virtual_library
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
