from .base import *

DEBUG = False
ALLOWED_HOSTS = ['your-domain.com']  # Replace with your actual domain

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '',
    }
}

# Add any production-specific settings here
