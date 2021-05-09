
from __future__ import unicode_literals
from django.db import models
# Create your models here.
# -*- coding: utf-8 -*-



# Create your models here.

# 用户信息表
class User_Info(models.Model):
    user_number = models.CharField(max_length=64,primary_key=True)
    user_id = models.CharField(max_length=64)
    user_password = models.CharField(max_length=64)
    user_name = models.CharField(max_length=64)
    user_gender = models.CharField(max_length = 64)
    user_class = models.CharField(max_length =64)
    def __unicode__(self):
        return self.user_number

# 毕业去向表
class Graduation_Destination(models.Model):
    user_number = models.CharField(max_length = 64,primary_key=True)
    user_name = models.CharField(max_length=64)
    user_email = models.CharField(max_length=64,default="null")
    # destination_department = models.CharField(max_length=64,default="null")
    type=models.CharField(max_length=64,default="null")
    destination_info = models.CharField(max_length=64)
    ischeck = models.CharField(max_length=64)

    def __unicode__(self):
        return self.user_number

# 书籍信息
class Book_Info(models.Model):
    book_id = models.CharField(max_length = 64,primary_key = True)
    user_number = models.CharField(max_length=64,default="null")
    book_name = models.CharField(max_length=64)
    author = models.CharField(max_length=64)
    publisher = models.CharField(max_length=64)
    publisher_email = models.CharField(max_length=64,default="null")
    type=models.CharField(max_length=64,default="null")
    introduction=models.CharField(max_length=64,default="null")
    ischeck = models.CharField(max_length=64)
    def __unicode__(self):
        return self.book_id

# 幕课信息
class Course_Info(models.Model):
    course_id = models.CharField(max_length=64,primary_key=True)
    course_name = models.CharField(max_length=64)
    user_number = models.CharField(max_length=64, default="null")
    publisher = models.CharField(max_length=64)
    publisher_email = models.CharField(max_length=64,default="null")
    teacher = models.CharField(max_length=64,default="null")
    type = models.CharField(max_length=64,default="null")
    book = models.CharField(max_length=64,default="null")
    introduction = models.CharField(max_length=64)
    ischeck = models.CharField(max_length=64)

    def __unicode__(self):
        return self.course_id

# 考证信息
class Certification_Info(models.Model):
    certification_id = models.CharField(max_length=64,primary_key=True)
    certification_name = models.CharField(max_length=64)
    user_number = models.CharField(max_length=64, default="null")
    publisher = models.CharField(max_length=64)
    publisher_email = models.CharField(max_length=64,default="null")
    introduction = models.CharField(max_length=64)
    link = models.CharField(max_length=64,default="null")
    # time = models.DateTimeField(default=timezone.now())
    ischeck = models.CharField(max_length=64)
    def __unicode__(self):
        return self.certification_id
