# yourapp/management/commands/create_default_user.py
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Creates a default Django user'

    def handle(self, *args, **kwargs):
        if not User.objects.filter(username='watchdxg').exists():
            User.objects.create_user(username='watchdxg', password='watchdxg')
            self.stdout.write(self.style.SUCCESS('Default user created.'))
        else:
            self.stdout.write('User already exists.')
