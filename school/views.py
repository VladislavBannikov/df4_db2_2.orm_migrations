from django.db.models import Prefetch
from django.views.generic import ListView
from django.shortcuts import render

from .models import Student, Teacher


def students_list(request):
    template = 'school/students_list.html'
    students_teachers = Student.objects.order_by('-name').prefetch_related(
        Prefetch('teachers', Teacher.objects.order_by('name'))
    ).all()
    context = {"object_list": students_teachers}


    return render(request, template, context)
