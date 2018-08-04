"""
WSGI config for django_practice project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_practice.settings")

sys.path.append('/home/ubuntu/projects/django_practice')
sys.path.append('/home/ubuntu/projects/django_practice/django_practice')

application = get_wsgi_application()
