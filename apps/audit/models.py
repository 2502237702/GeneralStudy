from django.db import models
from users import models as user_models


class FlowTemplate(models.Model):
    """流程模版"""
    name = models.CharField(max_length=128, unique=True, verbose_name='申请人')
    description = models.TextField(blank=True, null=True, verbose_name='申请描述')
    flow_type_choices = (('FlowVaction', '请假流程'),
                         ('FlowTrip', '出差申请'),
                         ('FlowBecome_Full_Staff', '转正申请'),
                         ('FlowLoan', '借款申请'),
                         )
    flow_type = models.CharField(choices=flow_type_choices, max_length=64, verbose_name='申请类型')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = '流程模版'
        verbose_name = '流程模版'


class Flow(models.Model):
    """流程总表，存储所有流程都会有的公共信息"""
    template = models.ForeignKey(FlowTemplate, on_delete=models.CASCADE, verbose_name='模板')
    started_user = models.ForeignKey(user_models.UserProfile, verbose_name="流程发起人", on_delete=models.CASCADE)
    content = models.TextField(blank=True, null=True, verbose_name="申请内容")
    in_queue = models.BooleanField(default=True, help_text="只要任务没被人处理，就会一直在queue中")

    date = models.DateTimeField(auto_created=True, auto_now=True, verbose_name='申请时间')

    def __str__(self):
        return "%s 发起人:%s" % (self.template, self.started_user)

    class Meta:
        verbose_name_plural = '流程总表'
        verbose_name = '流程总表'


class FlowTrip(models.Model):
    """出差流程"""
    flow = models.ForeignKey("Flow", on_delete=models.CASCADE, verbose_name='跟进')
    start_date = models.DateTimeField("开始时间")
    end_date = models.DateTimeField("结束时间")

    class Meta:
        verbose_name_plural = '出差流程'
        verbose_name = '出差流程'


class FlowLoan(models.Model):
    """借款申请"""
    flow = models.ForeignKey("Flow", on_delete=models.CASCADE, verbose_name='跟进')
    usage_choices = ((0, '出差借款'),)
    usage = models.SmallIntegerField(choices=usage_choices, verbose_name="用途")
    amount = models.PositiveIntegerField("借款金额")
    start_date = models.DateTimeField("用款时间")
    end_date = models.DateTimeField("还款时间")

    class Meta:
        verbose_name_plural = '借款申请'
        verbose_name = '借款申请'


class FlowBecome_Full_Staff(models.Model):
    """转正流程"""
    flow = models.ForeignKey("Flow", on_delete=models.CASCADE, verbose_name='跟进')
    probation_start_date = models.DateField("入职日期")
    probation_end_date = models.DateField("转正日期")

    class Meta:
        verbose_name_plural = '转正流程'
        verbose_name = '转正流程'


class FlowVaction(models.Model):
    """请假流程"""
    flow = models.ForeignKey("Flow", on_delete=models.CASCADE, verbose_name='跟进')
    vaction_type_choices = ((0, '病假'), (1, '年假'), (2, '事假'), (3, '产假'))
    vaction_type = models.SmallIntegerField(choices=vaction_type_choices, default=2, verbose_name='请假事由')
    start_date = models.DateTimeField("开始时间")
    end_date = models.DateTimeField("结束时间")

    def __str__(self):
        return "%s: %s" % (self.flow, self.vaction_type)

    class Meta:
        verbose_name_plural = '请假流程'
        verbose_name = '请假流程'


class Step(models.Model):
    """流程的每个环节"""
    flow_template = models.ForeignKey("FlowTemplate", verbose_name="所属流程", on_delete=models.CASCADE)
    name = models.CharField("环节名称", max_length=128)
    description = models.TextField("环节介绍", blank=True, null=True)
    order = models.PositiveSmallIntegerField("环节步骤")
    role = models.ForeignKey("FlowRole", verbose_name="审批角色", on_delete=models.CASCADE)
    is_countersign = models.BooleanField("会签环节", default=False)
    required_polls = models.PositiveSmallIntegerField("会签最少需同意的人数", blank=True, null=True)

    def __str__(self):
        return "流程:%s 名称:%s 环节:%s" % (self.flow_template, self.name, self.order)

    class Meta:
        unique_together = ("flow_template", 'order')
        verbose_name_plural = '流程环节'
        verbose_name = '流程环节'


class FlowRecord(models.Model):
    """流程的流转记录"""
    flow = models.ForeignKey("Flow", default=1, on_delete=models.CASCADE, verbose_name='跟进')
    step = models.ForeignKey("Step", on_delete=models.CASCADE, verbose_name='步骤')
    user = models.ForeignKey(user_models.UserProfile, verbose_name="审批用户", blank=True, null=True, on_delete=models.SET_NULL)
    status_choices = ((0, '同意'), (1, '拒绝'), (2, '需额外审批人审批'), (3, '待处理'))
    status = models.SmallIntegerField(choices=status_choices, verbose_name="审批状态")
    comment = models.TextField(max_length=1024, verbose_name="审批意见")
    extra_parties = models.ManyToManyField(user_models.UserProfile, verbose_name="额外审批人列表",
                                           related_name="related_parties",
                                           blank=True)
    date = models.DateTimeField(auto_now_add=True, verbose_name='时间')

    def __str__(self):
        return "%s:%s" % (self.step, self.get_status_display())

    class Meta:
        verbose_name_plural = '流程流转记录'
        verbose_name = '流程流转记录'


class FlowRole(models.Model):
    """流程角色"""
    name = models.CharField(max_length=64, unique=True, verbose_name='姓名')
    users = models.ManyToManyField(user_models.UserProfile, blank=True, verbose_name='用户')
    is_dynamic_role = models.BooleanField(default=False, verbose_name='是否高级用户')
    role_lookup_func = models.CharField("查找动态role的函数", max_length=64, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = '流程角色'
        verbose_name = '流程角色'






