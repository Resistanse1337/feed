from django.apps import apps
from rest_framework import serializers
from achievements.models import Achievement

from events.serializers_registry import SerializersRegistry


class AchievementSerializer(serializers.ModelSerializer, metaclass=SerializersRegistry):
    class Meta:
        model = Achievement
        fields = [
            "title",
            "reason",
            "image",
        ]
