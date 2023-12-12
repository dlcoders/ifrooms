# Generated by Django 5.0 on 2023-12-12 11:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calendarapp', '0006_event_id_reservation'),
        ('reservation', '0007_alter_reservation_justification_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='id_reservation',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='reservation.reservation', verbose_name='Reserva do evento'),
        ),
        migrations.AlterField(
            model_name='event',
            name='status',
            field=models.CharField(default='Aguardando Resposta', max_length=20, verbose_name='Status:'),
        ),
        migrations.DeleteModel(
            name='EventMember',
        ),
    ]