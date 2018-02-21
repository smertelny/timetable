from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.translation import gettext_lazy as _


class Class(models.Model):
    form = models.PositiveSmallIntegerField(validators=(
        MaxValueValidator(11, _("There can't be more than eleven form")),
        MinValueValidator(1, _("There can't be less then first form"))
    ), verbose_name=_("form"))
    index = models.CharField(max_length=1, verbose_name=_("index"))

    def __str__(self):
        return "{}-{}".format(self.form, self.index)

    class Meta:
        verbose_name = _("class")
        verbose_name_plural = _("classes")
        ordering = ('form', 'index')
        unique_together = (('form', 'index'),)
