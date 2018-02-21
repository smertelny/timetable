from modeltranslation.translator import register, TranslationOptions

from .models import Class


@register(Class)
class ClassTranslation(TranslationOptions):
    fields = ("index", )
