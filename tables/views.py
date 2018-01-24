import datetime

from django.shortcuts import render

from teachers.models import Teacher
from .models import Timetable, DAY_OF_THE_WEEK

def index(request):
    weekday = DAY_OF_THE_WEEK[datetime.date.today().weekday()][0]
    lessons = Timetable.objects.filter(weekday=weekday).order_by('lesson_number')
    return render(request, 'timetable/index.html', {'lessons': lessons})

def all(request):
    all = Timetable.objects.order_by('weekday', 'lesson_number')
    return render(request, 'timetable/all.html', {'all': all})

def test(request):
    teachers = Teacher.objects.all()
    q = request.GET.get('q', None)
    if q:
        weekday = DAY_OF_THE_WEEK[datetime.date.today().weekday()][0]
        lessons = Timetable.objects.filter(teacher__id=q).filter(weekday=weekday).order_by('lesson_number')
        return render(request, 'timetable/test.html', {'teachers': teachers, 'lessons': lessons})
    return render(request, 'timetable/test.html', {'teachers': teachers})