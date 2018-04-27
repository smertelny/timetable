from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponseRedirect
from django.views.decorators.http import require_POST
from django.contrib import messages

from custom_user.models import CustomUser
from classes.models import Class
from teachers.models import Teacher
# Create your views here.

@require_POST
def select_class(request):
    if request.method == "POST":
        data = request.POST.get('class_id', None)
        if data:
            klass = get_object_or_404(Class, pk=request.POST.get('class_id', None))
            selected = CustomUser.objects.filter(id=request.user.id)\
                .update(selected_class=klass)
    return HttpResponseRedirect(reverse('timetable:index'))

@require_POST
def select_teacher(request):
    if request.method == "POST":
        if not request.user.is_teacher:
            messages.add_message(request, messages.ERROR, "Not a teacher")
            return HttpResponseRedirect(reverse("timetable:index"))
        data = request.POST.get("teacher_id", None)
        if data:
            teacher = get_object_or_404(Teacher, pk=request.POST.get("teacher_id", None))
            selected = CustomUser.objects.filter(id=request.user.id)\
                .update(selected_teacher=teacher)
        return HttpResponseRedirect(reverse("timetable:index"))
