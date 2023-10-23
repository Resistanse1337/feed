from rest_framework import filters
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination

from events.models import BaseEvent, FeedEvent
from events.serializers import FeedEventSerializer


class EventsView(ListAPIView):
    serializer_class = FeedEventSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']
    pagination_class = PageNumberPagination

    def get_queryset(self):
        qs = FeedEvent.objects.select_related("user")

        for class_name in BaseEvent.get_evens_class_names():
            qs = qs.select_related(class_name)

        return qs.filter(user__id=self.kwargs["pk"]).order_by("-date")
