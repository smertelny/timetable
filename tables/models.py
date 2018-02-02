from django.db import models
from django.core.validators import MaxValueValidator
from django.contrib.auth.models import User

from teachers.models import Teacher
from classes.models import Class
from lessons.models import Lessons

DAY_OF_THE_WEEK = (
    (0, 'Monday'),
    (1, 'Tuesday'),
    (2, 'Wednesday'),
    (3, 'Thursday'),
    (4, 'Friday'),
    (5, 'Saturday'),
    (6, 'Sunday')
)


class SelectedTeacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, )
    selected = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True, default=None)

    is_teacher = models.BooleanField(default=False)

    def __str__(self):
        return "User: {}".format(self.user)


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
        return "#{} - {}".format(self.lesson_number, self.get_weekday_display())

    class Meta:
        verbose_name = 'timetable'
        verbose_name_plural = 'timetables'
        ordering = ('weekday', 'lesson_number', 'teacher')
        unique_together = (('teacher', 'weekday', 'lesson_number'),)
