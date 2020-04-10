from django.core.cache import cache
from django.test import TestCase

# Create your tests here.

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'stu_management.settings')
django.setup()

from stu_app import models

# print(cache.delete('name'))
# print(cache.get('name'))
#
# account = 1
# pwd = 1
# ex = models.Points.objects.filter(stu_num='s190101')
# for i in ex:
#     print(i.exam_time,
#           i.write_points,
#           i.competer_points,
#           i.total_points)
# expressions = models.School_expression.objects.filter(stu_num='s190101')
# print(expressions[0].stu_num.credit)
# info = models.Stu_msg.objects.filter(stu_num=cache.get('stu_num')).first()
# info_dict = {
#     'name': info.stu_num.name,
#     'sex': info.stu_num.sex,
#     'class_name': info.stu_num.class_name.class_name,
#     'profession': info.stu_num.class_name.profession,
#     'stu_num': info.stu_num.stu_num,
#     'teacher_name': info.stu_num.class_name.teacher_name,
#     'teach_name': info.stu_num.class_name.teach_name,
#     'age': info.age,
#     'address': info.address,
#     'phone': info.phone,
#     'creadit': info.stu_num.credit
# }
# print(info_dict)

