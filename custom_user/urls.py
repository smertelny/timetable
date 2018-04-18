from django.urls import path

from . import views

app_name = "user"
urlpatterns = [
    path("select_class/", views.select_class, name="select_class" ),
    path("select_teacher/", views.select_teacher, name="select_teacher"),
]
