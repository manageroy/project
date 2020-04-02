from django.shortcuts import render, HttpResponse
from django.http import request


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

def info(request):
    pass
