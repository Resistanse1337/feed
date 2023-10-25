from django.db import models
from django.utils.translation import gettext_lazy as _

from events.models import BaseEvent, FeedEvent
from users.models import User


class Note(BaseEvent):
    class Meta:
        verbose_name = _("заметка")
        verbose_name_plural = _("заметки")

    body = models.TextField(verbose_name=_("Тело"))

    @staticmethod
    def get_serializer_name():
        return "NoteSerializer"

    def create_event(self, user: User, title: str):
        FeedEvent.objects.create(
            user=user,
            note=self,
            title=title
        )
