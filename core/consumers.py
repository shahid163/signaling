from channels.generic.websocket import WebsocketConsumer
import json

class MyConsumer(WebsocketConsumer):

    def connect(self):
        print('came here');
        self.accept()

        self.send(text_data=json.dumps({
            'status': 'connected'
        }))
