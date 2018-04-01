#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/23 23:13
# @Author  : LiuShaoheng


from django.conf.urls import url

from users.views import UserInfoView, UploadImageView, SendEmailCodeView, UpdateEmailView, UpdatePwdView, MyCourseView, MyFavOrgView, MyFavTeacherView, MyFavCourseView, MyMessageView

app_name = "users"

urlpatterns = [

    # 用户信息
    url('info/', UserInfoView.as_view(), name="user_info"),
    # 用户头像上传
    url('image/upload/', UploadImageView.as_view(), name="image_upload"),
    # 用户个人中心修改密码
    url('update/pwd/', UpdatePwdView.as_view(), name="update_pwd"),
    # 专用于发送验证码的
    url('sendemail_code/', SendEmailCodeView.as_view(), name="sendemail_code"),

    url('update_email/', UpdateEmailView.as_view(), name="update_email"),
    # 用户中心我的课程
    url('mycourse/', MyCourseView.as_view(), name="mycourse"),
    # 我收藏的课程机构
    url('myfav/org/', MyFavOrgView.as_view(), name="myfav_org"),
    # 我收藏的授课讲师
    url('myfav/teacher/', MyFavTeacherView.as_view(), name="myfav_teacher"),
    # 我收藏的课程
    url('myfav/course/', MyFavCourseView.as_view(), name="myfav_course"),
    # 我的消息
    url('my_message/', MyMessageView.as_view(), name="my_message"),

]








