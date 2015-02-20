import os

from django.core.management import execute_from_command_line
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings


class Command(BaseCommand):
    args = ''
    help = 'Touches BASE_DIR/custom_collectstatic and then runs collectstatic'

    def handle(self, *args, **options):
        loc = os.path.join(settings.BASE_DIR, 'custom_collectstatic')
        with open(loc, 'w') as f:
            f.write('')

        execute_from_command_line(['manage.py', 'collectstatic', '--noinput'])
