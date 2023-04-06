from django.shortcuts import render, redirect

from director.models import Director


def login(request):
    if request.POST:
        param = request.POST
        if len(Director.objects.filter(login=param.get('login'))) != 0 \
                and Director.objects.filter(login=param.get('login'))[0].password == param.get('password'):
            return render(request, "director/storage.html")
        else:
            return render(request, "director/loginPage.html", {"error": "неправильный пароль/логин"})
    else:
        return render(request, "director/loginPage.html")


def registration(request):
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
            return render(request, "director/registration.html", {"error": "этот логин уже используется"})
    else:
        return render(request, "director/registration.html")



def storage(request):
    #id_dir = request.POST.get("id")

    return render(request, "director/storage.html")