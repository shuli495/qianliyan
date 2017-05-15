# -*- coding: utf-8 -*-
from django.db import models

class baiduHanyu(models.Model):

    hz = models.CharField(primary_key=True,max_length=32, verbose_name="汉字")
    py = models.CharField(max_length=32, verbose_name="拼音")

    class Meta:
        verbose_name = '百度汉语'
        db_table = 'baidu_hanyu'
