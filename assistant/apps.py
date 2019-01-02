from django.apps import AppConfig
from pytlas.importers import import_skills
from pytlas.settings import getpath, getbool, SETTING_SKILLS, SETTING_VERBOSE, SETTING_DEBUG
from pytlas.cli.utils import install_logs

class AssistantConfig(AppConfig):
    name = 'assistant'

    def ready(self):
        install_logs(getbool(SETTING_VERBOSE), getbool(SETTING_DEBUG, section='web'))
        import_skills(getpath(SETTING_SKILLS))
