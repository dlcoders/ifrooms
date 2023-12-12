from datetime import datetime, timedelta
from django.db import models
from django.urls import reverse

from apps.calendarapp.models import EventAbstract
from apps.accounts.models import User


class EventManager(models.Manager):
    """Event manager"""

    def get_all_events(self, user):
        events = Event.objects.filter(user=user, is_active=True, is_deleted=False)
        return events

    def get_running_events(self, user):
        # today = datetime.now().date()
        # start_of_week = today - timedelta(days=today.weekday())
        # end_of_week = start_of_week + timedelta(days=6)

        running_events = Event.objects.filter(
            user=user,
            is_active=True,
            is_deleted=False,
            end__gte=datetime.now().date(),
        ).order_by("start")

        return running_events


class Event(EventAbstract):
    """Event model"""

    STATUS_CHOICES = [
        ("granted", "Deferido"),
        ("rejected", "Indeferido"),
        ("in_progress", "Aguardando Resposta"),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="events",
        verbose_name="Usuário",
    )
    title = models.CharField(
        verbose_name="Título",
        max_length=200,
    )
    start = models.DateTimeField()
    end = models.DateTimeField()
    status = models.CharField(
        verbose_name="Status:",
        max_length=20,
        choices=STATUS_CHOICES,
        default="Aguardando Resposta",
    )

    objects = EventManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("calendarapp:event-detail", args=(self.id,))

    @property
    def get_html_url(self):
        url = reverse("calendarapp:event-detail", args=(self.id,))
        return f'<a href="{url}"> {self.title} </a>'
