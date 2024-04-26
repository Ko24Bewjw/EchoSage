# -*- coding: utf-8 -*-
# @Time : 10:44 2024/4/20
# @Author : Allen-wan
# @File : routing.py
# @Software : PyCharm
from django.urls import path
from .consumers import QuestionConsumer

websocket_urlpatterns = [
    path('ws/questions/', QuestionConsumer.as_asgi()),
]
