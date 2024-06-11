from django.http import HttpResponse
from django.shortcuts import render, reverse
import os
import datetime


def home_view(request):
    template_name = 'app/home.html'
    # функция reverse для генерации URL-адресов
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }

    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    # указание текущего времени
    current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    msg = f'Текущее время: {current_time}'
    return HttpResponse(msg)


def workdir_view(request):
    # получаем списка файлов в рабочей директории
    files = os.listdir('.')
    files_list = '<br>'.join(files)
    msg = f'Содержимое рабочей директории:<br>{files_list}'
    return HttpResponse(msg)
