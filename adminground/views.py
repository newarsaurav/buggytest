from django.shortcuts import render
from django.http import HttpResponse
from adminground.models import Slider
# Create your views here.
# request->response
# request handler

def test(request):
    return HttpResponse('heloworld')

def home(request):
    sliders = (Slider.objects.values())
    print(sliders)
    return render(request , 'home.html' , {'sliders':
                                           sliders})

# def home(request):
#     return render(request , 'home.html' , {'name':'mosh'})