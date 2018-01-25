from django.urls import path

from . import views

app_name = 'timetable'
urlpatterns = [
    path('', views.index, name='index'),
    path('all', views.all, name='all'),
    path('test', views.test, name='test'),
    path('selected', views.select_teacher, name='selected'),
]