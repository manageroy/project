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
    print(points)
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
    permission = cache.get('permission')
    infos = models.Stu_msg.objects.filter(stu_num=cache.get('stu_num'))
    infos_list = []
    for info in infos:
        if permission == 2:
            info_dict = {
                'name': info.stu_num.name,
                'sex': info.stu_num.sex,
                'class_name': info.stu_num.class_name,
                'profession': info.stu_num.profession,
                'stu_num': info.stu_num.stu_num,
                'teacher_name': info.stu_num.teacher_name,
                'teach_name': info.stu_num.teach_name,
                'age': info.age,
                'address': info.address,
                'phone': info.phone,
                'creadit': info.credit
            }
        else:
            info_dict = {
                'name': info.stu_num.name,
                'sex': info.stu_num.sex,
                'class_name': info.stu_num.class_name,
                'profession': info.stu_num.profession,
                'stu_num': info.stu_num.stu_num,
                'teacher_name': info.stu_num.teacher_name,
                'teach_name': info.stu_num.teach_name,
                'age': info.age,
                'address': info.address,
                'time_of_enrollment': info.time_of_enrollment,
                'recruiter': info.recruiter,
                'phone': info.phone,
                'parent': info.parent,
                'parent_phone': info.parent_phone,
                'tuition': info.tuition,
                'loans': info.loans,
                'creadit': info.credit
            }
        infos_list.append(info_dict)

    return JsonResponse({'infos': infos_list})


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
    try:
        dropouts = models.Leave_school.objects.filter()
        dropout_list = []
        for dropout in dropouts:
            dropout_dict = {
                'name': dropout.stu_num.name,
                'reason': dropout.reason,
                'teacher_name': dropout.stu_num.teacher_name,
                'id': dropout.id
            }
            dropout_list.append(dropout_dict)
        return JsonResponse({'dropouts': dropout_list})
    except Exception as e:
        return JsonResponse({'dropouts': [{
            'name': 'None',
            'reason': 'None',
            'teacher_name': 'None',
            'id': 'None'
        }]})


# 反馈表
def feedback(request):
    try:
        feedbacks = models.Suggestions.objects.filter()
        feedback_list = []
        for feedback in feedbacks:
            feedback_dict = {
                'suggestion': feedback.suggestion,
                'time': feedback.time,
                'id': feedback.id
            }
            feedback_list.append(feedback_dict)
        return JsonResponse({'feedbacks': feedback_list})
    except Exception as e:
        return JsonResponse({'feedbacks': [{
            'suggestion': 'None',
            'time': 'None',
            'id': 'None'
        }]})
