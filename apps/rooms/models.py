from django.db import models

from apps.accounts.models import User


class Room(models.Model):
    CHOICES_AVAILABLE = (
        ("yes", "Sim"),
        ("no", "Não"),
    )

    CHOICES_DEPARTMENT = (
        ("administration", "Bloco 01 - Direção"),
        ("main_building", "Bloco 02 - Principal"),
        ("laboratories", "Bloco 03 - Laboratórios"),
        ("dining_sector", "Bloco 04 - Setor de Alimentação"),
        ("library", "Bloco 05 - Biblioteca"),
        ("health_sector", "Bloco 06 - Setor de Saúde"),
        ("sports_gymnasium", "Bloco 07 - Ginásio Poliesportivo"),
        ("garage", "Bloco 08 - Garagem"),
        ("pool_and_field", "Bloco 09 - Piscina e Campo"),
        ("classrooms", "Bloco 10 - Salas de Aula"),
        ("honey_house", "Bloco 11 - Casa do Mel"),
        ("apiary", "Bloco 12 - Apiário"),
        ("vocational_training_center", "Bloco 13 - CVT"),
        ("campus_territory", "Território do Campus"),
    )

    room_name = models.CharField(
        max_length=100,
        verbose_name="Nome da Sala",
    )
    key = models.CharField(
        max_length=100,
        verbose_name="Chave da Sala",
    )
    department = models.CharField(
        max_length=100,
        verbose_name="Prédio:",
        choices=CHOICES_DEPARTMENT,
    )
    available = models.CharField(
        max_length=25,
        verbose_name="Agendável",
        choices=CHOICES_AVAILABLE,
    )
    id_user_coordinator = models.ManyToManyField(
        User,
        verbose_name="Avaliador de Agendamentos",
        related_name="coordinator_rooms",
        limit_choices_to={"registration_type": "coordinator"},
    )

    def __str__(self):
        return self.room_name
