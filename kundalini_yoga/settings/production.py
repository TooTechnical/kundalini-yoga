from .base import *
import dj_database_url

# Security settings
DEBUG = False

ALLOWED_HOSTS = [
    'kundalini-yoga-app-29d88017307f.herokuapp.com',
    '.herokuapp.com'  # Wildcard for all Heroku subdomains
]
# MySQL Configuration
DATABASES = {
    'default': dj_database_url.config(
        env='JAWSDB_URL',
        conn_max_age=600,
        engine='django.db.backends.mysql'
    )
}

DATABASES['default']['OPTIONS'] = {'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"}

# WhiteNoise configuration for static files
MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
