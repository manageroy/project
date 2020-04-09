import json
from django.shortcuts import render, HttpResponse
from stu_app import models


def expression(request):
    ex = models.School_expression.objects.get(status=0)
    if request.method == 'GET':
        return render(request, 'manage/manage_expression.html', context={'res': ex})
    result = request.POST.get('result')
    credit = request.POST.get('credit')
    ex.punish = result
    ex.result = credit
    ex.stu_num.credit = eval(f'{ex.stu_num.credit} + {credit}')
    ex.stu_num.save()
    # ex.save()
    ex.status = 1
    ex.save()
    return HttpResponse('afeiowj')


def change_class(request):
    if request.method == 'GET':
        res = models.Change_class.objects.filter(status=0)[0]
        return render(request, 'manage/manage_change_class.html', context={'res': res})
    suggestion = request.POST.get('suggestion')
    res = models.Change_class.objects.filter(status=0)[0]
    res.status = 1
    res.res = suggestion
    res.save()
    return HttpResponse('ll')


def dropout(request):
    res = json.loads(request.body)
    drop = models.Leave_school.objects.filter(id=res['id']).first()
    drop.res = res['result']
    drop.status = 1
    drop.save()
    return HttpResponse('ok')
