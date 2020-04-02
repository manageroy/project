from django.test import TestCase

# Create your tests here.

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'stu_management.settings')
django.setup()

from stu_app import models
account = 1
pwd = 1
ex = models.Student.objects.filter(stu_num=account, password=pwd)[0]
print(ex.password)
