# -*- coding: utf-8 -*-
# @Time : 17:24 2024/4/22
# @Author : Allen-wan
# @File : urls.py
# @Software : PyCharm
from django.urls import path
from .views import file_upload_view, cancel_task_view, task_status_view


urlpatterns = [
    path('', file_upload_view, name='file_upload_view'),
    path('cancel_task/<int:task_id>/', cancel_task_view, name='cancel_task_view'),
    path('status/<str:task_id>/', task_status_view, name='task_status'),  # 新增状态检查路由
]
