import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import country
from channels.db import database_sync_to_async

@database_sync_to_async
def save_message(message):
    c = country(**message)
    c.save()

class AddConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = "dash"
        self.room_group_name = "dash"
        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )


       # Normal

        #let's start playing:

    # Receive message from WebSocket 
    # websocket here represents websocket connection on client "javascript"
    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        
        await save_message(message)
        
        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'new_message',
                'message': message
            }
        )

    # Receive message from room group
    async def new_message(self, event):
        message = event['message']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))
    


class DashConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = "dash"
        self.room_group_name = "dash"

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )



    #   # Receive message from room group
    async def new_message(self, event):
        message = event['message']
        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))