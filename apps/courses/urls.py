#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/23 23:15
# @Author  : LiuShaoheng

from courses.views import CourseListView, CourseDetailView, CourseInfoView, CommentsView, AddCommentsView, VideoPlayView
from django.conf.urls import url


app_name = "courses"

urlpatterns = [

    # 课程列表url
    url(r'list/', CourseListView.as_view(), name="list"),
    # 课程详情页
    url(r'detail/(?P<course_id>\d+)/', CourseDetailView.as_view(), name="course_detail"),
    # 课程章节信息页
    url(r'info/(?P<course_id>\d+)/', CourseInfoView.as_view(), name="course_info"),
    # 课程章节信息页
    url(r'comments/(?P<course_id>\d+)/', CommentsView.as_view(), name="course_comments"),
    # 添加课程评论,已经把参数放到post当中了
    url(r'add_comment/', AddCommentsView.as_view(), name="add_comment"),
    # 课程视频播放页
    url(r'video/(?P<video_id>\d+)/', VideoPlayView.as_view(), name="video_play"),

]




































