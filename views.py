from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import HttpResponse

from django.contrib import auth

from app01.models import UserTable, DataReport


# from rbac.service.initail import initial_sesson


def login(request):
    if request.method == "GET":
        return render(request, "login.html")

    elif request.method == "POST":
        user = request.POST.get("user")
        pwd = request.POST.get("pwd")
        user = UserTable.objects.filter(username=user, password=pwd)

        if user:
            rbac = user.values()
            data = DataReport.objects.all().values()

            return render(request, "ok.html", locals())
        return HttpResponse("ok")


def update(request):
    print(request.POST.get("rbac"))

    if request.POST.get("rbac"):
        rbac = request.POST.get("rbac")
        print("rbac:", rbac)

        if request.method == "POST":
            date = request.POST.get("date")
            Ad_name = request.POST.get("Ad_name")
            Distribution_channel = request.POST.get("Distribution_channel")
            Exposure = request.POST.get("Exposure")
            Click_volume = request.POST.get("Click_volume")
            Click_rate = request.POST.get("Click_rate")
            price = request.POST.get("price")
            Consumption = request.POST.get("Consumption")

            DataReport.objects.create(date=date, Ad_name=Ad_name, Distribution_channel=Distribution_channel,
                                      Exposure=Exposure, Click_volume=Click_volume, Click_rate=Click_rate, price=price,
                                      Consumption=Consumption)

    return HttpResponse("ok")

def chaxun(request):
    dic = {}
    Ad_name = request.POST.get("Ad_name")
    if Ad_name:
        dic["Ad_name"]=Ad_name
    else:
        pass
    date = request.POST.get("date")
    if date:
        dic["date"]=date
    else:
        pass
    Distribution_channel = request.POST.get("Distribution_channel")
    if Distribution_channel:
        dic["Distribution_channel"]=Distribution_channel
    else:
        pass
    print(dic)

    chaxunshuju = DataReport.objects.filter(**dic)

    print(chaxunshuju.values())

    return HttpResponse("ok")

