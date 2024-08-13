from django.contrib import admin
from django.urls import path
from myApp import views

urlpatterns = [
    path('admin', admin.site.urls), 
    path('', views.index, name='index'),
    path('registro/', views.registro, name='registro'),
]
