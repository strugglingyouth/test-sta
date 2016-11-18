#!/usr/bin/env python
#coding:utf-8

import sys
reload(sys)
sys.setdefaultencoding('utf-8')


from django.db import models

class Comments(models.Model):
    """
        留言信息
    """
    user_name = models.CharField("评论者姓名",max_length=20)
    user_email = models.CharField("邮箱",max_length=100)
    user_phone = models.CharField("电话",max_length=20)
    user_grade = models.CharField("年级",max_length=30)
    user_messages = models.CharField("留言",max_length=255)
    created_time = models.DateTimeField("发表评论时间",auto_now_add=True)

    def __str__(self):
        return self.user_name
    def __unicode__(self):
        return self.user_name

class Enroll(models.Model):
    """
        报名表
    """
    user_number = models.CharField("学号",max_length=20)
    user_name = models.CharField("评论者姓名",max_length=20)
    user_email = models.CharField("邮箱",max_length=100)
    user_grade = models.CharField("年级",max_length=30)
    user_phone = models.CharField("电话",max_length=20)
    user_messages = models.CharField("留言",max_length=255)
    created_time = models.DateTimeField("发表评论时间",auto_now_add=True)





