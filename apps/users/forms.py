#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/22 16:27
# @Author  : LiuShaoheng

import re
from django import forms
from captcha.fields import CaptchaField
from users.models import UserProfile


# 登录表单验证
class LoginForm(forms.Form):
    # 用户名
    username = forms.CharField(
        required=True,
        min_length=6,
        error_messages={
            'required': '用户名不能为空.',
            'min_length': "用户名长度不能小于6个字符",
        }
    )
    # 密码
    password = forms.CharField(
        min_length=6,
        error_messages={
            'required': '密码不能为空.',
            'min_length': "密码长度不能小于6个字符",
        }
    )


# 验证码form & 注册表单form
class RegisterForm(forms.Form):
    # 此处email与前端name需保持一致。
    email = forms.EmailField(
        required=True,
        min_length=6,
        max_length=20,
        error_messages={
            'required': '用户名或邮箱不能为空.',
            'min_length': "用户名长度不能小于6个字符",
            'max_length': "用户名长度不能大于20个字符"
        }
    )
    # 密码
    password = forms.RegexField(
        '^(?=.*[0-9])(?=.*[a-zA-Z])[0-9a-zA-Z]{6,20}$',
        required=True,
        min_length=6,
        max_length=20,
        error_messages={
            'required': '密码不能为空.',
            'invalid': '密码必须包含数字，字母',
            'min_length': "密码长度不能小于6个字符",
            'max_length': "密码长度不能大于20个字符"
        }
    )
    # 应用验证码 自定义错误输出key必须与异常一样
    captcha = CaptchaField(error_messages={"invalid": "验证码错误"})


# 激活时验证码实现
class ActiveForm(forms.Form):
    # 激活时不对邮箱密码做验证
    # 应用验证码 自定义错误输出key必须与异常一样
    captcha = CaptchaField(error_messages={"invalid": "验证码错误"})


# 忘记密码实现
class ForgetForm(forms.Form):
    # 此处email与前端name需保持一致。
    email = forms.EmailField(required=True)
    # 应用验证码 自定义错误输出key必须与异常一样
    captcha = CaptchaField(error_messages={"invalid": "验证码错误"})


# 重置密码form实现
class ModifyPwdForm(forms.Form):
    # 密码不能小于6位
    password1 = forms.RegexField(
        '^(?=.*[0-9])(?=.*[a-zA-Z])[0-9a-zA-Z]{6,20}$',
        required=True,
        min_length=6,
        max_length=20,
        error_messages={
            'required': '密码不能为空.',
            'invalid': '密码必须包含数字，字母',
            'min_length': "密码长度不能小于6个字符",
            'max_length': "密码长度不能大于20个字符"
        }
    )
    # 密码不能小于6位
    password2 = forms.CharField(required=True, min_length=6)


# 用于文件上传，修改头像
class UploadImageForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ['image']


# 用于个人中心修改个人信息
class UserInfoForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ['nick_name', 'gender', 'birthday', 'address', 'mobile']

    def clean_mobile(self):
        mobile = self.cleaned_data['mobile']
        REGEX_MOBILE = '^1([358][0-9]|4[579]|66|7[0135678]|9[89])[0-9]{8}$'
        p = re.compile(REGEX_MOBILE)
        if p.match(mobile):
            return mobile
        else:
            raise forms.ValidationError("手机号码非法", code="mobile_invalid")









