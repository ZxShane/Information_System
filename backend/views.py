from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.core import serializers
from django.http import JsonResponse
import json

from .models import User_Info,Graduation_Destination,Book_Info,Course_Info,Certification_Info



# Create your views here.

# 增

# 添加学生信息（已测试）
@require_http_methods(["GET"])
def add_student(request):
    response = {}
    try:
        student = User_Info(
            user_number=request.GET.get('user_number'),
            user_id = request.GET.get('user_id'),
            user_password = request.GET.get('user_password'),
            user_name = request.GET.get('user_name'),
            user_gender = request.GET.get('user_gender'),
            user_class = request.GET.get('user_class')

        )
        student.save()
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)

# 添加毕业去向（已测试）
@require_http_methods(["GET"])
def add_destination(request):
    response = {}
    try:
        student = Graduation_Destination(
            user_number=request.GET.get('user_number'),
            user_name = request.GET.get('user_name'),
            user_email = request.GET.get('user_email'),
            # destination_department = request.GET.get('destination_department'),
            type = request.GET.get('type'),
            destination_info = request.GET.get('destination_info'),
            ischeck = request.GET.get('ischeck')

        )
        student.save()
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


# 添加书籍信息（已测试）
@require_http_methods(["GET"])
def add_book(request):
    response = {}
    try:
        student = Book_Info(
            book_id=request.GET.get('book_id'),
            book_name = request.GET.get('book_name'),
            author = request.GET.get('author'),
            publisher = request.GET.get('publisher'),
            introduction = request.GET.get('introduction'),
            ischeck = request.GET.get('ischeck'),
            publisher_email = request.GET.get('publisher_email'),
            type=request.GET.get('type'),
            user_number=request.GET.get('user_number')
        )
        student.save()
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)

# 添加幕课信息（已测试）
@require_http_methods(["GET"])
def add_course(request):
    response = {}
    try:
        student = Course_Info(
            course_id=request.GET.get('course_id'),
            course_name = request.GET.get('course_name'),
            publisher = request.GET.get('publisher'),
            book = request.GET.get('book'),
            introduction = request.GET.get('introduction'),
            ischeck = request.GET.get('ischeck'),
            publisher_email=request.GET.get('publisher_email'),
            teacher = request.GET.get('teacher'),
            type=request.GET.get('type'),
            user_number=request.GET.get('user_number')

        )
        student.save()
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


# 添加考证信息（已测试）
@require_http_methods(["GET"])
def add_certification(request):
    response = {}
    try:
        student = Certification_Info(
            certification_id=request.GET.get('certification_id'),
            certification_name = request.GET.get('certification_name'),
            publisher = request.GET.get('publisher'),
            introduction = request.GET.get('introduction'),
            ischeck = request.GET.get('ischeck'),
            link=request.GET.get('link'),
            publisher_email = request.GET.get('publisher_email'),
            user_number=request.GET.get('user_number')

        )
        student.save()
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


# 删
# 删除学生信息（已测试）
@require_http_methods(["GET"])
def delete_student(request):
    response = {}
    try:
        User_Info.objects.all().filter(user_number=request.GET.get('user_number')).delete()
        # be_evaluate_num = be_evaluate_students.be_evaluate_stu_num
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


# 删除毕业去向（已测试）
@require_http_methods(["GET"])
def delete_destination(request):
    response = {}
    try:
        Graduation_Destination.objects.all().filter(user_number=request.GET.get('user_number')).delete()
        # be_evaluate_num = be_evaluate_students.be_evaluate_stu_num
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


# 删除书籍信息（已测试）
@require_http_methods(["GET"])
def delete_book(request):
    response = {}
    try:
        Book_Info.objects.all().filter(book_id=request.GET.get('book_id')).delete()
        # be_evaluate_num = be_evaluate_students.be_evaluate_stu_num
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


# 删除幕课信息（已测试）
@require_http_methods(["GET"])
def delete_course(request):
    response = {}
    try:
        Course_Info.objects.all().filter(course_id=request.GET.get('course_id')).delete()
        # be_evaluate_num = be_evaluate_students.be_evaluate_stu_num
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


