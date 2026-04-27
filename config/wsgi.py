import os
from django.core.wsgi import get_wsgi_application

# Remplace 'config.settings' par le chemin vers tes réglages si nécessaire
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

application = get_wsgi_application()