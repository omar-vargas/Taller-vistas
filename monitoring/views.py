from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers

def home(request):
    return  HttpResponse("WELCOME TO MY SITE WEB SITE")



def get_variables(request):
    variables = get_all_variables()
    variable_list = serializers.serialize('json',variables)
    return HttpResponse(variable_list, content_type='application/json')


def get_measurements(request):
    measurements = get_all_measurements()
    measurement_list = serializers.serialize('json',measurements)
    return HttpResponse(measurement_list, content_type='application/json')
