# Generated by Django 5.0 on 2023-12-25 19:11

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0002_alter_room_available_alter_room_id_user_coordinator'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='id_user_coordinator',
            field=models.ManyToManyField(blank=True, limit_choices_to={'registration_type': 'coordinator'}, related_name='coordinator_rooms', to=settings.AUTH_USER_MODEL, verbose_name='Avaliador de Agendamentos'),
        ),
    ]
