from django.db import models
from django.utils.translation import gettext_lazy as _


class Lessons(models.Model):
    name = models.CharField(max_length=30, unique=True, verbose_name=_("name"))
    short_name = models.CharField(max_length=5, unique=True, help_text=_("Can't be longer than 5 characters"), verbose_name=_("short name"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('lesson')
        verbose_name_plural = _('lessons')
        ordering = ("name", )