"""
WSGI config for daily_logs project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

from conf.setup_env import setup_env
setup_env()
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "conf.settings.local")

application = get_wsgi_application()

from whitenoise.django import DjangoWhiteNoise
application = DjangoWhiteNoise(application)