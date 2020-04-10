from django.urls import path
from stu_app.views import data

urlpatterns = [
    path('class', data.classes),
    path('class_student', data.class_student),
    path('grade', data.grade),
    path('info', data.info),
    path('expression', data.total_expression),
    path('change_class', data.changeClass),
    path('dropout', data.dropout),
    path('feedback', data.feedback),
]
