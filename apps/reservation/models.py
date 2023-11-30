from django.db import models

from apps.accounts.models import User
from apps.rooms.models import Room


class Reservation(models.Model):
    JUSTIFICATION_CHOICES = [
        ("Aula", "Aula"),
        ("Trabalho", "Trabalho"),
        ("Reunião", "Reunião"),
    ]
    
    PERIODICITY_CHOICES = [
        ("Diária", "Diária"),
        ("Semanal", "Semanal"),
        ("Mensal", "Mensal"),
    ]
    
    STATUS_CHOICES = [
        ("Deferido", "Deferido"),
        ("Indeferido", "Indeferido"),
        ("Aguardando Resposta", "Aguardando Resposta"),
    ]
    
    date = models.DateField()
    startTime = models.TimeField()
    endTime = models.TimeField()
    justification = models.CharField(
        verbose_name="Justificativa:",
        max_length=20,
        choices=JUSTIFICATION_CHOICES,
        blank=True,
        null=True
    )
    periodicity = models.CharField(
        verbose_name="Periodicidade:",
        max_length=20,
        choices=PERIODICITY_CHOICES,
        blank=True,
        null=True
    )
    annex = models.FileField(
        verbose_name="Anexo:",
        upload_to="reservation_annex/", 
        blank=True, 
        null=True
    )
    message = models.CharField(
        verbose_name="Mensagem:",
        max_length=150,
        blank=True, 
        null=True
    )
    reply = models.CharField(
        verbose_name="Resposta:",
        max_length=150,
        blank=True, 
        null=True
    )
    status = models.CharField(
        verbose_name="Status:",
        max_length=20,
        choices=STATUS_CHOICES,
        blank=True,
        null=True
    )
    id_room = models.ForeignKey(
        Room,
        on_delete=models.CASCADE,
        null=True
    )
    id_user_teacher = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="teacher_reservations",
        limit_choices_to={"registration_type": "teacher"},
        null=True
    )
    id_user_coordinator = models.ManyToManyField(
        User,
        related_name="coordinator_reservations",
        limit_choices_to={"registration_type": "coordinator"},
        null=True
    )

    def __str__(self):
        return f"Reservation {self.id} - {self.justification} - {self.date} {self.startTime}-{self.endTime}"
