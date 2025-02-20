from .base import *
import dj_database_url

# Security settings
DEBUG = False
ALLOWED_HOSTS = ['kundalini-yoga-app-29d88017307f.herokuapp.com']

# Database configuration
DATABASES = {
    'default': dj_database_url.config(conn_max_age=600, ssl_require=True)
}

# WhiteNoise configuration for static files
MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
