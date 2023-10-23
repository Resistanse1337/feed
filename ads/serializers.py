from rest_framework import serializers

from ads.models import Ad
from events.serializers_registry import SerializersRegistry


class AdSerializer(serializers.ModelSerializer, metaclass=SerializersRegistry):
    class Meta:
        model = Ad
        fields = [
            "description",
            "image",
            "url",
        ]
