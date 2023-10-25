from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from events.models import BaseEvent, FeedEvent
from users.models import User


class Ad(BaseEvent):
    class Meta:
        verbose_name = _("рекламное объявление")
        verbose_name_plural = _("рекламные объявление")

    description = models.TextField(verbose_name=_("Описание"))
    image = models.ImageField(verbose_name=_("Изображение"), default=settings.DEFAULT_IMAGE)
    url = models.URLField(verbose_name=_("Ссылка на рекламируемый ресурс"))

    @staticmethod
    def get_serializer_name():
        return "AdSerializer"

    def create_event(self, user: User, title: str):
        FeedEvent.objects.create(
            user=user,
            ad=self,
            title=title
        )
