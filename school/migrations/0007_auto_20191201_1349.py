# Generated by Django 2.2.4 on 2019-12-01 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0006_auto_20191201_1343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='career',
            name='name',
            field=models.CharField(choices=[('SEG-QUA', 'SEG-QUA'), ('TER-QUI', 'TER-QUI'), ('SEXTA-2h', 'SEXTA-2h'), ('SÁBADO-2h', 'SÁBADO-2h')], max_length=80, unique=True, verbose_name='Dias da semana'),
        ),
    ]
