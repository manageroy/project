from django.urls import path
from stu_app.views import data

urlpatterns = [
    path('/class', data.c_lass),
    path('/grade', data.grade),
    path('/info', data.info),
    path('/expression', data.expression),
    path('/change_class', data.changeClass),
    path('/dropout', data.dropout),
    path('/feedback', data.feedback),
]
