from django.shortcuts import render, HttpResponse

from stu_app import models
import json


<<<<<<< HEAD
def pwd(request):
    if request.method == 'GET':
        return render(request, 'update/change_pwd.html')
    req = json.loads(request.body)
    account = req['account']
    pwd = req['pwd']
    pwd1 = req['pwd1']
    res = models.Student.objects.filter(stu_num=account, password=pwd)[0]
    res.password = pwd1
    res.save()
    return HttpResponse('ok')

=======
def pwd(request,name):
    if request.method=='GET':
        return render(request,'../templates/update/change_pwd.html')
    else:
        password1=request.POST.get('pwd1')
        password2=request.POST.get('pwd3')
        stu=models.Student.objects.get(name=name,password=password1)
        if stu:
            obj=models.Student.objects.get(name=name)
            obj.password=password2
            obj.save()
            return HttpResponseRedirect('/v1.0/login')
>>>>>>> 4f4280ff43bc75bc09601a1cc72b58d2950fe711

def info(request):
    stu = models.Stu_msg.objects.get(stu_num=1)
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
