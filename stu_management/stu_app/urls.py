from django.contrib import admin
from django.urls import path
from . import views
from . import dispose_from
from . import data

urlpatterns = [
    path('/index', views.index)
]
