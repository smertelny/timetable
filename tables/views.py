import datetime

from django.shortcuts import render, get_object_or_404, reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

from custom_user.models import CustomUser
from teachers.models import Teacher
from classes.models import Class
from .models import Timetable, DAY_OF_THE_WEEK

def index(request):
    weekday = datetime.date.today().weekday()
    if getattr(request.user, "is_teacher", None):
        selected_teacher = request.user.selected_teacher
        lessons = Timetable._get_today()\
            .filter(teacher=selected_teacher)\
            .order_by("lesson_number")
        return render(request, 'timetable/timetable.html', {'lessons': lessons})

    elif getattr(request.user, "is_student", None):
        selected_class = request.user.selected_class
        if selected_class:
            lessons = Timetable._get_today()\
                .filter(class_name=selected_class)\
                .order_by("lesson_number")
        else:
            lessons = Timetable._get_today()\
                .order_by("class_name", "lesson_number")
       
    else:
        lessons = Timetable._get_today()\
            .order_by("class_name", "lesson_number")
    return render(
        request,
        "timetable/students_week.html",
        {"lessons": lessons})


def week_timetable(request):
    lessons = Timetable.objects.select_related('lesson')\
        .select_related("class_name")\
        .filter(teacher=request.user.selected_teacher)\
        .order_by("weekday", "lesson_number")
    return render(request, "timetable/timetable.html", {"lessons": lessons})


def today_students(request):
    weekday = datetime.date.today().weekday()
    lessons = Timetable.objects\
        .select_related("lesson").select_related("class_name")\
        .filter(weekday=weekday).order_by("class_name")
    weekday = DAY_OF_THE_WEEK[weekday][1]
    return render(request, "timetable/students_week.html", {"lessons": lessons, "weekday": weekday})


def test(request):
    teachers = Teacher.objects.all()
    q = request.GET.get("q", None)
    if q:
        lessons = Timetable.objects.select_related("lesson").select_related("class_name")\
        .filter(teacher__id=q).order_by("weekday", "lesson_number")
        return render(request, "timetable/test.html", {"teachers": teachers, "lessons": lessons})
    return render(request, "timetable/test.html", {"teachers": teachers})


@login_required(login_url="/")
def user_settings(request):
    teachers = Teacher.objects.all()
    classes = Class.objects.all()
    return render(request,"timetable/user_settings.html",{"teachers": teachers, "classes": classes})
