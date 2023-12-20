# models.py
from django.db import models
from apps.accounts.models import User
from apps.calendarapp.models import Event
from apps.rooms.models import Room
from datetime import datetime, time


class Reservation(models.Model):
    PERIODICITY_CHOICES = [
        ("daily", "Diária"),
        ("weekly", "Semanal"),
        ("monthly", "Mensal"),
    ]

    STATUS_CHOICES = [
        ("granted", "Deferido"),
        ("rejected", "Indeferido"),
        ("in_progress", "Aguardando Resposta"),
    ]

    date = models.DateField(verbose_name="Data:", blank=True, null=False)
    start_time = models.TimeField(verbose_name="Horário de Início")
    end_time = models.TimeField(verbose_name="Horário Final")
    justification = models.TextField(
        verbose_name="Justificativa:",
        max_length=200,
    )
    class_school = models.CharField(
        verbose_name="Turma:",
        max_length=50,
        blank=True,
        null=True,
    )
    periodicity = models.CharField(
        verbose_name="Periodicidade:",
        max_length=20,
        choices=PERIODICITY_CHOICES,
        blank=True,
        null=True,
    )
    annex = models.FileField(
        verbose_name="Anexo:", upload_to="reservation_annex/", blank=True, null=True
    )
    message = models.CharField(
        verbose_name="Mensagem:", max_length=150, blank=True, null=True
    )
    reply = models.CharField(
        verbose_name="Resposta:", max_length=150, blank=True, null=True
    )
    status = models.CharField(
        verbose_name="Status:",
        max_length=20,
        choices=STATUS_CHOICES,
    )
    id_room = models.ForeignKey(Room, on_delete=models.CASCADE, verbose_name="Sala")
    id_user_teacher = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="teacher_reservations",
        limit_choices_to={"registration_type": "teacher"},
        verbose_name="Professor",
    )

    def __str__(self):
        return f"Reservation {self.id} - {self.justification} - {self.date} {self.start_time}-{self.end_time}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        event = Event.objects.filter(id_reservation=self).first()

        if event:
            event.title = self.justification
            event.start = datetime.combine(self.date, self.convert_to_time(self.start_time))
            event.end = datetime.combine(self.date, self.convert_to_time(self.end_time))
            event.status = self.status
            event.save()
        else:
            Event.objects.create(
                user=self.id_user_teacher,
                title=self.justification,
                start=datetime.combine(self.date, self.convert_to_time(self.start_time)),
                end=datetime.combine(self.date, self.convert_to_time(self.end_time)),
                class_school=self.class_school,
                id_reservation=self,
                id_room=self.id_room,
                status=self.status,
            )

    def convert_to_time(self, input_time):
        if isinstance(input_time, time):
            return input_time

        return datetime.strptime(str(input_time), "%H:%M:%S").time()