from django.apps import AppConfig


class EventsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'events'

    def ready(self) -> None:
        import achievements.serializers  # noqa
        import ads.serializers  # noqa
        import events.models  # noqa
        import notes.serializers  # noqa
        from events.signals import create_event  # noqa
