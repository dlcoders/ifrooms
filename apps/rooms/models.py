from django.db import models


class Room(models.Model):
    sala = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name="Nome da Sala",
    )
    chave = models.IntegerField(
        null=True,
        blank=True,
        verbose_name="Chave da Sala",
    )

    CHOICES_PREDIO = (
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

    predio = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name="Prédio",
        choices=CHOICES_PREDIO,
    )

    def __str__(self):
        return self.sala
