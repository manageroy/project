# Generated by Django 3.0.3 on 2020-04-08 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stu_app', '0003_auto_20200407_1050'),
    ]

    operations = [
        migrations.AddField(
            model_name='school_expression',
            name='time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
