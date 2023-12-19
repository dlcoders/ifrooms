from django.contrib import admin
from apps.calendarapp import models


@admin.register(models.Event)
class EventAdmin(admin.ModelAdmin):
    model = models.Event
    list_display = [
        "id",
        "title",
        "user",
        "status",
        "is_active",
        "is_deleted",
    ]
    list_filter = ["is_active", "is_deleted"]
    search_fields = ["title"]
