from django.shortcuts import render

from FrontPage.models import *

# Create your views here.
def home(request):
    data_landing_banner = landing_banner.objects.all()
    data_banner = banner.objects.all()
    data_service_list = service_list.objects.all()
    data_why_buggy_cloud = why_buggy_cloud.objects.all()
    data_front_blog = front_blog.objects.all()
    objs = {
        'landing_banner' : data_landing_banner,
        'banner' : data_banner,
        'service_list' : data_service_list,
        'why_buggy_cloud' : data_why_buggy_cloud,
        'front_blog' : data_front_blog,

    }

    print('------------------------------')
    for blog in data_front_blog:
        print(blog.subtitle)
        print(blog.title)
        print(blog.description)
  
    print('------------------------------z')
    return render(request, 'index.html' , objs)