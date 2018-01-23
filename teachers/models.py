from django.db import models


class Teacher(models.Model):
    first_name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=80)

    is_class_teacher = models.BooleanField(default=False)
    default_classroom = models.SmallIntegerField()

    def __str__(self):
        return "{} {}".format(self.first_name, self.second_name)
