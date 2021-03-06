#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/22 12:15
# @Author  : LiuShaoheng


import xadmin
from xadmin import views
from xadmin.models import Log
from django.contrib.auth.models import Group, Permission
from users.models import EmailVerifyRecord, Banner, UserProfile
from courses.models import Course, CourseResource, Lesson, Video, BannerCourse
from operation.models import UserFavorite, UserAsk, UserCourse, UserMessage, CourseComments
from organization.models import CityDict, CourseOrg, Teacher
from audit.models import FlowBecome_Full_Staff, FlowLoan, FlowRecord, FlowRole, FlowTemplate, FlowTrip, FlowVaction, Flow, Step


# X admin的全局配置信息设置
class BaseSetting(object):
    # 主题功能开启
    enable_themes = True
    use_bootswatch = True


# x admin 全局配置参数信息设置
class GlobalSettings(object):
    site_title = "后台管理系统"
    site_footer = "梦游的木头2018个人学习开发"
    # 收起菜单
    menu_style = "accordion"

    def get_site_menu(self):
        return (
            {'title': '机构管理', 'icon': 'fa fa-bars', 'menus': (
                {'title': '所在城市', 'url': self.get_model_url(CityDict, 'changelist')},
                {'title': '机构信息', 'url': self.get_model_url(CourseOrg, 'changelist')},
                {'title': '机构讲师', 'url': self.get_model_url(Teacher, 'changelist')},
            )},

            {'title': '课程管理', 'icon': 'fa fa-film', 'menus': (
                {'title': '课程信息', 'url': self.get_model_url(Course, 'changelist')},
                {'title': '轮播课程', 'url': self.get_model_url(BannerCourse, 'changelist')},
                {'title': '章节信息', 'url': self.get_model_url(Lesson, 'changelist')},
                {'title': '视频信息', 'url': self.get_model_url(Video, 'changelist')},
                {'title': '课程资源', 'url': self.get_model_url(CourseResource, 'changelist')},
                {'title': '课程评论', 'url': self.get_model_url(CourseComments, 'changelist')},
            )},

            {'title': '用户管理', 'icon': 'fa fa-users', 'menus': (
                {'title': '用户信息', 'url': self.get_model_url(UserProfile, 'changelist')},
                {'title': '用户验证', 'url': self.get_model_url(EmailVerifyRecord, 'changelist')},
                {'title': '用户课程', 'url': self.get_model_url(UserCourse, 'changelist')},
                {'title': '用户收藏', 'url': self.get_model_url(UserFavorite, 'changelist')},
                {'title': '用户消息', 'url': self.get_model_url(UserMessage, 'changelist')},
            )},

            {'title': '系统管理', 'icon': 'fa fa-cogs', 'menus': (
                {'title': '用户咨询', 'url': self.get_model_url(UserAsk, 'changelist')},
                {'title': '首页轮播', 'url': self.get_model_url(Banner, 'changelist')},
                {'title': '用户分组', 'url': self.get_model_url(Group, 'changelist')},
                {'title': '用户权限', 'url': self.get_model_url(Permission, 'changelist')},
                {'title': '日志记录', 'url': self.get_model_url(Log, 'changelist')},
            )},

            {'title': '审批管理', 'icon': 'fa fa-fire', 'menus': (
                {'title': '流程总表', 'url': self.get_model_url(Flow, 'changelist')},
                {'title': '请假流程', 'url': self.get_model_url(FlowVaction, 'changelist')},
                {'title': '出差流程', 'url': self.get_model_url(FlowTrip, 'changelist')},
                {'title': '借款申请', 'url': self.get_model_url(FlowLoan, 'changelist')},
                {'title': '转正流程', 'url': self.get_model_url(FlowBecome_Full_Staff, 'changelist')},
                {'title': '流程模版', 'url': self.get_model_url(FlowTemplate, 'changelist')},
                {'title': '流程角色', 'url': self.get_model_url(FlowRole, 'changelist')},
                {'title': '流程流转记录', 'url': self.get_model_url(FlowRecord, 'changelist')},
                {'title': '流程环节', 'url': self.get_model_url(Step, 'changelist')},
            )},
        )


# 创建admin的管理类,这里不再是继承admin，而是继承object
class EmailVerifyRecordAdmin(object):
    # 配置后台我们需要显示的列
    list_display = ['code', 'email', 'send_type', 'send_time']
    # 配置搜索字段,不做时间搜索
    search_fields = ['code', 'email', 'send_type']
    # 配置筛选字段
    list_filter = ['code', 'email', 'send_type', 'send_time']


# 创建banner的管理类
class BannerAdmin(object):
    list_display = ['title', 'image', 'url', 'index', 'add_time']
    search_fields = ['title', 'image', 'url', 'index']
    list_filter = ['title', 'image', 'url', 'index', 'add_time']


xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(Banner, BannerAdmin)

xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)














