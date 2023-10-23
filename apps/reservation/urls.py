from django.urls import path
from .views import GrantsView, RoomsView, CoordinatorGrantReservationFormView, TeacherMakeReservationFormView, TeacherMyReservationFormView

app_name = "reservation" 

urlpatterns = [
    path(
        'coord-grants/',
        GrantsView.as_view(),
        name='coord-grants'
    ),
    path(
        'coord-rooms/',
        RoomsView.as_view(),
        name='coord-rooms'
    ),
    path(
        'coord-grant-reservation/',
        CoordinatorGrantReservationFormView.as_view(),
        name='coord-grant-reservation'
    ),
    path('teacher-room-reservation/',
        TeacherMakeReservationFormView.as_view(),
        name='teacherroom-reservation'
    ),
    path(
        'teacher-my-reservation/',
        TeacherMyReservationFormView.as_view(),
        name='teacher-my-reservation'
    ),
]
