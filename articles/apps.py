# articles/apps.py
from django.apps import AppConfig
import os

class ArticlesConfig(AppConfig):
    name = 'articles'

    def ready(self):
        if os.environ.get('RUN_MAIN', None) != 'true':
            from django.core.management import call_command
            call_command('fetch_stock_data')