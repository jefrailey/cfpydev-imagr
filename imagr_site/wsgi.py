"""
WSGI config for imagr_site project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "imagr_site.settings")
os.environ.setdefault('DJANGO_CONFIGURATION', 'Dev')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
