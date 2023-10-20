from django.urls import path
from .views import calendar_view, BookingRoomView, MyReservationView, CreateRoomFormView

urlpatterns = [
    path('rooms/', calendar_view, name='rooms'),
    path('booking-room/', BookingRoomView.as_view(), name='booking-room'),
    path('my-reservations/', MyReservationView.as_view(), name='my-reservations'),
    path('create-room', CreateRoomFormView.as_view(), name='create-room')
]
