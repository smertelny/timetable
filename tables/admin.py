from django.contrib import admin

from .models import Timetable


class TimetableAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'lesson_number', 'weekday', 'teacher')
    list_filter = ('teacher', 'lesson')
    ordering = ('weekday', 'lesson_number')
admin.site.register(Timetable, TimetableAdmin)
