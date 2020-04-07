from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from stu_app import models
from django.core.cache import cache


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        job_num = request.POST.get('job_num')
        password = request.POST.get('password')
        print(job_num)
        if 's' in job_num:
            obj_stu = models.Student.objects.get(stu_num=job_num, password=password)
            if obj_stu:
                cache.set('stu_num', obj_stu.stu_num)
                cache.set('name', obj_stu.name)
                cache.set('permission', obj_stu.permission)
                return redirect('/v1.0/main')
            return HttpResponseRedirect('/v1.0/login')
        else:
            obj = models.Administrator.objects.get(job_num=job_num, password=password)
            if obj:
                cache.set('stu_num', obj.job_num)
                cache.set('name', obj.name)
                cache.set('permission', obj.permission)
                return redirect('/v1.0/main')
            else:
                return HttpResponseRedirect('/v1.0/login')


def main(request):
    if cache.get('permission') == 0:
        return render(request, '../templates/main/high.html', {'name': cache.get('name')})
    elif cache.get('permission') == 1:
        return render(request, '../templates/main/teacher_main.html', {'name': cache.get('name')})
    elif cache.get('permission') == 2:
        return render(request, '../templates/main/teach_main.html', {'name': cache.get('name')})
    else:
        return render(request, '../templates/main/student_main.html', {'name': cache.get('name')})