# 删除考证信息（已测试）
@require_http_methods(["GET"])
def delete_certification(request):
    response = {}
    try:
        Certification_Info.objects.all().filter(certification_id=request.GET.get('certification_id')).delete()
        # be_evaluate_num = be_evaluate_students.be_evaluate_stu_num
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


# 查
# 查看所有学生信息（已测试）
@require_http_methods(["GET"])
def show_all_users(request):
    response = {}
    try:
        users=User_Info.objects.all()
        # be_evaluate_num = be_evaluate_students.be_evaluate_stu_num
        response['list'] = json.loads(serializers.serialize("json", users))
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


# 查看所有毕业去向（已测试）
@require_http_methods(["GET"])
def show_all_destinations(request):
    response = {}
    try:
        destinations=Graduation_Destination.objects.all()
        # be_evaluate_num = be_evaluate_students.be_evaluate_stu_num
        response['list'] = json.loads(serializers.serialize("json", destinations))
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


# 查看所有书籍信息（已测试）
@require_http_methods(["GET"])
def show_all_books(request):
    response = {}
    try:
        books=Book_Info.objects.all()
        # be_evaluate_num = be_evaluate_students.be_evaluate_stu_num
        response['list'] = json.loads(serializers.serialize("json", books))
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


# 查看所有幕课信息（已测试）
@require_http_methods(["GET"])
def show_all_courses(request):
    response = {}
    try:
        courses=Course_Info.objects.all()
        # be_evaluate_num = be_evaluate_students.be_evaluate_stu_num
        response['list'] = json.loads(serializers.serialize("json", courses))
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


# 查看所有考证信息（已测试）
@require_http_methods(["GET"])
def show_all_certifications(request):
    response = {}
    try:
        certifications=Certification_Info.objects.all()
        # be_evaluate_num = be_evaluate_students.be_evaluate_stu_num
        response['list'] = json.loads(serializers.serialize("json", certifications))
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


# 查某一个学生的信息（已测试）
@require_http_methods(["GET"])
def show_one_user(request):
    response = {}
    try:
        print(request.GET.get('user_number'))
        user=User_Info.objects.all().filter(user_number=request.GET.get('user_number'))
        # be_evaluate_num = be_evaluate_students.be_evaluate_stu_num
        response['list'] = json.loads(serializers.serialize("json", user))
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


# 查某一个学生的毕业去向（已测试）
@require_http_methods(["GET"])
def show_one_destination(request):
    response = {}
    try:
        destination=Graduation_Destination.objects.all().filter(user_number=request.GET.get('user_number'))
        # be_evaluate_num = be_evaluate_students.be_evaluate_stu_num
        response['list'] = json.loads(serializers.serialize("json", destination))
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)

@require_http_methods(["GET"])
def show_someone_destination(request):
    response = {}
    try:
        destinations=Graduation_Destination.objects.all().filter(user_number=request.GET.get('user_number'))
        # be_evaluate_num = be_evaluate_students.be_evaluate_stu_num
        response['list'] = json.loads(serializers.serialize("json", destinations))
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


# 查某一本书的信息（已测试）
@require_http_methods(["GET"])
def show_one_book(request):
    response = {}
    try:
        book=Book_Info.objects.all().filter(book_id=request.GET.get('book_id'))
        # be_evaluate_num = be_evaluate_students.be_evaluate_stu_num
        response['list'] = json.loads(serializers.serialize("json", book))
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)

@require_http_methods(["GET"])
def show_someone_book(request):
    response = {}
    try:
        books=Book_Info.objects.all().filter(user_number=request.GET.get('user_number'))
        # be_evaluate_num = be_evaluate_students.be_evaluate_stu_num
        response['list'] = json.loads(serializers.serialize("json", books))
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


# 查某一个幕课的信息（已测试）
@require_http_methods(["GET"])
def show_one_course(request):
    response = {}
    try:
        course=Course_Info.objects.all().filter(course_id=request.GET.get('course_id'))
        # be_evaluate_num = be_evaluate_students.be_evaluate_stu_num
        response['list'] = json.loads(serializers.serialize("json", course))
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)

@require_http_methods(["GET"])
def show_someone_course(request):
    response = {}
    try:
        courses=Course_Info.objects.all().filter(user_number=request.GET.get('user_number'))
        # be_evaluate_num = be_evaluate_students.be_evaluate_stu_num
        response['list'] = json.loads(serializers.serialize("json", courses))
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)

