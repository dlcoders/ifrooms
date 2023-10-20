from django.urls import path
from .views import GrantsView, RoomsView, GrantReservationFormView, RoomReservationdFormView

app_name = "reservation"

urlpatterns = [
    path('grants/', GrantsView.as_view(), name='grants'),
    path('rooms/', RoomsView.as_view(), name='rooms'),
    path('grant-reservation/', GrantReservationFormView.as_view(), name='grant-reservation'),
    path('room-reservation/', RoomReservationdFormView.as_view(), name='room-reservation'),
]
