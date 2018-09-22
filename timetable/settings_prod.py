from .settings import *

DEBUG = False

ALLOWED_HOSTS = ['timetable.school91.org.ua']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': SECRET_DATA['db_name'],
        'USER': SECRET_DATA["db_user"],
        'PASSWORD': SECRET_DATA["db_pass"],
        'HOST': SECRET_DATA["db_host"],
        'PORT': SECRET_DATA["db_port"],
    }
}

INTERNAL_IPS = []

# SSL Settings
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# HTML minification
HTML_MINIFY = True

# Raven configuration
RAVEN_CONFIG = {
    'dsn': SECRET_DATA["sentry_dsn"],
    'release': raven.fetch_git_sha(os.path.abspath(BASE_DIR)),
}

# Making static files to be generated with MD5 hash for better caching
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'
