from django.urls import path, include
from stu_app.views import manage

urlpatterns = [
    path('/expression', manage.expression),
    path('/change_class', manage.change_class),
    path('/dropout', manage.dropout),
    path('/feedback', manage.feedback),
]