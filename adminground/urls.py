from django.urls import path
from . import views

urlpatterns = [
    path('' , views.home),
    path('test/' , views.test),
    path('adminhome/' , views.home),
    path('home/' , views.home)
]