from django.contrib import admin

from ads.models import Ad


@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    pass
