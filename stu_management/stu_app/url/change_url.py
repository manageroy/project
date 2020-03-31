from django.urls import path, include
from stu_app.views import change

urlpatterns = [
    path('/pwd', change.pwd),
    path('/info', change.info),
]