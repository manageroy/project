import json
from django.shortcuts import render, HttpResponse
from stu_app import models


def expression(request):
    res = json.loads(request.body)
    result = res['result']
    credit = res['credit']
    ex = models.School_expression.objects.filter(id=res['id']).first()
    if ex:
        ex.punish = result
        ex.result = credit
        ex.stu_num.credit = eval(f'{ex.stu_num.credit} + {credit}')
        ex.stu_num.save()
        ex.status = 1
        ex.save()
        return HttpResponse('ok')
    return HttpResponse('失败')


def change_class(request):
    res = json.loads(request.body)
    change = models.Change_class.objects.filter(id=res['id']).first()
    if res['select'] == 'male':
        class_name = models.Class.objects.filter(class_name=change.class_name).first()
        change.stu_num.class_name = class_name
        change.stu_num.save()
    change.status = 1
    change.res = res['result']
    change.save()
    return HttpResponse('ok')


def dropout(request):
    res = json.loads(request.body)
    drop = models.Leave_school.objects.filter(id=res['id']).first()
    if res['select'] == 'male':
        stu_num = drop.stu_num
        models.Dropout(name=stu_num.name, sex=stu_num.sex,
                       profession=stu_num.class_name.profession,
                       class_name=stu_num.class_name.class_name,
                       stu_num=stu_num.stu_num,
                       time_of_enrollment=stu_num.stu_info.time_of_enrollment,
                       reason=drop.reason
                       ).save()
        stu_num.delete()
        stu_num.save()
        return HttpResponse('ok')
    else:
        drop.res = res['result']
        drop.status = 1
        drop.save()
        return HttpResponse('ok')
