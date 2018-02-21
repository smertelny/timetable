from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import reverse
from django.utils import translation
from django.conf import settings

from jinja2 import Environment


def environment(**options):
    env = Environment(extensions=['jinja2.ext.i18n'], **options)
    env.globals.update({
        'static': staticfiles_storage.url,
        'url': reverse,
        'range': range,
        'get_current_language': translation.get_language,
        'avaliable_languages': settings.LANGUAGES,
    })
    return env
