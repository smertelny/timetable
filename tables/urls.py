from django.urls import path

from . import views

app_name = 'timetable'
urlpatterns = [
    path('', views.index, name='index'),
    path('week', views.week_timetable, name='week'),
    path('test', views.test, name='test'),
    path('selected', views.select_teacher, name='selected'),
]