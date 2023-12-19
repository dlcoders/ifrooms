from django.urls import path

from . import views

app_name = "calendarapp"


urlpatterns = [
    path("general-calendar", views.GeneralCalendar.as_view(), name="general-calendar"),
    path(
        "my-calendar-teacher/",
        views.MyCalendarTeacher.as_view(),
        name="my-calendar-teacher",
    ),
]
