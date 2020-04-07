from django.contrib import admin
from django.urls import path, include
from .views import login

urlpatterns = [
    path('data/', include('stu_app.url.data_url')),
    path('add/', include('stu_app.url.add_url')),
    path('change/', include('stu_app.url.change_url')),
    path('manage/', include('stu_app.url.manage_url')),
    path('login', login.login),
    path('main', login.main)
]
