from django.shortcuts import render, HttpResponse
from django.http import request


def student(request):
    if request.method == 'GET':
        return render(request, 'add_student.html')
    res = request.POST['name']
    print(res)
    return HttpResponse('ll')


def info(request):
    pass


def grade(request):
    pass


def feedback(request):
    pass


def expression(request):
    pass


def change_class(request):
    pass


def dropout(request):
    pass
