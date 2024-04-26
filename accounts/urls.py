# -*- coding: utf-8 -*-
# @Time : 19:20 2024/4/22
# @Author : Allen-wan
# @File : urls.py
# @Software : PyCharm
from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import MyLoginView
from .views import signup

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', MyLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
]
