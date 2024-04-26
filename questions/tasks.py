# -*- coding: utf-8 -*-
# @Time : 10:23 2024/4/20
# @Author : Allen-wan
# @File : tasks.py
# @Software : PyCharm
# questions/tasks.py
from celery import shared_task
import dashscope

dashscope.api_key = 'sk-9309a81d693947f394635eb7196a78b7'

@shared_task
def fetch_answer(question):
    try:
        response = dashscope.Generation.call(
            model=dashscope.Generation.Models.qwen_max,
            prompt=question
        )
        # 确保响应中存在所需的数据
        print(response.output.text)
        return response.output.text if response.output and hasattr(response.output, 'text') else 'No response text available.'
    except Exception as e:
        return 'Error fetching response'

