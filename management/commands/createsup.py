from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

from conf import settings

class Command(BaseCommand):

    def handle(self, *args, **options):
        if not User.objects.filter(username="JasonMize").exists():
            User.objects.create_superuser("JasonMize", "jasonemize@gmail.com", settings.SUPER_USER_PASS)