from Parsing_MyServer.parser import Parser
from django.shortcuts import render
from .models import Sensors
from django.http import JsonResponse

data = Parser()

def base(request):
    return render(request, 'base.html')

def api_sensor(request):
    pars = data.get_data_serv()
    Sensors.objects.create(cpu=pars['cpu'], mem=pars['mem'], disk=pars['disk'])
    return JsonResponse(pars)

def api_data_users(request):
    pars = data.get_data_user()
    return JsonResponse(pars)

def sensors(request):
    return render(request, 'sensors.html')

def users(request):
    return render(request, 'users.html')

