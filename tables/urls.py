from django.urls import path

from . import views

app_name = 'timetable'
urlpatterns = [
    path('', views.index, name='index'),
    path('week', views.week_timetable, name='week'),
    path('test', views.test, name='test'),
    path('settings', views.user_settings, name='user_settings'),
    # path('students', views.today_students, name="students"),
    path('students', views.today_chosen_class, name="today_chosen_class"),
]
