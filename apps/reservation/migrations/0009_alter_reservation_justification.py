# Generated by Django 5.0 on 2023-12-12 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0008_alter_reservation_justification'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='justification',
            field=models.TextField(max_length=200, verbose_name='Justificativa:'),
        ),
    ]
