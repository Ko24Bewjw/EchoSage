# -*- coding: utf-8 -*-
# @Time : 12:15 2024/4/20
# @Author : Allen-wan
# @File : routing.py
# @Software : PyCharm
# -*- coding: utf-8 -*-
# @Time : 10:44 2024/4/20
# @Author : Allen-wan
# @File : routing.py
# @Software : PyCharm
from django.urls import path
from .questions.consumers import QuestionConsumer

websocket_urlpatterns = [
    path('/ws/questions/', QuestionConsumer.as_asgi()),
]
