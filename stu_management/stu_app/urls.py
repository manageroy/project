from django.contrib import admin
from django.urls import path, include
from .views import login,main_search

urlpatterns = [
    path('data/', include('stu_app.url.data_url')),
    path('add/', include('stu_app.url.add_url')),
    path('change/', include('stu_app.url.change_url')),
    path('manage/', include('stu_app.url.manage_url')),
    path('login', login.login),
    path('main', login.main),
    path('logout', login.logout),
    path('search_msg',main_search.search_msg)
]
