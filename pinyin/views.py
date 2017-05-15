# -*- coding: utf-8 -*-
from django.http import HttpResponse
from rest_framework.views import APIView

class pinyin(APIView):

    def get(self, request, *args):
        # 汉字
        hz = args[0]

        word_dict = {}

        with open('word.data') as f_obj:
            for f_line in f_obj.readlines():
                try:
                    line = f_line.split(':')
                    word_dict[line[0]] = line[1]
                except:
                    line = f_line.split('@')

        result = []
        for char in hz:
            key = '%X' % ord(char)
            if not word_dict.get(key):
                result.append(char)
            else:
                result.append(word_dict.get(key, char).split()[0][:-1].lower())

        return HttpResponse(result)