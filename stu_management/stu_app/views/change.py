from django.shortcuts import render, HttpResponse
from stu_app import models
from django.core.cache import cache
import json


def pwd(request):
    req = json.loads(request.body)
    pwd = req['pwd']
    pwd1 = req['pwd1']
    if cache.get('permission') == 4:
        res = models.Student.objects.filter(stu_num=cache.get('stu_num'), password=pwd).first()
    else:
        res = models.Administrator.objects.filter(job_num=cache.get('stu_num'), password=pwd).first()
    if res:
        res.password = pwd1
        res.save()
        cache.delete('stu_num')
        cache.delete('name')
        cache.delete('permission')
        return HttpResponse('密码修改成功')
    return HttpResponse('原密码错误')


def info(request):
    res = request.GET
    stu = models.Stu_msg.objects.get(stu_num=res['stu_num'])
    if stu:
        if request.method == 'GET':
            return render(request, 'update/change_info.html', context={'stu': stu})
        stu.id_num = request.POST.get('id_num')
        stu.age = request.POST.get("age")
        stu.address = request.POST.get("address")
        stu.time_of_enrollment = request.POST.get("time_of_enrollment")
        stu.recruiter = request.POST.get("recruiter")
        stu.phone = request.POST.get("phone")
        stu.parent = request.POST.get("parent")
        stu.parent_phone = request.POST.get("parent_phone")
        stu.money = request.POST.get("money")
        stu.loans = request.POST.get("loans")
        stu.save()
        return HttpResponse('ll')
