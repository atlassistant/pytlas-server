from channels.generic.websocket import WebsocketConsumer
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework_simplejwt.settings import api_settings
import json

class AssistantConsumer(WebsocketConsumer):

  def connect(self):
    self.accept()
    self._authenticated = False

  def disconnect(self, code):
    pass

  def receive(self, text_data):
    data = json.loads(text_data)

    if self._authenticated:
      self.send(text_data=json.dumps({
        'message': data['message'],
      }))
    elif data.get('type') == 'authenticate':
      try:
        token = AccessToken(data.get('token'))
        print ('Authenticated user id', token[api_settings.USER_ID_CLAIM])
        self._authenticated = True
      except Exception as e:
        print (e)
        self.close()

