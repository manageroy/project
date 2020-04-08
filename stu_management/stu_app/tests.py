from django.test import TestCase

# Create your tests here.

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'stu_management.settings')
django.setup()

# from stu_app import models
#
# account = 1
# pwd = 1
# ex = models.Points.objects.filter(stu_num='s190101')
# for i in ex:
#     print(i.exam_time,
#           i.write_points,
#           i.competer_points,
#           i.total_points)
#
