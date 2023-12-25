from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='views-home'),
    path('addMyself/', views.add, name='views-add')
]