from django.db import models
from datetime import datetime
from django.urls import reverse

from apps.accounts.models import User
from apps.rooms.models import Room


class EventAbstract(models.Model):
    """Event abstract model"""

    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class EventAbstract(models.Model):
    """Event abstract model"""

    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class EventManager(models.Manager):
    """Event manager"""

    def get_all_events(self):
        events = Event.objects.filter(is_active=True, is_deleted=False)
        return events

    def get_all_events_by_user(self, user):
        events = Event.objects.filter(user=user, is_active=True, is_deleted=False)
        return events

    def get_running_events(self):
        running_events = Event.objects.filter(
            is_active=True,
            status="Deferido",
            is_deleted=False,
            end__gte=datetime.now().date(),
        ).order_by("start")

        return running_events

    def get_running_events_by_user(self, user):
        running_events = Event.objects.filter(
            user=user,
            is_active=True,
            status="Deferido",
            is_deleted=False,
            end__gte=datetime.now().date(),
        ).order_by("start")

        return running_events


class Event(EventAbstract):
    """Event model"""

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
    class_school = models.CharField(
        verbose_name="Turma:",
        max_length=50,
        blank=True,
        null=True,
    )
    id_room = models.ForeignKey(Room, on_delete=models.CASCADE, verbose_name="Sala")
    status = models.CharField(
        verbose_name="Status:",
        max_length=20,
        default="Aguardando Resposta",
    )
    id_reservation = models.OneToOneField(
        "reservation.Reservation",
        on_delete=models.CASCADE,
        verbose_name="Reserva do evento",
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
