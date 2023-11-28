from django.db import models

from apps.accounts.models import User


class Room(models.Model):
    room_name = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name="Nome da Sala",
    )
    key = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name="Chave da Sala",
    )

    CHOICES_DEPARTMENT = (
        ("Bloco 01 - Direção", "Bloco 01 - Direção"),
        ("Bloco 02 - Principal", "Bloco 02 - Principal"),
        ("Bloco 03 - Laboratórios", "Bloco 03 - Laboratórios"),
        ("Bloco 04 - Setor de Alimentação", "Bloco 04 - Setor de Alimentação"),
        ("Bloco 05 - Biblioteca", "Bloco 05 - Biblioteca"),
        ("Bloco 06 - Setor de Saúde", "Bloco 06 - Setor de Saúde"),
        ("Bloco 07 - Ginásio Poliesportivo", "Bloco 07 - Ginásio Poliesportivo"),
        ("Bloco 08 - Garagem", "Bloco 08 - Garagem"),
        ("Bloco 09 - Piscina e Campo", "Bloco 09 - Piscina e Campo"),
        ("Bloco 10 - Salas de Aula", "Bloco 10 - Salas de Aula"),
        ("Bloco 11 - Casa do Mel", "Bloco 11 - Casa do Mel"),
        ("Bloco 12 - Apiário", "Bloco 12 - Apiário"),
        ("Bloco 13 - CVT", "Bloco 13 - CVT"),
        ("Território do Campus", "Território do Campus"),
    )

    department = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name="Prédio:",
        choices=CHOICES_DEPARTMENT,
    )
    CHOICES_AVAILABLE = (
        ("Sim", "Sim"),
        ("Não", "Não"),
    )
    available = models.CharField(
        max_length=5,
        verbose_name="Agendável",
        choices=CHOICES_AVAILABLE,
        blank=True,
        null=True,
    )
    id_user_coordinator = models.ForeignKey(
        User,
        verbose_name="Avaliador de Agendamentos",
        on_delete=models.CASCADE,
        related_name="coordinator_rooms",
        limit_choices_to={"registration_type": "coordinator"},
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.room_name
