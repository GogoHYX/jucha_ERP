"""
WSGI config for jucha_ERP project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os
import sys
from os.path import dirname, abspath
from django.core.wsgi import get_wsgi_application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'jucha_ERP.settings')
PROJECT_DIR = dirname(dirname(abspath(__file__)))
sys.path.insert(0, PROJECT_DIR)


# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "travel_record.settings")
os.environ["DJANGO_SETTINGS_MODULE"] = "jucha_ERP.settings"
print(sys.path)
print(sys.version)


application = get_wsgi_application()
