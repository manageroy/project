import json
from django.http import JsonResponse
from stu_app import models
from django.core.cache import cache


# 班主任页管理班级
def classes(request):
    teacher_obj = models.Administrator.objects.get(job_num=cache.get('stu_num'))
    teacher_name = teacher_obj.name
    if cache.get('permission') == 1:
        classes = models.Class.objects.filter(teacher_name=teacher_name)
    elif cache.get('permission') == 2:
        classes = models.Class.objects.filter(teach_name=teacher_name)
    else:
        classes = models.Class.objects.filter()
    class_lsit = []
    for clas in classes:
        clas_dict = {
            'class_name': clas.class_name,
            'profession': clas.profession,
            'teach_name': clas.teach_name
        }
        class_lsit.append(clas_dict)
    return JsonResponse({'classes': class_lsit})


# 同一个班级的同学的所有信息
def class_student(request):
    if cache.get('permission') == 4:
        class_students = models.Student.objects.get(stu_num=cache.get('stu_num'))
        class_name = class_students.class_name
    else:
        res = json.loads(request.body)
        class_name = res['class_name']
    class_students2 = models.Student.objects.filter(class_name=class_name)
    same_classstudent_list = []
    for clas_stu in class_students2:
        name = clas_stu.name
        sex = clas_stu.sex
        credit = clas_stu.credit
        try:
            phone = clas_stu.stu_info.phone
            address = clas_stu.stu_info.address
        except:
            phone = None
            address = None
        clas_dict = {
            'name': name,
            'sex': sex,
            'phone': phone,
            'address': address,
            'credit': credit
        }
        same_classstudent_list.append(clas_dict)
    return JsonResponse({'class_students': same_classstudent_list})


# 个人分数
def grade(request):
    points = models.Points.objects.filter(stu_num=cache.get('stu_num'))
    pon_list = []
    for point in points:
        pon_dict = {
            'exam_time': point.exam_time,
            'write_points': point.write_points,
            'competer_points': point.competer_points,
            'total_points': point.total_points
        }
        pon_list.append(pon_dict)
    return JsonResponse({'points': pon_list})


# 个人信息
def info(request):
    info_obj = models.Stu_msg.objects.filter(stu_num=cache.get('stu_num')).first()
    info_dict = {
        'name': info_obj.stu_num.name,
        'sex': info_obj.stu_num.sex,
        'class_name': info_obj.stu_num.class_name.class_name,
        'profession': info_obj.stu_num.class_name.profession,
        'stu_num': info_obj.stu_num.stu_num,
        'teacher_name': info_obj.stu_num.class_name.teacher_name,
        'teach_name': info_obj.stu_num.class_name.teach_name,
        'age': info_obj.age,
        'address': info_obj.address,
        'phone': info_obj.phone,
        'creadit': info_obj.stu_num.credit
    }
    return JsonResponse({'info': info_dict})


# 表现表
def total_expression(request):
    expressions = models.School_expression.objects.filter(status=0)
    expression_list = []
    for expression in expressions:
        expression_dict = {
            'name': expression.stu_num.name,  # 姓名
            'class_name': expression.stu_num.class_name.class_name,  # 班级
            'id': expression.id,
            'profession': expression.stu_num.class_name.profession,  # 专业
            'teacher_name': expression.stu_num.class_name.teacher_name,  # 班主任
            'reason': expression.reason,  # 原因
            'time': expression.time,  # 时间
        }
        expression_list.append(expression_dict)
    return JsonResponse({'expressions': expression_list})


# 转班表
def changeClass(request):
    change_classes = models.Change_class.objects.filter(status=0)
    change_class_list = []
    for change_class in change_classes:
        change_class_dict = {
            'name': change_class.stu_num.name,
            'reason': change_class.change_class_reason,
            'profession': change_class.stu_num.class_name.profession,
            'teacher_name': change_class.stu_num.class_name.teacher_name,
            'class_name': change_class.class_name,
            'before_class': change_class.before_class,
            'id': change_class.id
        }
        change_class_list.append(change_class_dict)
    return JsonResponse({'change_classes': change_class_list})


# 退学表
def dropout(request):
    dropouts = models.Leave_school.objects.filter(status=0)
    dropout_list = []
    for dropout in dropouts:
        dropout_dict = {
            'name': dropout.stu_num.name,
            'class_name': dropout.stu_num.class_name.class_name,
            'profession': dropout.stu_num.class_name.profession,
            'reason': dropout.reason,
            'time_of_enrollment': dropout.stu_num.stu_info.time_of_enrollment,
            'teacher_name': dropout.stu_num.class_name.teacher_name,
            'id': dropout.id
        }
        dropout_list.append(dropout_dict)
    return JsonResponse({'dropouts': dropout_list})


# 反馈表
def feedback(request):
    feedbacks = models.Suggestions.objects.filter(status=0)
    feedback_list = []
    for suggestion in feedbacks:
        feedback_dict = {
            'suggestion': suggestion.suggestion,
            'time': suggestion.time,
        }
        feedback_list.append(feedback_dict)
        suggestion.status = 1
        suggestion.save()
    return JsonResponse({'feedbacks': feedback_list})
