from django.apps import AppConfig
from pytlas.importers import import_skills
from pytlas.settings import getpath, SETTING_SKILLS

class AssistantConfig(AppConfig):
    name = 'assistant'

    def ready(self):
        import_skills(getpath(SETTING_SKILLS))
