from modeltranslation.translator import register, TranslationOptions

from .models import Lessons


@register(Lessons)
class LessonsTranslation(TranslationOptions):
    fields = ("name", "short_name")
