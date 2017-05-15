# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.contrib import admin
from baidu_hanyu.views import hanyu
from pinyin.views import pinyin

project = "qianliyan/"

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    # 百度汉语
    url(r'^'+project+'baidu/hanyu/(.+)$', hanyu.as_view()),

    # 汉字转拼音
    url(r'^'+project+'pinyin/(.+)$', pinyin.as_view()),

]
