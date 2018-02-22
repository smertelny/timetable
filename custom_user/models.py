from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.utils.text import format_lazy

from teachers.models import Teacher
from classes.models import Class


class CustomUser(AbstractUser):
    selected_teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True, default=None, verbose_name=_("selected teacher"))
    selected_class = models.ForeignKey(Class, on_delete=models.CASCADE, null=True, default=None, verbose_name=_("selected class"))
    is_teacher = models.BooleanField(default=False, verbose_name=_("is teacher?"))

    def __str__(self):
        return str(format_lazy("{user}: {name}", name=self.username, user=_('User')))

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")
