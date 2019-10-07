from django.apps import AppConfig
from pytlas.cli import VERBOSE, DEBUG, SKILLS_DIR
from pytlas.handling.importers import import_skills
from pytlas.settings import CONFIG
from pytlas.cli.utils import install_logs

class AssistantConfig(AppConfig):
    name = 'assistant'

    def ready(self):
        install_logs(CONFIG.getbool(VERBOSE), CONFIG.getbool(DEBUG, section='web'))
        import_skills(CONFIG.getpath(SKILLS_DIR))
