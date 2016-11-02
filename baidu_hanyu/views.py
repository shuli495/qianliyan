# -*- coding: utf-8 -*-
from django.http import HttpResponse
from rest_framework.views import APIView
from baidu_hanyu.models import BaiduHanyu
import urllib
from bs4 import BeautifulSoup

class hanyu(APIView):

    def get(self, request, *args):
        # 汉字
        hz = args[0]

        # 查询库中数据
        hz_list = BaiduHanyu.objects.filter(hz=hz)

        return_pinyin = ""

        if len(hz_list) != 0:
            return_pinyin = hz_list[0].py
        else:
            try:
                # 使用百度汉语查询拼音
                url = "http://dict.baidu.com/s?wd=" + urllib.request.quote(hz)
                page_data = urllib.request.urlopen(url).read()

                # 解析拼音
                soup = BeautifulSoup(page_data.decode('UTF-8'), "html")
                return_pinyin = soup.find(id="pinyin").b.string.replace("[","").replace("]","")

                # 入库
                BaiduHanyu.objects.create(hz=hz, py=return_pinyin)
            except Exception:
                return_pinyin = ""

        return HttpResponse(return_pinyin)