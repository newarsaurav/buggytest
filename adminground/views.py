from django.shortcuts import render
from django.http import HttpResponse
from adminground.models import Slider, ServiceList
# Create your views here.
# request->response
# request handler

def test(request):
    return HttpResponse('heloworld')

def home(request):
    sliders = (Slider.objects.values())
    service_lists = ServiceList.objects.filter(active=True).values()

    return render(request , 'home.html' , {'sliders':  sliders , 'service_lists' : service_lists})
