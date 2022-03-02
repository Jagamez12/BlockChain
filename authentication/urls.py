from django import views
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('singup',views.singup, name="singup"),
    path('singin',views.singin, name="singin"),
    path('singout',views.singout, name="singout")
]