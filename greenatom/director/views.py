from django.core.cache import cache
from django.shortcuts import render, redirect

from director.models import Director

from employee.models import Employee


def login(request):
    if len(request.POST) > 1:
        param = request.POST
        if len(Director.objects.filter(login=param.get('login'))) != 0 \
                and Director.objects.filter(login=param.get('login'))[0].password == param.get('password'):
            print(request.session)
            cache.set("auth", "true")
            cache.set("id", Director.objects.filter(login=param.get('login'))[0].id)
            return redirect("storage")
        else:
            return_param = param.dict()
            return_param['errors'] = list()
            return_param['errors'].append("Неверный пароль/логин")
            return render(request, "director/loginPage.html", return_param)
    else:
        return render(request, "director/loginPage.html")


def registration(request):
    print(request.POST)
    if len(request.POST) == 1:
        return render(request, "director/registration.html")
    if request.POST:
        param = request.POST
        if len(Director.objects.filter(login=param.get('login'))) == 0 and len(param.get('name').split(" ")) > 2:
            Director.objects.create(name=param.get('name').split(" ")[1],
                                    surname=param.get('name').split(" ")[0],
                                    third_name=param.get('name').split(" ")[2::],
                                    depat_name=param.get('depart'),
                                    group_name=param.get('group'),
                                    center_name=param.get('center'),
                                    pos_name=param.get('position'),
                                    login=param.get('login'),
                                    password=param.get('password'))

            return redirect("login")
        else:
            return_param = param.dict()
            return_param['errors'] = list()
            if len(Director.objects.filter(login=param.get('login'))) != 0:
                return_param['errors'].append("Этот логин уже используется")
            if len(param.get('password')) < 8:
                return_param['errors'].append("Длина пароля должна быть больше 8 символов")
            if len(param.get('name').split(" ")) <= 2:
                return_param['errors'].append("ФИО не заполнено")
            if param.get('position') == '':
                return_param['errors'].append("Не указана должность")
            if param.get('group') == '':
                return_param['errors'].append("Не указана группа")
            if param.get('depart') == '':
                return_param['errors'].append("Не указан отдел")
            if param.get('center') == '':
                return_param['errors'].append("Не указан центр")

            return render(request, "director/registration.html", return_param)
    else:
        return render(request, "director/registration.html")


def storage(request):
    if cache.get("auth") == 'true':
        if request.POST.get('password') == "exit":
            cache.delete("auth")
            cache.delete("id")
            return redirect('login')
        else:
            print(cache.get("id"))
            emps = Director.objects.filter(id=cache.get("id"))[0].id_emp.all()
            param = dict()
            param["pos"] = list()
            param["emps"] = list()
            print(Employee.objects.filter(id=1)[0].position.filter(id=1)[0].name)
            for i in emps:
                param["emps"].append(i)
                param["pos"].append(i.position.all()[0].name)
            return render(request, "director/storage.html", param)
    else:
        return redirect('login')
    #id_dir = request.POST.get("id")



