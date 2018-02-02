import datetime

from django.shortcuts import render, get_object_or_404, reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

from teachers.models import Teacher
from .models import Timetable, DAY_OF_THE_WEEK, SelectedTeacher

def index(request):
    weekday = datetime.date.today().weekday()
    try:
        selected_teacher = request.user.selectedteacher.selected
    except AttributeError:
        lessons = Timetable.objects.select_related('lesson').\
        select_related('class_name').filter(weekday=weekday).order_by('lesson_number')
        return render(request, 'timetable/all.html', {'all': lessons})
    lessons = Timetable.objects.select_related('lesson').select_related('class_name')\
    .filter(weekday=weekday).filter(teacher=selected_teacher).order_by('lesson_number')
    return render(request, 'timetable/timetable.html', {'lessons': lessons})

def week_timetable(request):
    lessons = Timetable.objects.select_related('lesson').select_related('class_name')\
    .order_by('weekday', 'lesson_number')
    return render(request, 'timetable/timetable.html', {'lessons': lessons})

def test(request):
    teachers = Teacher.objects.all()
    q = request.GET.get('q', None)
    if q:
        lessons = Timetable.objects.select_related('lesson').select_related('class_name')\
        .filter(teacher__id=q).order_by('weekday', 'lesson_number')
        return render(request, 'timetable/test.html', {'teachers': teachers, 'lessons': lessons})
    return render(request, 'timetable/test.html', {'teachers': teachers})

@login_required(login_url='/')
def select_teacher(request):
    teachers = Teacher.objects.all()
    selected = None
    if request.method == 'POST':
        data = request.POST.get('teacher_id', None)
        if data:
            teacher = get_object_or_404(Teacher, pk=request.POST.get('teacher_id', None))
            user = get_object_or_404(SelectedTeacher, user_id=request.user.id)
            try:
                selected = SelectedTeacher.objects.filter(user=request.user)\
                .update(selected=teacher)
            except SelectedTeacher.DoesNotExist:
                SelectedTeacher.objects.create(user=request.user, selected=teacher)
            return HttpResponseRedirect(reverse('timetable:index'))
    return render(request, 'timetable/select.html', {'teachers': teachers, 'selected':selected})
