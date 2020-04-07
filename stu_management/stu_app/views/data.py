from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from stu_app import models
from django.core.cache import cache


def c_lass(request):
    pass


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
    pass


def expression(request):
    pass


def changeClass(request):
    pass


def dropout(request):
    pass


def feedback(request):
    pass
