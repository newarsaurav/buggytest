from django.contrib import admin

from django.urls import path
from . import views

urlpatterns = [
    path('' , views.admin_login),
    path('dashboard/' , views.dashboard),
    path('dashboard/slider/', views.cust_slider, name='slider'),

    path('dashboard/slider/<int:id>', views.update_cust_slider, name='update_servicelist'),


    path('dashboard/servicelist/', views.cust_serviceList, name='servicelist'),

   
]