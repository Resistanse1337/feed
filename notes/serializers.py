from rest_framework import serializers

from events.serializers_registry import SerializersRegistry
from notes.models import Note


class NoteSerializer(serializers.ModelSerializer, metaclass=SerializersRegistry):
    class Meta:
        model = Note
        fields = [
            "body"
        ]
