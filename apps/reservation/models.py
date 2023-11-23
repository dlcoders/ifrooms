from django.db import models


class Reservation(models.Model):
    JUSTIFICATION_CHOICES = [
        ("Aula", "Aula"),
        ("Trabalho", "Trabalho"),
        ("Reunião", "Reunião"),
    ]

    date = models.DateField()
    startTime = models.TimeField()
    endTime = models.TimeField()
    justification = models.CharField(max_length=20, choices=JUSTIFICATION_CHOICES)
    annex = models.FileField(upload_to="reservation_annex/", blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    reply = models.TextField(blank=True, null=True)
    # id_user_teacher = models.ForeignKey(User, )
    # id_user_coordinator = models.ForeignKey(User, )

    def __str__(self):
        return f"Reservation {self.id} - {self.justification} - {self.date} {self.startTime}-{self.endTime}"
