from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.loginUser , name='loginUser'),
    path('register', views.register, name='register'),
    path('logoutUser', views.logoutUser, name='logoutUser'),
    path('organiseevent', views.organiseevent, name='organiseevent'),
    path('home', views.home, name='home'),
    path('UpdatedEvent/<int:Event_id>/', views.UpdatedEvent, name='UpdatedEvent'),
    path('tickets/<int:Event_id>/', views.tickets, name='tickets'),
]