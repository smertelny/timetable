from django.db import models
from django.utils.translation import gettext_lazy as _


class Teacher(models.Model):
    first_name = models.CharField(max_length=50, verbose_name=_("first name"))
    second_name = models.CharField(max_length=80, verbose_name=_("second name"))

    is_class_teacher = models.BooleanField(default=False, verbose_name=_("is class teacher?"))
    default_classroom = models.SmallIntegerField(verbose_name=_("default classroom"))

    def __str__(self):
        return "{} {}".format(self.first_name, self.second_name)

    class Meta:
        verbose_name = _("teacher")
        verbose_name_plural = _("teachers")
