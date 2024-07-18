from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib import messages

from django.http import HttpResponseRedirect

from adminground.models import *

# Create your views here.
def admin_login(request):
    try:
        if request.user.is_authenticated:
            return redirect('/dashboard')
        if request.method =="POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            user_obj = User.objects.filter(username=username)
            if not user_obj.exists():
                messages.info(request,'account not found')
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            
            user_obj = authenticate(username = username , password = password)

            if user_obj and user_obj.is_superuser:
                login(request , user_obj)
                return redirect('/dashboard')
            
            messages.info(request , 'invalid password')
            return redirect('/')
        
        return render(request , 'login.html')
    except Exception as e:
        print(e)


def dashboard(request):
    return render(request , 'dashboard.html')

def cust_slider(request):
    objs = Slider.objects.all()
    objs_list =  {
            'id': objs[0].id,
            'header': objs[0].header,
            'sub_header': objs[0].sub_header,
            'image_path': objs[0].image_path,
            'active': objs[0].active
        } 
    
    return render(request , 'sliders.html', {'datas': objs_list})

def update_cust_slider(request , id):
    
    objs = get_object_or_404(Slider, id=id)
    t = request.POST.get('header')
   
    if request.method == 'POST':
        objs.header = request.POST.get('header', objs.header)
        objs.sub_header = request.POST.get('sub_header', objs.sub_header)
        objs.image_path = request.POST.get('image_path', objs.image_path)
        objs.save()

        return redirect('slider')

def cust_serviceList(request):
    objs = ServiceList.objects.all()
    objs_list =  {
            'id': objs[0].id,
            'title': objs[0].title,
            'sub_title': objs[0].sub_title,
            'service_type': objs[0].service_type,
            'active': objs[0].active
        } 
    
    return render(request , 'servicelist.html', {'datas': objs_list})
