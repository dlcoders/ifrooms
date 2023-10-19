from django.urls import path
from .views import GrantsView, RoomsView

app_name = "reservation"

urlpatterns = [
    path('grants/', GrantsView.as_view(), name='grants'),
    path('rooms/', RoomsView.as_view(), name='rooms'),
]
