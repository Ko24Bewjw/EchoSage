from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
import json
import dashscope

dashscope.api_key = 'sk-9309a81d693947f394635eb7196a78b7'

class QuestionConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        question = text_data_json.get('question', 'No question received')

        # 调用同步方法获取答案，使用 database_sync_to_async 来处理同步函数调用
        response = await self.get_response(question)

        # 发送响应回 WebSocket 客户端
        await self.send(text_data=json.dumps({'answer': response}))

    async def disconnect(self, close_code):
        # 处理断开连接
        pass

    @database_sync_to_async
    def get_response(self, text):
        # 假设这是你的同步方法调用
        response = dashscope.Generation.call(
            model=dashscope.Generation.Models.qwen_max,
            prompt=text
        )
        # 返回处理后的文本
        return response.output.text if response.output and hasattr(response.output,
                                                                   'text') else 'No response text available.'
