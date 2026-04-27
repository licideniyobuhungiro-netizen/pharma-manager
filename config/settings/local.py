from .base import *

# Pour l'instant on utilise SQLite pour que tu puisses tester vite, 
# mais l'entreprise demande PostgreSQL à la fin.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
# Dans INSTALLED_APPS, ajoute :
# 'rest_framework',
# 'drf_spectacular',

REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}

SPECTACULAR_SETTINGS = {
    'TITLE': 'PharmaManager API',
    'DESCRIPTION': 'API de gestion de pharmacie – Développé avec SMARTHOLOL standards',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
}