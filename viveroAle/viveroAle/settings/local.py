import os
from .base import *

DEBUG = True

ALLOWED_HOSTS = ['*']

# Data BAse
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': get_secret ("DB_NAME"),
        'USER': get_secret ("DB_USER"),
        'PASSWORD': get_secret ("DB_PASSWORD"),
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# Direction off JS - IMG - CSS
STATIC_URL = '/static/'
STATICFILES_DIRS = ( os.path.join(BASE_DIR, 'static'), )


# Direction off MEDIA
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR.child('media')

