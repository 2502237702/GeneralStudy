#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/23 20:15
# @Author  : LiuShaoheng

import re
from django import forms
from operation.models import UserAsk


# 进阶版本的modelform：它可以向model一样save
class UserAskForm(forms.ModelForm):

    class Meta:
        model = UserAsk
        fields = ['name', 'mobile', 'course_name']

    # 手机号的正则表达式验证
    def clean_mobile(self):
        mobile = self.cleaned_data['mobile']
        REGEX_MOBILE = '^1([358][0-9]|4[579]|66|7[0135678]|9[89])[0-9]{8}$'
        p = re.compile(REGEX_MOBILE)
        if p.match(mobile):
            return mobile
        else:
            raise forms.ValidationError("手机号码非法", code="mobile_invalid")














