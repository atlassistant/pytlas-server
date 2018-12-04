from channels.generic.websocket import WebsocketConsumer
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework_simplejwt.settings import api_settings
from django.contrib.auth.models import User
import json

class AssistantConsumer(WebsocketConsumer):
  """Assistant consumer which require an authentication in the form of a first
  authenticate message type with the user token.
  """

  def connect(self):
    self.accept()
    self.user = None

  def disconnect(self, code):
    pass

  def receive(self, text_data):
    try:
      data = json.loads(text_data)
      data_type = data.get('type')

      if self.user:
        self.send(text_data=json.dumps({
          'type': 'message',
          'message': data.get('message'),
        }))
      else:
        if data_type != 'authenticate':
          raise Exception('Expected message type authenticate')
        else:
          token = AccessToken(data.get('token'))
          self.user = User.objects.get(id=token[api_settings.USER_ID_CLAIM])
    except:
      self.close()

