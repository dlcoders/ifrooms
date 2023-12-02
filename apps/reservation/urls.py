from django.urls import path
from .views import (
    CoordinatorGrantsReservationView,
    GrantsView,
    CoordinatorGrantReservationFormView,
    ReservationCreateView,
    ReservationDeleteView,
    ReservationListView,
    ReservationUpdateView,
    TeacherMakeReservationFormView,
    TeacherReservationFormView,
    # TeacherBookingRoomView,
    TeacherMyReservationView,
    TeacherReservationListView,
    TeacherRoomsListView,
)

app_name = "reservation"

urlpatterns = [
    path(
        "reservation-create/<int:id>",
        ReservationCreateView.as_view(),
        name="reservation-create",
    ),
    path(
        "teacher-reservation-list",
        TeacherReservationListView.as_view(),
        name="teacher-reservation-list",
    ),
    path("reservation-list", ReservationListView.as_view(), name="reservation-list"),
    path(
        "coordinator/reservation-grants/<int:id>",
        CoordinatorGrantsReservationView.as_view(),
        name="coordinator-reservation-feedback",
    ),
    path(
        "reservation-update/<int:id>",
        ReservationUpdateView.as_view(),
        name="reservation-update",
    ),
    path(
        "reservation-delete/<int:id>",
        ReservationDeleteView.as_view(),
        name="reservation-delete",
    ),
    path("coord-grants/", GrantsView.as_view(), name="coord-grants"),
    path(
        "coord-grant-reservation/",
        CoordinatorGrantReservationFormView.as_view(),
        name="coord-grant-reservation",
    ),
    # path(
    #     "teacher-make-reservation/<int:id>/",
    #     TeacherMakeReservationFormView.as_view(),
    #     name="teacher-make-reservation",
    # ),
    # path(
    #     "teacher-my-reservation/",
    #     TeacherReservationFormView.as_view(),
    #     name="teacher-my-reservation",
    # ),
    # path(
    #     "teacher-booking-room/",
    #     TeacherRoomsListView.as_view(),
    #     name="teacher-booking-room",
    # ),
    path(
        "teacher-reservations/",
        TeacherMyReservationView.as_view(),
        name="teacher-reservations",
    ),
]
