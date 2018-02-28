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
    if request.user.is_anonymous:
        lessons = Timetable._get_today()\
        .order_by("class_name")
        return render(
            request,
            "timetable/students_week.html",
            {"lessons": lessons})
    elif request.user.is_teacher:
        selected_teacher = request.user.selected_teacher
        lessons = Timetable._get_today()\
            .filter(teacher=selected_teacher)\
            .order_by("lesson_number")
    else:
        selected_class = request.user.selected_class
        lessons = Timetable._get_today()\
            .filter(class_name=selected_class)\
            .order_by("lesson_number")
        return render(
            request,
            "timetable/students_week.html",
            {"lessons": lessons})
    return render(request, 'timetable/timetable.html', {'lessons': lessons})
    # weekday = datetime.date.today().weekday()
    # try:
    #     selected_teacher = request.user.selected_teacher
    # except AttributeError:
    #     lessons = Timetable.objects.select_related('lesson')\
    #         .select_related('class_name')\
    #         .filter(weekday=weekday)\
    #         .order_by('lesson_number')
    #     return render(request, 'timetable/timetable.html', {'lessons': lessons})
    # lessons = Timetable.objects.select_related('lesson')\
    #     .select_related('class_name')\
    #     .filter(weekday=weekday)\
    #     .filter(teacher=selected_teacher)\
    #     .order_by('lesson_number')
    # return render(request, 'timetable/timetable.html', {'lessons': lessons})

def week_timetable(request):
    lessons = Timetable.objects.select_related('lesson').select_related('class_name')\
    .order_by('weekday', 'lesson_number')
    return render(request, 'timetable/timetable.html', {'lessons': lessons})

def today_students(request):
    weekday = datetime.date.today().weekday()
    lessons = Timetable.objects.select_related('lesson').select_related('class_name')\
    .filter(weekday=weekday).order_by("class_name")
    weekday = DAY_OF_THE_WEEK[weekday][1]
    return render(request, "timetable/students_week.html", {"lessons": lessons, "weekday": weekday})

def test(request):
    teachers = Teacher.objects.all()
    q = request.GET.get('q', None)
    if q:
        lessons = Timetable.objects.select_related('lesson').select_related('class_name')\
        .filter(teacher__id=q).order_by('weekday', 'lesson_number')
        return render(request, 'timetable/test.html', {'teachers': teachers, 'lessons': lessons})
    return render(request, 'timetable/test.html', {'teachers': teachers})

@login_required(login_url='/')
def user_settings(request):
    teachers = Teacher.objects.all()
    classes = Class.objects.all()
    selected = None
    if request.method == 'POST':
        data = request.POST.get('teacher_id', None)
        if data:
            teacher = get_object_or_404(Teacher, pk=request.POST.get('teacher_id', None))
            selected = CustomUser.objects.filter(id=request.user.id)\
                .update(selected_teacher=teacher)
            return HttpResponseRedirect(reverse('timetable:index'))
    return render(request,'timetable/user_settings.html',{'teachers': teachers,'selected':selected,'classes': classes})
