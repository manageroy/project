from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from stu_app import models
from django.core.cache import cache


def c_lass(request):
    classes = models.Student.objects.all()
    return JsonResponse(classes)


def grade(request):
    ponints = models.Points.objects.filter(stu_num=cache.get('stu_num'))
    pon_list = []
    for ponint in ponints:
        pon_dict = {
            'exam_time': ponint.exam_time,
            'write_points': ponint.write_points,
            'competer_points': ponint.competer_points,
            'total_points': ponint.total_points}
        pon_list.append(pon_dict)
    return JsonResponse({'ponints': pon_list})


def info(request):
    infos = models.Stu_msg.objects.all()
    return JsonResponse(infos)


def expression(request):
    expressions = models.School_expression.objects.all()
    return JsonResponse(expressions)


def changeClass(request):
    change_classes = models.Change_class.objects.all()
    return JsonResponse(change_classes)


def dropout(request):
    dropouts = models.Leave_school.objects.all()
    return JsonResponse(dropouts)


def feedback(request):
    feedbacks = models.Suggestions.objects.all()
    return JsonResponse(feedbacks)
