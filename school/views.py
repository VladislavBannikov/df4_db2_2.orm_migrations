from django.views.generic import ListView
from django.shortcuts import render

from .models import Student


def students_list(request):
    template = 'school/students_list.html'
    context = {"object_list": Student.objects.prefetch_related("teachers").order_by("name").all()}

    #:TODO Как сделать второй уровень сортировки по именам учителей?

    return render(request, template, context)
