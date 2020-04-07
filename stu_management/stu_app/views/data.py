from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from stu_app import models

def c_lass(request):
    classes=models.Student.objects.all()
    return JsonResponse(classes)

def grade(request):
    grades=models.Points.objects.all()
    return JsonResponse(grades)

def info(request):
    infos=models.Stu_msg.objects.all()
    return JsonResponse(infos)

def expression(request):
    expressions=models.School_expression.objects.all()
    return JsonResponse(expressions)

def changeClass(request):
    change_classes=models.Change_class.objects.all()
    return JsonResponse(change_classes)

def dropout(request):
    dropouts=models.Leave_school.objects.all()
    return JsonResponse(dropouts)

def feedback(request):
    feedbacks=models.Suggestions.objects.all()
    return JsonResponse(feedbacks)


