from django.urls import path, include
from stu_app.views import add

urlpatterns = [
    path('/student', add.student),
    path('/info', add.info),
    path('/grade', add.grade),
    path('/feedback', add.feedback),
    path('/expression', add.expression),
    path('/change_class', add.change_class),
    path('/dropout', add.dropout),
]