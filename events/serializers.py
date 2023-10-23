from rest_framework import serializers

from events.models import FeedEvent


class FeedEventSerializer(serializers.ModelSerializer):
    event = serializers.SerializerMethodField()

    class Meta:
        model = FeedEvent
        fields = [
            "date",
            "title",
            "event"
        ]

    def get_event(self, feed_event: FeedEvent):
        event_object = feed_event.get_event_object()
        serializer = event_object.get_serializer()
        return serializer(event_object).data
