from django.db import models
from django.core.validators import MaxValueValidator
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.utils.text import format_lazy

from teachers.models import Teacher
from classes.models import Class
from lessons.models import Lessons

DAY_OF_THE_WEEK = (
    (0, _('Monday')),
    (1, _('Tuesday')),
    (2, _('Wednesday')),
    (3, _('Thursday')),
    (4, _('Friday')),
    (5, _('Saturday')),
    (6, _('Sunday'))
)


class SelectedTeacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, )
    selected = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True, default=None)

    is_teacher = models.BooleanField(default=False)

    def __str__(self):
        return str(format_lazy("{user}: {name}", name=self.user, user=_('User')))


class Timetable(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True)
    weekday = models.IntegerField(choices=DAY_OF_THE_WEEK)
    lesson_number = models.PositiveSmallIntegerField(
        validators=(MaxValueValidator(8, message="There can't be more than 8 lessons"),)
    )
    lesson = models.ForeignKey(Lessons, on_delete=models.SET_NULL, blank=True, null=True)
    class_name = models.ForeignKey(Class, on_delete=models.SET_NULL, blank=True, null=True)
    classroom = models.IntegerField()

    def __str__(self):
        return str(format_lazy("#{num} - {weekday}", num=self.lesson_number, weekday=self.get_weekday_display()))

    class Meta:
        verbose_name = _('timetable')
        verbose_name_plural = _('timetables')
        ordering = ('weekday', 'lesson_number', 'teacher')
        unique_together = (('teacher', 'weekday', 'lesson_number'),)
