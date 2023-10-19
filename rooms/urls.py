from django.urls import path
from .views import calendar_view

urlpatterns = [
    path('rooms/', calendar_view, name='rooms'),
]
