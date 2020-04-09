from django.http import JsonResponse
from stu_app import models
from django.core.cache import cache


# 班主任页管理班级
def classes(request):
    try:
        teacher_obj = models.Administrator.objects.get(stu_num=cache.get('stu_num'))
        teacher_name = teacher_obj.name
        classes = models.Class.objects.filter(teacher_name=teacher_name)
        class_lsit = []
        for clas in classes:
            clas_dict = {
                'class_name': clas.class_name,
                'profession': clas.profession,
                'teacher_name': clas.teacher_name,
                'teach_name': clas.teach_name
            }
            class_lsit.append(clas_dict)
        return JsonResponse({'classes': class_lsit})
    except Exception as e:
        return JsonResponse({'classes': [{
            'class_name': 'None',
            'profession': 'None',
            'teacher_name': 'None',
            'teach_name': 'None'
        }]})


# 同一个班级的同学的所有信息
def class_student(request):
    try:
        class_students = models.Student.objects.get(stu_num=cache.get('stu_num'))
        class_name = class_students.class_name
        class_students2 = models.Student.objects.filter(class_name=class_name)
        same_classstudent_list = []
        for clas_stu in class_students2:
            clas_dict = {
                'id': clas_stu.id,
                'name': clas_stu.name,
                'sex': clas_stu.sex,
                'phone': clas_stu.stu_msg.phone,
                'address': clas_stu.stu_msg.address,
                'credit': clas_stu.stu_msg.credit
            }
            same_classstudent_list.append(clas_dict)
        return JsonResponse({'class_students': same_classstudent_list})
    except Exception as e:
        return JsonResponse({'class_students': [{
            'id': 'None',
            'name': 'None',
            'sex': 'None',
            'phone': 'None',
            'address': 'None',
            'credit': 'None',
        }]})


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
    expressions = models.School_expression.objects.filter(stu_num=cache.get('stu_num'))
    expression_list = []
    for expression in expressions:
        expression_dict = {
            'reason': expression.reason,
            'punish': expression.punish,
            'result': expression.result,
            'time': expression.time.today(),
        }
        expression_list.append(expression_dict)
    return JsonResponse({'expressions': expression_list, 'credit': expressions[0].stu_num.credit})


# 转班表
def changeClass(request):
    try:
        change_classes = models.Change_class.objects.filter()
        change_class_list = []
        for change_class in change_classes:
            change_class_dict = {
                'name': change_class.stu_num.name,
                'reason': change_class.change_class_reason,
                'profession': change_class.stu_num.profession,
                'class_name': change_class.class_name,
                'id': change_class.id
            }
            change_class_list.append(change_class_dict)
        return JsonResponse({'change_classes': change_class_list})
    except Exception as e:
        return JsonResponse({'change_classes': [{
            'name': 'None',
            'reason': 'None',
            'profession': 'None',
            'class_name': 'None',
            'id': 'None'
        }]})


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
