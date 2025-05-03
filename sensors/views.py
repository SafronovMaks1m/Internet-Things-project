from Parsing_MyServer.parser import Parser
from django.shortcuts import render
from .models import Sensors
from django.http import JsonResponse

def sensor(request):
    data = Parser()
    pars = data.get_data_serv()
    Sensors.objects.create(cpu=pars['cpu'], mem=pars['mem'], disk=pars['disk'])
    return JsonResponse(pars)

def base(request):
    return render(request, 'base.html')
