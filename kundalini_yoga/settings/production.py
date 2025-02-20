from .base import *
import dj_database_url

# Security settings
DEBUG = False
ALLOWED_HOSTS = [
    'kundalini-yoga-app-29d88017307f.herokuapp.com',
    '.herokuapp.com'  # Wildcard for all Heroku subdomains
]

# JawsDB MySQL Configuration
DATABASES = {
    'default': dj_database_url.config(
        env='JAWSDB_URL',  # Explicitly use JAWSDB_URL environment variable
        conn_max_age=600,
        conn_health_checks=True
    )
}

# MySQL Strict Mode Configuration
DATABASES['default']['OPTIONS'] = {
    'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
    'charset': 'utf8mb4'  # Recommended for full Unicode support
}
