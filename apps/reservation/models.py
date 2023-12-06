# models.py
from dateutil.relativedelta import relativedelta
from django.db import models
from django.utils import timezone
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

    date = models.DateField(verbose_name="Data:", blank=True, null=False)
    startTime = models.TimeField(verbose_name="Horário de Início")
    endTime = models.TimeField(verbose_name="Horário Final")
    justification = models.CharField(
        verbose_name="Justificativa:",
        max_length=20,
        choices=JUSTIFICATION_CHOICES,
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
        return f"Reservation {self.id} - {self.justification} - {self.date} {self.startTime}-{self.endTime}"

    def save(self, *args, **kwargs):
        if self.periodicity:
            num_occurrences = kwargs.pop("num_occurrences", 1)

            for i in range(1, num_occurrences):
                if self.periodicity == 'Diária':
                    new_date = self.date + timezone.timedelta(days=i)
                elif self.periodicity == 'Semanal':
                    new_date = self.date + timezone.timedelta(weeks=i)
                elif self.periodicity == 'Mensal':
                    # Use relativedelta for months with different numbers of days
                    new_date = self.date + relativedelta(months=i)

                new_reservation = Reservation(
                    date=new_date,
                    startTime=self.startTime,
                    endTime=self.endTime,
                    justification=self.justification,
                    periodicity=self.periodicity,
                    annex=self.annex,
                    message=self.message,
                    reply=self.reply,
                    status=self.status,
                    id_room=self.id_room,
                    id_user_teacher=self.id_user_teacher,
                )

                new_reservation.save_base(raw=True)

        super().save(*args, **kwargs)