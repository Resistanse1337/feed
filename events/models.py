from django.db import models
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from events.serializers_registry import SerializersRegistry
from django.db.models.signals import post_save

from users.models import User


class EventManager(models.Manager):
    def bulk_create(self, objs, **kwargs):
        super().bulk_create(objs=objs)

        for i in objs:
            post_save.send(i.__class__, instance=i, created=True)


class BaseEvent(models.Model):
    class Meta:
        abstract = True

    objects = EventManager()

    title = models.CharField(max_length=32, verbose_name=_("Заголовок"))
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    @staticmethod
    def get_serializer_name() -> str:
        raise NotImplementedError("You need to implement get_serializer_name method")
    
    def get_serializer(self) -> serializers.ModelSerializer:
        return SerializersRegistry.get_serializer(self.get_serializer_name())

    def create_event(self, user: User, serializer_name: str):
        raise NotImplementedError("You need to implement create_event method")

    @classmethod
    def get_evens_class_names(cls) -> list[str]:
        return [name.__name__.lower() for name in cls.__subclasses__()]


class FeedEvent(models.Model):
    class Meta:
        verbose_name = _("событие в новостной ленте")
        verbose_name_plural = _("события в новостной ленте")

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True, verbose_name=_("Дата создания"))
    title = models.CharField(max_length=32, verbose_name=_("Заголовок"))
    
    achievement = models.ForeignKey('achievements.Achievement', on_delete=models.CASCADE, null=True)
    ad = models.ForeignKey('ads.Ad', on_delete=models.CASCADE, null=True)
    note = models.ForeignKey('notes.Note', on_delete=models.CASCADE, null=True)

    def get_event_object(self) -> BaseEvent | None:
        for field in self._meta.get_fields():
            field_name = str(field).split(".")[-1]
            field_value = getattr(self, field_name)

            if getattr(field_value, "get_serializer_name", None):
                return field_value
