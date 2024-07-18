from django.urls import path
from . import views

urlpatterns = [
    path('' , views.home),
    path('home/', views.home, name='frontpage_home'),
]