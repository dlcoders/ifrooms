from django.urls import path
from .views import (
    GrantsView,
    CoordinatorGrantReservationFormView,
    TeacherMakeReservationFormView,
    TeacherReservationFormView,
    # TeacherBookingRoomView,
    TeacherMyReservationView,
    TeacherRoomsListView,
)

app_name = "reservation"

urlpatterns = [
    path("coord-grants/", GrantsView.as_view(), name="coord-grants"),
    path(
        "coord-grant-reservation/",
        CoordinatorGrantReservationFormView.as_view(),
        name="coord-grant-reservation",
    ),
    path(
        "teacher-make-reservation/<int:id>/",
        TeacherMakeReservationFormView.as_view(),
        name="teacher-make-reservation",
    ),
    path(
        "teacher-my-reservation/",
        TeacherReservationFormView.as_view(),
        name="teacher-my-reservation",
    ),
    path(
        "teacher-booking-room/",
        TeacherRoomsListView.as_view(),
        name="teacher-booking-room",
    ),
    path(
        "teacher-reservations/",
        TeacherMyReservationView.as_view(),
        name="teacher-reservations",
    ),
]
