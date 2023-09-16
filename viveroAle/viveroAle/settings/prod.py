import os
from .base import *

DEBUG = False

ALLOWED_HOSTS = ['ViveroDonPedro.pythonanywhere.com']

# Data BAse
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': get_secret ("DB_PROD_NAME"),
        'USER': get_secret ("DB_PROD_USER"),
        'PASSWORD': get_secret ("DB_PROD_PASSWORD"),
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# Direction off JS - IMG - CSS
STATIC_URL = '/static/'
STATICFILES_DIRS = ( os.path.join(BASE_DIR, 'static'), )
STATIC_ROOT = BASE_DIR.child('staticfiles')


# Direction off MEDIA
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR.child('media')

