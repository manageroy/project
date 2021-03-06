# Generated by Django 3.0.3 on 2020-04-07 01:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Administrator',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=15)),
                ('permission', models.IntegerField()),
                ('job_num', models.CharField(max_length=10, unique=True)),
                ('manage_class', models.CharField(max_length=1)),
                ('password', models.CharField(default='123456', max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('class_name', models.CharField(max_length=6, unique=True)),
                ('profession', models.CharField(max_length=8)),
                ('teacher_name', models.CharField(max_length=15)),
                ('teach_name', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Suggestions',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('suggestion', models.TextField()),
                ('time', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(default='0', max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=15)),
                ('sex', models.CharField(max_length=1)),
                ('stu_num', models.CharField(max_length=13, unique=True)),
                ('password', models.CharField(default='123456', max_length=15)),
                ('permission', models.IntegerField(default=4)),
                ('class_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='students', to='stu_app.Class', to_field='class_name')),
            ],
        ),
        migrations.CreateModel(
            name='Stu_msg',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('id_num', models.CharField(max_length=18, unique=True)),
                ('age', models.CharField(max_length=3)),
                ('address', models.CharField(max_length=30)),
                ('time_of_enrollment', models.CharField(max_length=20)),
                ('recruiter', models.CharField(max_length=15)),
                ('phone', models.CharField(max_length=11)),
                ('parent', models.CharField(max_length=15)),
                ('parent_phone', models.CharField(max_length=11)),
                ('tuition', models.CharField(max_length=6)),
                ('loans', models.CharField(max_length=6)),
                ('credit', models.IntegerField(default=100)),
                ('stu_num', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='stu_info', to='stu_app.Student', to_field='stu_num')),
            ],
        ),
        migrations.CreateModel(
            name='School_expression',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('reason', models.TextField()),
                ('punish', models.TextField()),
                ('result', models.CharField(max_length=3)),
                ('status', models.CharField(default='0', max_length=2)),
                ('stu_num', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='school_expression', to='stu_app.Student', to_field='stu_num')),
            ],
        ),
        migrations.CreateModel(
            name='Points',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('exam_time', models.CharField(max_length=3)),
                ('write_points', models.IntegerField()),
                ('competer_points', models.IntegerField()),
                ('total_points', models.IntegerField()),
                ('stu_num', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Points', to='stu_app.Student', to_field='stu_num')),
            ],
        ),
        migrations.CreateModel(
            name='Leave_school',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('reason', models.TextField()),
                ('res', models.TextField()),
                ('status', models.CharField(default='0', max_length=2)),
                ('stu_num', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='dropout', to='stu_app.Student', to_field='stu_num')),
            ],
        ),
        migrations.CreateModel(
            name='Change_class',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('class_name', models.CharField(max_length=6)),
                ('before_class', models.CharField(max_length=6)),
                ('teacher_evaluate', models.TextField(default=' ')),
                ('change_class_reason', models.TextField(default='考试不合格')),
                ('res', models.TextField()),
                ('status', models.CharField(default='0', max_length=2)),
                ('stu_num', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='change_class', to='stu_app.Student', to_field='stu_num')),
            ],
        ),
    ]
