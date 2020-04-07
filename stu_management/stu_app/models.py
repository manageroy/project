from django.db import models


# Create your models here.
# 管理员表
class Administrator(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=15)
    permission = models.IntegerField()
    job_num = models.CharField(max_length=10, unique=True)  # 工号
    manage_class = models.CharField(max_length=1)
    password = models.CharField(max_length=15, default='123456')


# 学生表
class Student(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=15)  # 姓名
    sex = models.CharField(max_length=1)  # 年龄
    stu_num = models.CharField(max_length=13, unique=True)  # 学号
    password = models.CharField(max_length=15, default='123456')  # 密码
    permission = models.IntegerField(default=4)  # 权限
    class_name = models.ForeignKey('Class', to_field='class_name', related_name='student',
                                   on_delete=models.CASCADE)


# 班级表
class Class(models.Model):
    id = models.AutoField(primary_key=True)
    class_name = models.CharField(max_length=6)  # 班级名称
    profession = models.CharField(max_length=8)  # 专业
    teacher_name = models.CharField(max_length=15)  # 班主任
    teach_name = models.CharField(max_length=15)  # 任课老师


# 学生信息表
class Stu_msg(models.Model):
    id = models.AutoField(primary_key=True)
    id_num = models.CharField(max_length=18, unique=True)  # 身份证号
    age = models.CharField(max_length=3)
    # 籍贯
    address = models.CharField(max_length=30)
    # 入学时间
    time_of_enrollment = models.CharField(max_length=20)
    # 招生老师
    recruiter = models.CharField(max_length=15)
    phone = models.CharField(max_length=11)
    parent = models.CharField(max_length=15)
    parent_phone = models.CharField(max_length=11)
    # 学费
    tuition = models.CharField(max_length=6)
    # 贷款
    loans = models.CharField(max_length=6)
    # 学分
    credit = models.IntegerField(default=100)
    stu_num = models.OneToOneField('Student', to_field='stu_num', related_name='stu_info',
                                   on_delete=models.CASCADE)


# 转班表
class Change_class(models.Model):
    id = models.AutoField(primary_key=True)
    class_name = models.CharField(max_length=6)
    before_class = models.CharField(max_length=6)
    teacher_evaluate = models.TextField(default=' ')
    change_class_reason = models.TextField(default='考试不合格')
    res = models.TextField()
    status = models.CharField(default='0', max_length=2)
    stu_num = models.ForeignKey('Student', to_field='stu_num', related_name='change_class',
                                on_delete=models.CASCADE)


# 在校表现
class School_expression(models.Model):
    id = models.AutoField(primary_key=True)
    reason = models.TextField()
    punish = models.TextField()
    result = models.CharField(max_length=3)
    status = models.CharField(default='0', max_length=2)
    stu_num = models.ForeignKey('Student', to_field='stu_num', related_name='school_expression',
                                on_delete=models.CASCADE)


# 成绩表
class Points(models.Model):
    id = models.AutoField(primary_key=True)
    exam_time = models.CharField(max_length=3)
    write_points = models.IntegerField()
    competer_points = models.IntegerField()
    total_points = models.IntegerField()
    stu_num = models.ForeignKey('Student', to_field='stu_num', related_name='Points', on_delete=models.CASCADE)


# 建议表
class Suggestions(models.Model):
    id = models.AutoField(primary_key=True)
    suggestion = models.TextField()
    time = models.DateTimeField(auto_now=True)
    status = models.CharField(default='0', max_length=2)


# 退学表
class Leave_school(models.Model):
    id = models.AutoField(primary_key=True)
    reason = models.TextField()
    res = models.TextField()
    status = models.CharField(default='0', max_length=2)
    stu_num = models.OneToOneField(to_field='stu_num', to='Student', related_name='dropout',
                                   on_delete=models.CASCADE)
