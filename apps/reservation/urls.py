from django.urls import path
from .views import (
    CoordinatorGrantsReservationView,
    ReservationCreateView,
    ReservationDeleteView,
    ReservationListView,
    ReservationUpdateView,
    TeacherReservationListView,
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
]
