import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
from .models import Post

class ForumConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add("forum", self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("forum", self.channel_name)

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        await self.channel_layer.group_send(
            "forum",
            {
                'type': 'forum_message',
                'message': message
            }
        )

    async def forum_message(self, event):
        message = event['message']
        await self.send(text_data=json.dumps({
            'message': message
        }))