# 查某一个考证信息（已测试）
@require_http_methods(["GET"])
def show_one_certification(request):
    response = {}
    try:
        certification=Certification_Info.objects.all().filter(certification_id=request.GET.get('certification_id'))
        # be_evaluate_num = be_evaluate_students.be_evaluate_stu_num
        response['list'] = json.loads(serializers.serialize("json", certification))
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)

@require_http_methods(["GET"])
def show_someone_certification(request):
    response = {}
    try:
        certifications=Certification_Info.objects.all().filter(user_number=request.GET.get('user_number'))
        # be_evaluate_num = be_evaluate_students.be_evaluate_stu_num
        response['list'] = json.loads(serializers.serialize("json", certifications))
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


# 按照名字搜索书（已测试）
@require_http_methods(["GET"])
def search_book(request):
    response = {}
    try:
        book=Book_Info.objects.all().filter(book_name__contains=request.GET.get('book_name'))
        # be_evaluate_num = be_evaluate_students.be_evaluate_stu_num
        response['list'] = json.loads(serializers.serialize("json", book))
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


# 按照名字搜索幕课（已测试）
@require_http_methods(["GET"])
def search_course(request):
    response = {}
    try:
        course=Course_Info.objects.all().filter(course_name__contains=request.GET.get('course_name'))
        # be_evaluate_num = be_evaluate_students.be_evaluate_stu_num
        response['list'] = json.loads(serializers.serialize("json", course))
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


# 按照名字搜索考证信息（已测试）
@require_http_methods(["GET"])
def search_certification(request):
    response = {}
    try:
        certification=Certification_Info.objects.all().filter(certification_name__contains=request.GET.get('certification_name'))
        # be_evaluate_num = be_evaluate_students.be_evaluate_stu_num
        response['list'] = json.loads(serializers.serialize("json", certification))
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


# 改
# 修改学生信息（已测试）
@require_http_methods(["GET"])
def change_user(request):
    response = {}
    try:
        User_Info.objects.all().filter(user_number=request.GET.get('user_number')).update(
            user_id = request.GET.get('user_id'),
            user_name = request.GET.get('user_name'),
            user_password = request.GET.get('user_password'),
            user_gender = request.GET.get('user_gender'),
            user_class = request.GET.get('user_class'),
        )

        response['msg'] = 'success'
        response['error_num'] = 0
        user = User_Info.objects.filter(user_number=request.GET.get('user_number'))
        response['list'] = json.loads(serializers.serialize("json", user))
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


# 修改毕业去向（已测试）
@require_http_methods(["GET"])
def change_destination(request):
    response = {}
    try:
        Graduation_Destination.objects.all().filter(user_number=request.GET.get('user_number')).update(
            destination_info = request.GET.get('destination_info'),
            user_name =request.GET.get('user_name'),
            user_email=request.GET.get('user_email'),
            type = request.GET.get('type')
        )

        response['msg'] = 'success'
        response['error_num'] = 0
        destination = Graduation_Destination.objects.filter(user_number=request.GET.get('user_number'))
        response['list'] = json.loads(serializers.serialize("json", destination))
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


# 修改书籍信息（已测试）
@require_http_methods(["GET"])
def change_book(request):
    response = {}
    try:
        Book_Info.objects.all().filter(book_id=request.GET.get('book_id')).update(
            book_name = request.GET.get('book_name'),
            author = request.GET.get('author'),
            publisher = request.GET.get('publisher'),
            introduction = request.GET.get('introduction'),
            publisher_email = request.GET.get('publisher_email'),
            type = request.GET.get('type')
        )
        response['msg'] = 'success'
        response['error_num'] = 0
        book = Book_Info.objects.filter(book_id=request.GET.get('book_id'))
        response['list'] = json.loads(serializers.serialize("json", book))
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


