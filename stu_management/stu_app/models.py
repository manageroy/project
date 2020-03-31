from django.db import models

# Create your models here.
# 管理员表
class Administrator(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=15)
    permission=models.IntegerField(max_length=1)
    manage_class=models.CharField(max_length=1)
    password=models.CharField(max_length=15,default='123456')

#学生表
class Student(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=15)
    sex=models.CharField(max_length=1)
    class_name=models.CharField(max_length=6)
    # 专业
    profession=models.CharField(max_length=8)
    teacher_name=models.CharField(max_length=15)
    teach_name=models.CharField(max_length=15)
    password=models.CharField(max_length=15,default='123456')
    #权限
    permission=models.IntegerField(default=4)

# 学生信息表
class Stu_msg(models.Model):
    id=models.AutoField(primary_key=True)
    id_num=models.CharField(max_length=18,unique=True)
    age=models.CharField(max_length=3)
    #籍贯
    address=models.CharField(max_length=30)
    #入学时间
    come_of_enrollment=models.CharField(max_length=20)
    #招生老师
    recruiter=models.CharField(max_length=15)
    tel_num=models.CharField(max_length=11)
    parent_name=models.CharField(max_length=15)
    parent_tel_num=models.CharField(max_length=11)
    #学费
    tuition=models.CharField(max_length=6)
    #贷款
    loans=models.CharField(max_length=6)
    # 学分
    credit=models.IntegerField(max_length=3)
    s_id = models.OneToOneField(to_field='name', to='Student',on_delete=models.CASCADE)

# 转班表
class Change_class(models.Model):
    id = models.AutoField(primary_key=True)
    class_name=models.CharField(max_length=6)
    before_class_name=models.CharField(max_length=6)
    teacher_evaluate=models.TextField(default=' ')
    change_class_num=models.IntegerField()
    status=models.CharField(default='0')

#在校表现
class School_expression(models.Model):
    id = models.AutoField(primary_key=True)
    reason=models.TextField()
    punish=models.TextField()
    result=models.CharField(max_length=3)
    s_id=models.ForeignKey('Student',to_field='name',on_delete=models.CASCADE)

#成绩表
class Points(models.Model):
    id = models.AutoField(primary_key=True)
    exam_time=models.CharField(max_length=3)
    write_points=models.IntegerField()
    competer_points=models.IntegerField()
    total_points=models.IntegerField()
    s_id=models.ForeignKey('Student',to_field='name',on_delete=models.CASCADE)

#建议表
class Suggestions(models.Model):
    id=models.AutoField(primary_key=True)
    sug_content=models.TextField()
    time=models.DateTimeField(auto_now=True)
    status=models.CharField(default='0')

#退学表
class Leave_school(models.Model):
    id=models.AutoField(primary_key=True)
    reason=models.TextField()
    status=models.CharField(default='0')
    s_id=models.OneToOneField(to_field='name', to='Student',on_delete=models.CASCADE)