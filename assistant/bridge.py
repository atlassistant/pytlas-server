import logging
from pytlas import Agent
from pytlas.cli import CACHE_DIR
from pytlas.settings import CONFIG
from pytlas.understanding.snips import SnipsInterpreter

agents_by_user = {}

def get_agent_for_user(user):
  agent = agents_by_user.get(user.id)

  if not agent:
    logging.info('Agent does not exist for "%s", creating it' % user.id)

    interpreter = SnipsInterpreter(user.profile.language[:2], CONFIG.getpath(CACHE_DIR))
    interpreter.fit_from_skill_data()

    agent = Agent(interpreter, uid=user.id)

    agents_by_user[user.id] = agent
  else:
    logging.info('Agent found matching this user!')

  user_settings = user.setting_set.all()
  user_settings_dict = { setting.name: setting.value for setting in user_settings }

  # Update agent meta with user settings
  agent.meta.update(user_settings_dict)

  return agent
