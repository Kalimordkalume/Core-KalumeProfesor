"""
ASGI config for project project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

# if os.environ.get("DJANGO_SETTINGS_MODULE") == "backend.project.settings":
#     settings_module = "backend.project.settings.settings_prod"
# else:
#     settings_module = "backend.project.settings.settings_dev"

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.project.settings")

application = get_asgi_application()
