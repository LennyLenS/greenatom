from django.http import HttpResponse
from django.shortcuts import render

from position.models import Position


def index(request):
    print(request.POST)
    return render(request, "employee/j_d_form.html", {'title': 'Создание ДИ'})


def create_j_d(request):
    if request.POST:
        print(request.POST)

    pos_names = list()
    for i in list(Position.objects.all()):
        pos_names.append(i.name)

    #generate_j_d(request.POST)

    return render(request, "employee/j_d_form.html", {'title': 'Создание ДИ', 'pos_names': pos_names})


def emp_history(request):

    return HttpResponse("Страница не найдена1")


def emp_jb(request, emp_id):
    return HttpResponse("Страница не найдена1")


def emp_info(request, emp_id):
    return HttpResponse("Страница не найдена1")