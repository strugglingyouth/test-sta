#!/usr/bin/env python
#coding:utf-8

import sys
reload(sys)
sys.setdefaultencoding('utf-8')


from django import forms
from .models import Comments,Enroll

class CommentsForm(forms.ModelForm):
    """
        评论表单
    """
    class Meta:
        """
            指定一些 Meta 选项以改变 form 被渲染后的样式
        """
        model = Comments 
        
        fields = ['user_name', 'user_email', 'user_phone', 'user_grade', 'user_messages']

        widgets = {
            # 为要渲染的字段添加 css 样式
            # 例如 user_name 渲染后的html组件如下：
            # <input type="text" class="form-control" placeholder="Username" aria-describedby="sizing-addon1">

            'user_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': "请输入姓名",
                'aria-describedby': "sizing-addonl",
                'onblur': "identify1()",
                'id': 'name'
            }),
            'user_email': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '请输入邮箱',
                'aria-describedby': 'sizing-addonl',
                'onblur': "identify2()",
                'id': 'email'
            }),
            'user_phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '请输入电话',
                'aria-describedby': 'sizing-addonl',
                'onblur': "identify3()",
                'id': 'phone'
            }),
            'user_grade': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '年级',
                'aria-describedby': 'sizing-addonl',
                'onblur': "identify4()",
                'id': 'class'
            }),
            'user_messages': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': '说点什么吧...',
                'id': 'message',
                'style': 'height:290px'
            }),
        }
class EnrollForm(forms.ModelForm):
    """
        报名表单
    """
    class Meta:
        """
            指定一些 Meta 选项以改变 form 被渲染后的样式
        """
        model = Enroll
        
        fields = ['user_number','user_name', 'user_email', 'user_phone', 'user_grade', 'user_messages']

        widgets = {
            # 为要渲染的字段添加 css 样式
            # 例如 user_name 渲染后的html组件如下：
            # <input type="text" class="form-control" placeholder="Username" aria-describedby="sizing-addon1">

            'user_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': "请输入学号",
                'aria-describedby': "sizing-addonl",
                'onblur': "identify1()",
                'id': 'name'
            }),
            'user_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': "请输入昵称",
                'aria-describedby': "sizing-addonl",
                'onblur': "identify1()",
                'id': 'name'
            }),
            'user_email': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '请输入邮箱',
                'aria-describedby': 'sizing-addonl',
                'onblur': "identify2()",
                'id': 'email'
            }),
            'user_phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '请输入电话',
                'aria-describedby': 'sizing-addonl',
                'onblur': "identify3()",
                'id': 'phone'
            }),
            'user_grade': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '年级',
                'aria-describedby': 'sizing-addonl',
                'onblur': "identify4()",
                'id': 'class'
            }),
            'user_messages': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': '说点什么吧...',
                'id': 'message',
                'style': 'height:290px'
            }),
        }
