"""
WSGI config for ecommerce project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application

# Check if we're running on Vercel
if 'VERCEL' in os.environ:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce.settings_prod')
else:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce.settings')

# Get the WSGI application
application = get_wsgi_application()

# Vercel needs the variable to be named 'app'
app = application
