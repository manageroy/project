# Generated by Django 3.0.3 on 2020-04-07 02:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stu_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='administrator',
            name='manage_class',
        ),
    ]
