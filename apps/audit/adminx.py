#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/1 10:45
# @Author  : LiuShaoheng


import xadmin
from .models import Flow, FlowBecome_Full_Staff, FlowLoan, FlowRecord, FlowRole, FlowTemplate, FlowTrip, FlowVaction, Step


class StepAdmin(object):
    list_display = ['flow_template', 'name', 'order', 'role']
    list_filter = ['flow_template', ]


class FlowRecordAdmin(object):
    list_display = ['flow', 'step', 'user', 'status', 'date', 'comment']
    list_filter = ['flow', 'status']


xadmin.site.register(Flow)
xadmin.site.register(FlowVaction)
xadmin.site.register(FlowTrip)
xadmin.site.register(FlowLoan)
xadmin.site.register(FlowBecome_Full_Staff)
xadmin.site.register(FlowTemplate)
xadmin.site.register(FlowRole)
xadmin.site.register(FlowRecord, FlowRecordAdmin)
xadmin.site.register(Step, StepAdmin)












