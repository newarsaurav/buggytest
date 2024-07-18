from django.shortcuts import render
from django.http import HttpResponse
from adminground.models import Slider, ServiceList , Saurav , Surname ,BlogList
# Create your views here.
# request->response
# request handler

def test(request):
    return HttpResponse('heloworld')

def home(request):
    sliders = (Slider.objects.values())
    sau = [(Saurav.objects.values())]
    sur = [(Surname.objects.values())]
    service_lists = ServiceList.objects.filter(active=True).values()
    bloglist = BlogList.objects.values()

    return render(request , 'home.html' , {'sliders':  sliders , 'service_lists' : service_lists , 'sau' : sau ,'sur' : sur , 'bloglist': bloglist})
