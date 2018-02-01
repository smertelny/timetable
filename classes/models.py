from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Class(models.Model):
    form = models.PositiveSmallIntegerField(validators=(
        MaxValueValidator(11, "There can't be more than eleven form"),
        MinValueValidator(1, "There can't be less then first form")
    ))
    index = models.CharField(max_length=1)

    def __str__(self):
        return "{}-{}".format(self.form, self.index)

    class Meta:
        verbose_name = "class"
        verbose_name_plural = "classes"
        ordering = ('form', 'index')
        unique_together = (('form', 'index'),)
