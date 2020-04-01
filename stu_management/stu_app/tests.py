from django.test import TestCase

# Create your tests here.

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'stu_management.settings')
django.setup()


from stu_app import models

res = models.Student.objects.get(stu_num='s190101')
print(res.stu_info.loans)
