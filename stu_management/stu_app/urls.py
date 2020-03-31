from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('/data', include('stu_app.url.data_url')),
    path('/add', include('stu_app.url.add_url')),
    path('/change', include('stu_app.url.change_url')),
    path('/manage', include('stu_app.url.manage_url')),
]
