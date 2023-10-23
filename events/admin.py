from django.contrib import admin

from events.models import FeedEvent


@admin.register(FeedEvent)
class FeedEventAdmin(admin.ModelAdmin):
    pass
