from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import reverse
from django.utils import translation
from django.conf import settings
from django.utils import translation
from django.contrib import messages

from jinja2 import Environment


def environment(**options):
    env = Environment(extensions=['jinja2.ext.i18n'], **options)
    env.install_gettext_translations(translation)
    env.globals.update({
        'static': staticfiles_storage.url,
        'url': reverse,
        'get_current_language': translation.get_language,
        'avaliable_languages': settings.LANGUAGES,
        'messages': messages.get_messages,
    })
    return env
