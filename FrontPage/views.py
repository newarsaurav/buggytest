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
    return render(request, 'index.html' , objs)


def blog_page(request , id):
    data_front_blog = front_blog.objects.filter(id=id).values()
    all_blog = front_blog.objects.all()
    data_list = list(data_front_blog)
    objs = {
        "id"  : id,
        "data" : data_list[0],
        "blogs": all_blog
    }
    return render(request , 'blog.html' ,  objs)