# Generated by Django 4.2.6 on 2023-10-18 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='matricula',
            field=models.CharField(default=1, help_text='Ex: 123456', max_length=12, unique=True, verbose_name='Matrícula'),
            preserve_default=False,
        ),
    ]
