from django.http import JsonResponse
from stu_app import models
from django.core.cache import cache
import json

name = models.Student.objects.all()
permission = cache.get('permission')


def search_msg(request):
    search_msg = json.loads(request.body)['msg']
    print(search_msg)
    msg_list = []
    objs = name.filter(name=search_msg)
    for obj in objs:
        dict = {
            'nickname': obj.name,
            'stu_numa': obj.stu_num,
            'credita': obj.credit,
            'class_name': obj.class_name.class_name,
            'profeteacher_namessiona': obj.class_name.profession,
            '': obj.class_name.teacher_name,
            'teach_name': obj.class_name.teach_name
        }
        msg_list.append(dict)
    return JsonResponse({'msgss': msg_list})
