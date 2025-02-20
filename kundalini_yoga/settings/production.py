from .base import *
import dj_database_url

DEBUG = False

ALLOWED_HOSTS = ['kundalini-yoga-app-29d88017307f.herokuapp.com']

DATABASES = {
    'default': dj_database_url.config(conn_max_age=600, ssl_require=True)
}

# Add any production-specific settings here
