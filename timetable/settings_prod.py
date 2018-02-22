from .settings import *

DEBUG = False

ALLOWED_HOSTS = ['timetable.school91.org.ua']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': secret_data['db_name'],
        'USER': secret_data["db_user"],
        'PASSWORD': secret_data["db_pass"],
        'HOST': secret_data["db_host"],
        'PORT': secret_data["db_port"],
    }
}

INTERNAL_IPS = []

# SSL Settings
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
