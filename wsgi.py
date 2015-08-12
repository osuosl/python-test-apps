"""
WSGI config for test_django project.

It exposes the WSGI callable as a module-level variable named ``app``. This
file has been moved and changed to test the python-webapp cookbook.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tutorial_a.settings")


from django.core.wsgi import get_wsgi_application
app = get_wsgi_application()
