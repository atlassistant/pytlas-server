from channels.generic.websocket import WebsocketConsumer
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework_simplejwt.settings import api_settings
from django.contrib.auth.models import User
from . import bridge
import json

class AssistantConsumer(WebsocketConsumer):
  """Assistant consumer which require an authentication in the form of a first
  authenticate message type with the user token.
  """

  def connect(self):
    self.accept()
    self.agent = None
    self.user = None

    usr = self.scope["user"]

    if usr and not usr.is_anonymous:
      self.user = usr

    self.create_agent()

  def disconnect(self, code):
    pass

  def create_agent(self):
    if not self.user:
      return

    self.agent = bridge.get_agent_for_user(self.user)
    self.agent.model = self

    self.send(text_data=json.dumps({
      'type': 'ready',
      'lang': self.agent._interpreter.lang,
    }))

  def on_answer(self, text, cards, **meta):
    meta.update({
      'text': text,
      'cards': [c.__dict__ for c in cards] if cards else None,
    })

    self.send(text_data=json.dumps({
      'type': 'answer',
      'data': meta,
    }))

  def on_ask(self, slot, text, choices, **meta):
    meta.update({
      'slot': slot,
      'text': text,
    })

    self.send(text_data=json.dumps({
      'type': 'ask',
      'data': meta,
    }))

  def on_done(self, require_input):
    self.send(text_data=json.dumps({
      'type': 'done',
      'require_input': require_input,
    }))

  def on_thinking(self):
    self.send(text_data=json.dumps({
      'type': 'thinking',
    }))

  def on_context(self, name):
    self.send(text_data=json.dumps({
      'type': 'context',
      'name': name,
    }))

  def receive(self, text_data):
    try:
      data = json.loads(text_data)
      data_type = data.get('type')

      if self.user:
        self.agent.parse(data.get('message'))
      else:
        if data_type != 'authenticate':
          raise Exception('Expected message type authenticate')
        else:
          token = AccessToken(data.get('token'))
          self.user = User.objects.get(id=token[api_settings.USER_ID_CLAIM])
          self.create_agent()
    except:
      self.close()

