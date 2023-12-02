from django.urls import path
from .views import (
    calendar_view,
    RoomsListView,
    RoomsCreateView,
    RoomsDeleteView,
    RoomsUpdateView,
)

app_name = "room"

urlpatterns = [
    path("calendar", calendar_view, name="calendar"),
    path("room-list", RoomsListView.as_view(), name="room-list"),
    path("room-create", RoomsCreateView.as_view(), name="room-create"),
    path("room-update/<int:id>", RoomsUpdateView.as_view(), name="room-update"),
    path("room-delete/<int:id>", RoomsDeleteView.as_view(), name="room-delete"),
]
