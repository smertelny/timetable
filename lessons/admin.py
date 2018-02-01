from django.contrib import admin

from .models import Lessons


class LessonsAdmin(admin.ModelAdmin):
    list_display = ('name', 'short_name')


admin.site.register(Lessons, LessonsAdmin)
