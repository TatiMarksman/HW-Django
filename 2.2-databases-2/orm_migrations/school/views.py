from django.views.generic import ListView
from django.shortcuts import render
from .models import Student


def students_list(request):
    students = Student.objects.all().order_by('group')

    context = {
        'object_list': students
    }

    template = 'school/students_list.html'

    return render(request, template, context)
