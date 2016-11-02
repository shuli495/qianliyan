# -*- coding: utf-8 -*-
from django.http import HttpResponse
from rest_framework.views import APIView
from baidu_hanyu.models import BaiduHanyu
import urllib
from bs4 import BeautifulSoup
import pytesseract
from PIL import Image

class yanzhengma(APIView):

    def get(self, request, *args):
        image = Image.open('vcode.png')

        vcode = pytesseract.image_to_string(image)

        print(vcode)