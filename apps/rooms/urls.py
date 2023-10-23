from django.urls import path
from .views import calendar_view,CoordinatorCreateRoomFormView

app_name = "room"

urlpatterns = [
    path(
        'rooms/',
        calendar_view,
        name='rooms'
    ),
    path(
        'coord-form-room/',
        CoordinatorCreateRoomFormView.as_view(),
        name='coord-form-room'
    )
]
