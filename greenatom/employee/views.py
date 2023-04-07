from django.core.cache import cache
from django.http import HttpResponse
from django.shortcuts import render, redirect

from position.models import Position

from .models import Employee
from director.models import Director


def index(request):
    print(request.POST)
    return render(request, "employee/j_d_form.html", {'title': 'Создание ДИ'})


def create_j_d(request):
    if request.POST:
        param = request.POST
        if len(param.get('name').split(" ")) > 2 and len(param.get('key-word').split(" ")) != 0:
            new_user = Employee(name=param.get('name').split(" ")[1],
                                    surname=param.get('name').split(" ")[0],
                                    third_name=param.get('name').split(" ")[2::],
                                    depat_name=param.get('depart'),
                                    group_name=param.get('group'),
                                    center_name=param.get('center'),
                                    position=param.get('position'),
                                    specialization=param.get('position'),
                                    job=param.get('key-word'))
            new_user.save()
            Director.objects.filter(id=cache.get("id"))[0].add(new_user)
            return redirect("storage")
        else:
            return_param = param.dict()
            return_param['errors'] = list()
            if len(param.get('name').split(" ")) <= 2:
                return_param['errors'].append("ФИО не заполнено")
            if len(param.get('key-word').split(" ")) == 0:
                return_param['errors'].append("Нет ключевых слов")

            return render(request, "employee/j_d_form.html", return_param)
    else:
        return render(request, "employee/j_d_form.html")


def emp_history(request):

    return HttpResponse("Страница не найдена1")


def emp_jb(request, emp_id):
    return HttpResponse("Страница не найдена1")


def emp_info(request, emp_id):
    return HttpResponse("Страница не найдена1")