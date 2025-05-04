from Parsing_MyServer.parser import Parser
from django.shortcuts import render
from .models import Sensors, Users, DataUser
from django.http import JsonResponse

data = Parser()

def api_sensor(request):
    pars = data.get_data_serv()
    Sensors.objects.create(cpu=pars['cpu'], mem=pars['mem'], disk=pars['disk'])
    return JsonResponse(pars)

def api_data_users(request):
    pars = data.get_data_user()
    for k, v in pars.items():
        get_user = Users.objects.get_or_create(name = k)[0]
        DataUser.objects.create(upload=v['upload'], download=v['download'], 
                                traffic=v['traffic'], user=get_user)
    return JsonResponse(pars)

def base(request):
    return render(request, 'base.html')

def sensors(request):
    return render(request, 'sensors.html')

def users(request):
    return render(request, 'users.html')