# 修改幕课信息（已测试）
@require_http_methods(["GET"])
def change_course(request):
    response = {}
    try:
        Course_Info.objects.all().filter(course_id=request.GET.get('course_id')).update(
            course_name = request.GET.get('course_name'),
            publisher = request.GET.get('publisher'),
            book = request.GET.get('book'),
            introduction = request.GET.get('introduction'),
            type=request.GET.get('type'),
            teacher=request.GET.get('teacher')
        )
        response['msg'] = 'success'
        response['error_num'] = 0
        course = Course_Info.objects.filter(course_id=request.GET.get('course_id'))
        response['list'] = json.loads(serializers.serialize("json", course))
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


# 修改考证信息（已测试）
@require_http_methods(["GET"])
def change_certification(request):
    response = {}
    try:
        Certification_Info.objects.all().filter(certification_id=request.GET.get('certification_id')).update(
            certification_name = request.GET.get('certification_name'),
            publisher = request.GET.get('publisher'),
            introduction = request.GET.get('introduction'),
            link = request.GET.get('link'),
            publisher_email = request.GET.get('publisher_email')
            # time = request.GET.get('time')
        )
        response['msg'] = 'success'
        response['error_num'] = 0
        certification = Certification_Info.objects.filter(certification_id=request.GET.get('certification_id'))
        response['list'] = json.loads(serializers.serialize("json", certification))
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


# 审核
# 审核毕业去向（已测试）
@require_http_methods(["GET"])
def check_destination(request):
    response = {}
    try:
        Graduation_Destination.objects.all().filter(user_number=request.GET.get('user_number')).update(
            ischeck = request.GET.get('ischeck')
        )
        destination = Graduation_Destination.objects.filter(user_number=request.GET.get('user_number'))
        response['list'] = json.loads(serializers.serialize("json", destination))
        response['msg'] = 'success'
        response['error_num'] = 0

    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


# 审核书籍信息（已测试）
@require_http_methods(["GET"])
def check_book(request):
    response = {}
    try:
        Book_Info.objects.all().filter(book_id=request.GET.get('book_id')).update(
            ischeck=request.GET.get('ischeck')
        )
        book = Book_Info.objects.filter(book_id=request.GET.get('book_id'))
        response['list'] = json.loads(serializers.serialize("json", book))
        response['msg'] = 'success'
        response['error_num'] = 0

    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


# 审核幕课信息（已测试）
@require_http_methods(["GET"])
def check_course(request):
    response = {}
    try:
        Course_Info.objects.all().filter(course_id=request.GET.get('course_id')).update(
            ischeck=request.GET.get('ischeck')
        )
        course = Course_Info.objects.filter(course_id=request.GET.get('course_id'))
        response['list'] = json.loads(serializers.serialize("json", course))
        response['msg'] = 'success'
        response['error_num'] = 0

    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


# 审核考证信息（已测试）
@require_http_methods(["GET"])
def check_certification(request):
    response = {}
    try:
        Certification_Info.objects.all().filter(certification_id=request.GET.get('certification_id')).update(
            ischeck=request.GET.get('ischeck')
        )
        certification = Certification_Info.objects.filter(certification_id=request.GET.get('certification_id'))
        response['list'] = json.loads(serializers.serialize("json", certification))
        response['msg'] = 'success'
        response['error_num'] = 0

    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)



@require_http_methods(["GET"])
def show_destination(request):
    response = {}
    try:
        destination=Graduation_Destination.objects.all().filter(ischeck="1")
        # be_evaluate_num = be_evaluate_students.be_evaluate_stu_num
        response['list'] = json.loads(serializers.serialize("json", destination))
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)

@require_http_methods(["GET"])
def show_book(request):
    response = {}
    try:
        book=Book_Info.objects.all().filter(ischeck="1")
        # be_evaluate_num = be_evaluate_students.be_evaluate_stu_num
        response['list'] = json.loads(serializers.serialize("json", book))
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)

@require_http_methods(["GET"])
def show_course(request):
    response = {}
    try:
        course=Course_Info.objects.all().filter(ischeck="1")
        # be_evaluate_num = be_evaluate_students.be_evaluate_stu_num
        response['list'] = json.loads(serializers.serialize("json", course))
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)

@require_http_methods(["GET"])
def show_certification(request):
    response = {}
    try:
        certification=Certification_Info.objects.all().filter(ischeck="1")
        # be_evaluate_num = be_evaluate_students.be_evaluate_stu_num
        response['list'] = json.loads(serializers.serialize("json", certification))
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)




