from django.shortcuts import render, HttpResponse
from stu_app import models
import json


def student(request):
    res = json.loads(request.body)
    name = res['name']
    sex = res['sex']
    class_name = res['class']
    stu_num = res['stu_num']
    cl = models.Class.objects.filter(class_name=class_name).first()
    if cl:
        models.Student(name=name, sex=sex, class_name=cl, stu_num='s' + stu_num,).save()
        return HttpResponse(f'学生{name}添加成功')
    return HttpResponse(f'学生{name}添加失败')


def info(request):
    if request.method == 'GET':
        return render(request, 'add/add_info.html')
    stu_num = request.POST.get('stu_num')
    stu = models.Student.objects.get(stu_num=stu_num)
    if stu:
        id_num = request.POST.get('id_num')
        age = request.POST.get("age")
        address = request.POST.get("address")
        time_of_enrollment = request.POST.get("time_of_enrollment")
        recruiter = request.POST.get("recruiter")
        phone = request.POST.get("phone")
        parent = request.POST.get("parent")
        parent_phone = request.POST.get("parent_phone")
        money = request.POST.get("money")
        loans = request.POST.get("loans")
        models.Stu_msg(stu_num=stu, id_num=id_num, age=age, address=address, time_of_enrollment=time_of_enrollment,
                       recruiter=recruiter, phone=phone, parent=parent, parent_phone=parent_phone, tuition=money,
                       loans=loans).save()
    return HttpResponse('ll')


def grade(request):
    res = json.loads(request.body)
    stu_num = res['stu_num']
    stu = models.Student.objects.filter(stu_num=stu_num).first()
    if stu:
        time = res["time"]
        pen = int(res["pen"])
        competer = int(res["competer"])
        models.Points(stu_num=stu, exam_time=time, write_points=pen, competer_points=competer,
                      total_points=pen + competer).save()
        return HttpResponse(f'学生{stu.name}考试成绩添加成功')
    return HttpResponse(f'没有此学生')


def feedback(request):
    suggestion = json.loads(request.body)['suggestion']
    models.Suggestions(suggestion=suggestion).save()
    return HttpResponse('提交成功')


def expression(request):
    res = json.loads(request.body)
    stu = models.Student.objects.filter(stu_num=res['stu_num'], name=res['name']).first()
    if stu:
        models.School_expression(stu_num=stu, reason=res['reason']).save()
        return HttpResponse('提交成功')
    return HttpResponse('没有此学生')


def change_class(request):
    res = json.loads(request.body)
    stu = models.Student.objects.filter(stu_num=res['stu_num'], name=res['name']).first()
    if stu:
        class_name = res["hope_class"]
        befor_class = res["befor_class"]
        models.Change_class(stu_num=stu, class_name=class_name, before_class=befor_class).save()
        return HttpResponse(f'学生{stu.name}转班申请以发送')
    return HttpResponse(f'没有此学生')


def dropout(request):
    res = json.loads(request.body)
    stu = models.Student.objects.filter(stu_num=res['stu_num'], name=res['name']).first()
    if stu:
        models.Leave_school(stu_num=stu, reason=res['reason']).save()
        return HttpResponse('提交成功')
    return HttpResponse('没有此学生')
