from modeltranslation.translator import register, TranslationOptions

from .models import Teacher


@register(Teacher)
class TeacherTranslation(TranslationOptions):
    fields = ("first_name", "second_name")
