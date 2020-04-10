# Generated by Django 3.0.3 on 2020-04-10 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stu_app', '0006_auto_20200410_0926'),
    ]

    operations = [
        migrations.CreateModel(
            name='dropout',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=15)),
                ('sex', models.CharField(max_length=15)),
                ('profession', models.CharField(max_length=15)),
                ('class_name', models.CharField(max_length=15)),
                ('stu_num', models.CharField(max_length=15)),
                ('time_of_enrollment', models.CharField(max_length=15)),
                ('reason', models.CharField(max_length=15)),
                ('dropout', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]