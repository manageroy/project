from django.shortcuts import render, HttpResponse
from stu_app import models


def res(request, parameter: list):
    r = {}
    for i in parameter:
        r[i] = (request.POST.get(i))
    return r


def student(request):
    if request.method == 'GET':
        return render(request, 'add/add_student.html')
    name = request.POST.get('name')
    sex = request.POST.get('sex')
    class_name = request.POST.get('class')
    major = request.POST.get('major')
    stu_num = request.POST.get('stu_num')
    teacher = request.POST.get('teacher')
    teach = request.POST.get('teach')
    models.Student(name=name, sex=sex, class_name=class_name, profession=major, stu_num='s' + stu_num,
                   teacher_name=teacher, teach_name=teach).save()
    return render(request, 'add/add_student.html')


def info(request):
    if request.method == 'GET':
        return render(request, 'add/add_info.html')

    stu_num = request.POST.get('stu_num')
    stu = models.Student.objects.get(stu_num=stu_num)
    print(stu.stu_num)
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
    if request.method == 'GET':
        return render(request, 'add/add_grade.html')
    stu_num = request.POST.get('stu_num')
    stu = models.Student.objects.get(stu_num=stu_num)
    if stu:
        time = request.POST.get("time")
        pen = int(request.POST.get("pen"))
        competer = int(request.POST.get("competer"))
        models.Points(stu_num=stu, exam_time=time, write_points=pen, competer_points=competer,
                      total_points=pen + competer).save()
    return render(request, 'add/add_grade.html')


def feedback(request):
    if request.method == 'GET':
        return render(request, 'add/add_feedback.html')
    suggestion = request.POST.get('suggestion')
    models.Suggestions(suggestion=suggestion).save()
    return HttpResponse('ok')


def expression(request):
    if request.method == 'GET':
        return render(request, 'add/add_expression.html')
    stu_num = request.POST.get('stu_num')
    stu = models.Student.objects.get(stu_num=stu_num)
    if stu:
        reason = request.POST.get("reason")
        models.School_expression(reason=reason, stu_num=stu).save()
    return HttpResponse('ok')


def change_class(request):
    if request.method == 'GET':
        return render(request, 'add/add_change_class.html')
    stu_num = request.POST.get('stu_num')
    stu = models.Student.objects.get(stu_num=stu_num)
    if stu:
        name = request.POST.get("name")
        class_name = request.POST.get("class")
        befor_class = request.POST.get("befor_class")
        teacher_evaluate = request.POST.get("teacher_evaluate")
        num = request.POST.get("num")
        models.Change_class(stu_num=stu, class_name=class_name, before_class=befor_class,
                            teacher_evaluate=teacher_evaluate, change_class_num=num).save()
    return HttpResponse('ok')


def dropout(request):
    if request.method == 'GET':
        return render(request, 'add/add_dropout.html')
    stu_num = request.POST.get('stu_num')
    stu = models.Student.objects.get(stu_num=stu_num)
    if stu:
        reason = request.POST.get("reason")
        models.Leave_school(stu_num=stu, reason=reason).save()
    return HttpResponse('ok')
