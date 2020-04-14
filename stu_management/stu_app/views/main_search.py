from django.http import JsonResponse
from stu_app import models
from django.core.cache import cache
import json
from stu_management.settings import LIST_NUM

class_name = models.Class.objects.all()
name = models.Student.objects.all()
permission=cache.get('permission')
def search_msg(request):
    search_msg = json.loads(request.body)['msg']
    msg_list = []
    if search_msg[0] in LIST_NUM :
        obj = class_name.get(class_name=search_msg+'班')
        if obj:
            dict = {
            'permisssions': 'c1',
            'classname': obj.class_name,
            'professiona': obj.profession,
            'teach_name': obj.teach_name,
            'teacher_name': obj.teacher_name,
            'count_num': name.filter(class_name=search_msg).count()
         }
            msg_list.append(dict)
            return JsonResponse({'msgss': msg_list})
    elif search_msg == name.filter(name=search_msg)[0].name:
        objs = name.filter(name=search_msg)
        for obj in objs:
            dict={
                        'permisssions': 'c2',
                        'nickname': obj.name,
                        'stu_numa': obj.stu_num,
                        'credita': obj.credit,
                        'class_name': obj.class_name.class_name,
                        'profeteacher_namessiona': obj.class_name.profession,
                        '': obj.class_name.teacher_name,
                        'teach_name': obj.class_name.teach_name
                    }
            msg_list.append(dict)
        return JsonResponse({'msgss':msg_list})
    else:
        return JsonResponse({'msgss':[{'permisssions':'空'}]})