from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _
from events.models import BaseEvent, FeedEvent
from users.models import User


class Achievement(BaseEvent):
    class Meta:
        verbose_name = _("достижение")
        verbose_name_plural = _("достижения")

    reason = models.TextField(verbose_name=_("Условие получения"))
    image = models.ImageField(verbose_name=_("Изображение"), default=settings.DEFAULT_IMAGE)

    @staticmethod
    def get_serializer_name():
        return "AchievementSerializer"
    
    def create_event(self, user: User, title: str):
        FeedEvent.objects.create(
            user=user,
            achievement=self,
            title=title
        )
