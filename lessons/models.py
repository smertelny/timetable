from django.db import models


class Lessons(models.Model):
    name = models.CharField(max_length=30, unique=True)
    short_name = models.CharField(max_length=5, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'lesson'
        verbose_name_plural = 'lessons'
        