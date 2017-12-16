"""
WSGI config for congreso project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""
"""
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "congreso.settings")

application = get_wsgi_application()
"""

import os
from dotenv import load_dotenv
from django.core.wsgi import get_wsgi_application

try:
    dotenv_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), '.env')
    load_dotenv(dotenv_path)
except:
    pass


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "congreso.settings")

application = get_wsgi_application()
