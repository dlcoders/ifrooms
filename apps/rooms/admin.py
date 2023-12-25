from django.contrib import admin
from .models import Room

class RoomAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "room_name",
        "key",
        "department",
        "available",
        "coordinators_list",  # Esta será uma função personalizada para exibir coordenadores
    ]
    list_filter = [
        "department",
        "available",
    ]

    def coordinators_list(self, obj):
        return ", ".join([coordinator.name for coordinator in obj.id_user_coordinator.all()])

    coordinators_list.short_description = "Avaliadores de Agendamentos"

admin.site.register(Room, RoomAdmin)
