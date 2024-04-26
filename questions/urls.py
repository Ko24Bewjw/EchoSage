# -*- coding: utf-8 -*-
# @Time : 09:19 2024/4/20
# @Author : Allen-wan
# @File : urls.py
# @Software : PyCharm
from django.urls import path
from .views import question_view

urlpatterns = [
    path('', question_view, name='question'),
]
