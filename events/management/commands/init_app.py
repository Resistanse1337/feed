from random import choice

from django.conf import settings
from django.core.files import File
from django.core.management.base import BaseCommand

from achievements.models import Achievement
from ads.models import Ad
from notes.models import Note
from users.models import User


class Command(BaseCommand):
    help = 'The Zen of Python'

    def handle(self, *args, **options):
        users = [
            User.objects.create(first_name="user1", last_name="lastname1"),
            User.objects.create(first_name="user2", last_name="lastname2")
        ]

        reasons = ["register", "topup", "invite friend"]
        titles = ["book", "table", "phone", "note", "achievements", "ads"]

        achievements = [
            Achievement(
                user=choice(users), 
                reason=choice(reasons),
                title=choice(titles)
            ) for _ in range(100)
        ]
        ads = [
            Ad(
                user=choice(users), 
                description="description",
                url="https://example.com",
                title=choice(titles)
            ) for _ in range(100)
        ]
        notes = [
            Note(
                user=choice(users),
                body="body",
                title=choice(titles)
            ) for _ in range(100)
        ]

        Achievement.objects.bulk_create(objs=achievements)
        Ad.objects.bulk_create(objs=ads)
        Note.objects.bulk_create(objs=notes)
