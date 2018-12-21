import logging
from pytlas import Agent, settings
from pytlas.interpreters.snips import SnipsInterpreter

agents_by_user = {}

def _instantiate_agent(user):
  interpreter = SnipsInterpreter(settings.get(settings.SETTING_LANG), settings.getpath(settings.SETTING_CACHE))
  interpreter.fit_from_skill_data()

  return Agent(interpreter, uid=user.id)

def get_agent_for_user(user):
  agent = agents_by_user.get(user.id)

  if not agent:
    logging.info('Agent does not exist for "%s", creating it' % user.id)
    agent = _instantiate_agent(user)

    agents_by_user[user.id] = agent

  return agent
