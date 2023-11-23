from django.urls import path
from .views import calendar_view, RoomsListView, RoomsCreateView, RoomsDeleteView, RoomsDetailView, RoomsUpdateView

app_name = "room"

urlpatterns = [
    path("rooms/", calendar_view, name="rooms"),

    path("rooms/list", RoomsListView.as_view(), name="rooms_list"),
    path("rooms/create", RoomsCreateView.as_view(), name="rooms_create"),
    path("rooms/update/<int:id>", RoomsUpdateView.as_view(), name="rooms_update"),
    path("rooms/delete/<int:id>", RoomsDeleteView.as_view(), name="rooms_delete"),
    path("rooms/detail/<int:id>", RoomsDetailView.as_view(), name="rooms_detail")
]
