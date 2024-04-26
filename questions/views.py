# views.py
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from http import HTTPStatus
import json
import requests  # 如果需要发送HTTP请求
import dashscope


# dashscope.api_key = 'sk-9309a81d693947f394635eb7196a78b7'

#
# @csrf_exempt
# def question_view(request):
#     if request.method == "POST":
#         data = json.loads(request.body)
#         question = data.get('question', '')
#         # 调用函数获取文本回答
#         answer_text = call_with_prompt(question)
#         # 返回JSON响应
#         return JsonResponse({'answer': answer_text})
#     else:
#         return render(request, 'questions/index.html')
#
#
# def call_with_prompt(text):
#     try:
#         response = dashscope.Generation.call(
#             model=dashscope.Generation.Models.qwen_max,
#             prompt=text
#         )
#         # 确保响应中存在所需的数据
#         return response.output.text if response.output and hasattr(response.output, 'text') else 'No response text available.'
#     except Exception as e:
#         print("Error during API call:", e)
#         return 'Error fetching response'
# from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def question_view(request):
    # views.py
    """渲染包含 WebSocket 客户端逻辑的主页面。"""
    return render(request, 'questions/index.html')
