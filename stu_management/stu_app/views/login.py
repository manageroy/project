from django.shortcuts import render
from django.http import HttpResponseRedirect
from stu_app import models
def login(request):
    if request.method == 'GET':
        return render(request,'login.html')
    else:
        job_num=request.POST.get('job_num')
        password=request.POST.get('password')
        print(job_num)
        if job_num[:1] == 's':
            obj_stu = models.Student.objects.get(stu_num=job_num, password=password)
            if obj_stu:
                name = obj_stu.name
                return render(request, '../templates/main/student_main.html', {'name': name})
            return HttpResponseRedirect('/v1.0/login')
        else:
            obj = models.Administrator.objects.get(job_num=job_num, password=password)
            if obj:
                name=obj.name
                permission=obj.permission
                if permission==0:
                    return render(request,'../templates/main/high.html',{'name':name})
                elif permission==1:
                    return render(request,'../templates/main/teacher_main.html',{'name':name})
                else:
                    return render(request,'../templates/main/teach_main.html',{'name':name})
            else:
                return HttpResponseRedirect('/v1.0/login')

