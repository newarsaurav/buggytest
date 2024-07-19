from django.urls import path
from . import views

urlpatterns = [
    path('' , views.home),
    path('home/', views.home, name='frontpage_home'),
    path('blog/<int:id>', views.blog_page, name='blog_page'),
]