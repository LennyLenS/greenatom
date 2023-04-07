from django.core.cache import cache
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect

from position.models import Position

from .models import Employee
from director.models import Director

from specialization.models import Specialization


def index(request):
    print(request.POST)
    return render(request, "employee/j_d_form.html", {'title': 'Создание ДИ'})


def create_j_d(request):
    print("!!!!!!!", request.POST)
    if cache.get("auth") != "true":
        return redirect("login")
    if cache.get('emp_id'):
        param = request.POST
        if len(param.get('name').split(" ")) > 2 and len(param.get('key_words').split(" ")) != 0:
            new_user = Employee.objects.filter(id=cache.get('emp_id'))[0]
            new_user.name = param.get('name').split(" ")[1]
            new_user.surname = param.get('name').split(" ")[0]
            new_user.third_name = param.get('name').split(" ")[2]
            new_user.depat_name = param.get('depart')
            new_user.group_name = param.get('group')
            new_user.center_name = param.get('center')
            new_user.job = param.get('key_words')

            print(new_user.position.all()[0].name)
            new_user.position.remove(Position.objects.filter(name=new_user.position.all()[0].name)[0].id)
            new_user.specialization.remove(Specialization.objects.filter(name=new_user.specialization.all()[0].name)[0].id)

            new_user.position.add(Position.objects.filter(name=param.get('position'))[0])
            new_user.specialization.add(Specialization.objects.filter(name=param.get('specialization'))[0])

            new_user.save()
            cache.delete('emp_id')
            return redirect("storage")
        else:
            return_param = param.dict()
            return_param['errors'] = list()
            if len(param.get('name').split(" ")) <= 2:
                return_param['errors'].append("ФИО не заполнено")
            if len(param.get('key_words').split(" ")) == 0:
                return_param['errors'].append("Нет ключевых слов")

            pos_names = list()
            for i in list(Position.objects.all()):
                pos_names.append(i.name)
            spec_names = list()
            for i in list(Specialization.objects.all()):
                spec_names.append(i.name)
            return_param['spec_names'] = spec_names
            return_param['pos_names'] = pos_names
            print(pos_names)

            return render(request, "employee/j_d_form.html", return_param)
    elif len(request.POST) != 2:
        param = request.POST
        if len(param.get('name').split(" ")) > 2 and len(param.get('key_words').split(" ")) != 0:
            new_user = Employee.objects.create(name=param.get('name').split(" ")[1],
                                                surname=param.get('name').split(" ")[0],
                                                third_name=param.get('name').split(" ")[2],
                                                depat_name=param.get('depart'),
                                                group_name=param.get('group'),
                                                center_name=param.get('center'),
                                                job=param.get('key_words'))
            print(param.get('specialization'))
            Director.objects.filter(id=cache.get("id"))[0].id_emp.add(new_user)
            new_user.position.add(Position.objects.filter(name=param.get('position'))[0])
            new_user.specialization.add(Specialization.objects.filter(name=param.get('specialization'))[0])
            return redirect("storage")
        else:
            return_param = param.dict()
            return_param['errors'] = list()
            if len(param.get('name').split(" ")) <= 2:
                return_param['errors'].append("ФИО не заполнено")
            if len(param.get('key_words').split(" ")) == 0:
                return_param['errors'].append("Нет ключевых слов")

            pos_names = list()
            for i in list(Position.objects.all()):
                pos_names.append(i.name)
            spec_names = list()
            for i in list(Specialization.objects.all()):
                spec_names.append(i.name)
            return_param['spec_names'] = spec_names
            return_param['pos_names'] = pos_names
            print(pos_names)
            return render(request, "employee/j_d_form.html", return_param)
    elif len(request.POST) == 2:
        param = request.POST
        new_user = Employee.objects.filter(id=param['id'])[0]

        print("fgfg", param.get('specialization'))

        return_param = dict()
        pos_names = list()
        for i in list(Position.objects.all()):
            pos_names.append(i.name)
        spec_names = list()
        for i in list(Specialization.objects.all()):
            spec_names.append(i.name)
        return_param['spec_names'] = spec_names
        return_param['pos_names'] = pos_names

        return_param['name'] = new_user.name
        return_param['surname'] = new_user.surname
        return_param['third_name'] = new_user.third_name
        return_param['key_words'] = new_user.job
        cache.set("emp_id", param['id'])
        print("@@@@@@",param['id'])
        return render(request, "employee/j_d_form.html", return_param)

    else:
        return_param = dict()
        pos_names = list()
        for i in list(Position.objects.all()):
            pos_names.append(i.name)
        spec_names = list()
        for i in list(Specialization.objects.all()):
            spec_names.append(i.name)
        return_param['spec_names'] = spec_names
        return_param['pos_names'] = pos_names
        print(pos_names)
        return render(request, "employee/j_d_form.html", return_param)


def page_405(request, a):
    print("sdfsdfsdfdsf")
    return redirect('login')


def page_403(request):
    return redirect('login')