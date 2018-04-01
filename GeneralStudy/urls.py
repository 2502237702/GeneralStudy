"""GeneralStudy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.static import serve
from django.views.generic import TemplateView
from users import views as v
from GeneralStudy.settings import MEDIA_ROOT
import xadmin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^xadmin/', xadmin.site.urls),

    url(r'^$', v.IndexView.as_view(), name='index'),
    url(r'^login/$', v.LoginView.as_view(), name='login'),
    url(r'^logout/$', v.LogoutView.as_view(), name='logout'),
    url(r'^register/$', v.RegisterView.as_view(), name='register'),
    url(r"^captcha/", include('captcha.urls')),
    url(r'^active/(?P<active_code>.*)/', v.ActiveUserView.as_view(), name="user_active"),
    url(r'^forget/', v.ForgetPwdView.as_view(), name="forget_pwd"),
    url(r'^reset/(?P<active_code>.*)/', v.ResetView.as_view(), name="reset_pwd"),
    url(r'^modify_pwd/', v.ModifyPwdView.as_view(), name="modify_pwd"),

    url(r"^org/", include('organization.urls', namespace='org')),

    url(r'media/(?P<path>.*)', serve, {"document_root": MEDIA_ROOT}),

    # url(r'^static/(?P<path>.*)', serve, {"document_root": STATIC_ROOT}),

    url(r"^course/", include('courses.urls', namespace="course")),

    url(r"^users/", include('users.urls', namespace="users")),

    url(r'^ueditor/', include('DjangoUeditor.urls')),

]


# 全局404:
# handler404 = 'users.views.page_not_found'






