from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponseRedirect

from custom_user.models import CustomUser
from classes.models import Class
# Create your views here.

def select_class(request):
    if request.method == "POST":
        data = request.POST.get('class_id', None)
        if data:
            klass = get_object_or_404(Class, pk=request.POST.get('class_id', None))
            selected = CustomUser.objects.filter(id=request.user.id)\
                .update(selected_class=klass)
            return HttpResponseRedirect(reverse('timetable:index'))
