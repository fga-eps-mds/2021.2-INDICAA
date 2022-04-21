from django.apps import AppConfig
import sys

class IndicaaApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'
    def ready(self):
        if "runserver" in sys.argv:
            from scraping.QtdeAlunosMatriculados import main
            main()