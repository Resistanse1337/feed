from django.dispatch import receiver
from django.db.models.signals import post_save

from achievements.models import Achievement
from ads.models import Ad
from notes.models import Note


@receiver(post_save, sender=Achievement)
@receiver(post_save, sender=Ad)
@receiver(post_save, sender=Note)
def create_event(sender, instance, created, **kwargs):
    if created:
        instance.create_event(user=instance.user, title=instance.title)
