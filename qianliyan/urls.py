# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.contrib import admin
from baidu_hanyu.views import hanyu

project = "qianliyan/"

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    # 百度汉语
    url(r'^'+project+'baidu/hanyu/(.+)$', hanyu.as_view()),
]
