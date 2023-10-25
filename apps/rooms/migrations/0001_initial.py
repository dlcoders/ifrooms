# Generated by Django 4.2.6 on 2023-10-19 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rooms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sala', models.CharField(blank=True, max_length=100, null=True, verbose_name='Nome da Sala')),
                ('chave', models.IntegerField(blank=True, null=True, verbose_name='Chave da Sala')),
                ('predio', models.CharField(blank=True, choices=[('Bloco 01 - Direção', 'Bloco 01 - Direção'), ('Bloco 02 - Principal', 'Bloco 02 - Principal'), ('Bloco 03 - Laboratórios', 'Bloco 03 - Laboratórios'), ('Bloco 04 - Setor de Alimentação', 'Bloco 04 - Setor de Alimentação'), ('Bloco 05 - Biblioteca', 'Bloco 05 - Biblioteca'), ('Bloco 06 - Setor de Saúde', 'Bloco 06 - Setor de Saúde'), ('Bloco 07 - Ginásio Poliesportivo', 'Bloco 07 - Ginásio Poliesportivo'), ('Bloco 08 - Garagem', 'Bloco 08 - Garagem'), ('Bloco 09 - Piscina e Campo', 'Bloco 09 - Piscina e Campo'), ('Bloco 10 - Salas de Aula', 'Bloco 10 - Salas de Aula'), ('Bloco 11 - Casa do Mel', 'Bloco 11 - Casa do Mel'), ('Bloco 12 - Apiário', 'Bloco 12 - Apiário'), ('Bloco 13 - CVT', 'Bloco 13 - CVT'), ('Território do Campus', 'Território do Campus')], max_length=100, null=True, verbose_name='Prédio')),
            ],
        ),
    ]
