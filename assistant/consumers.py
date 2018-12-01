from channels.generic.websocket import WebsocketConsumer
import json

class AssistantConsumer(WebsocketConsumer):

  def connect(self):
    self.accept()

  def disconnect(self, code):
    pass

  def receive(self, text_data):
    data = json.loads(text_data)

    self.send(text_data=json.dumps({
      'message': data['message'],
    }))
