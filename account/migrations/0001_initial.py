# Generated by Django 2.2.4 on 2019-12-01 16:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_birth', models.DateField(blank=True, help_text='mm/dd/yy', null=True, verbose_name='Data nascimento')),
                ('address', models.CharField(blank=True, max_length=255, verbose_name='Endereço')),
                ('phone', models.CharField(blank=True, max_length=255, verbose_name='Telefone')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Data criação')),
                ('profile_type', models.CharField(choices=[('PR', 'Professor'), ('AL', 'Aluno'), ('AD', 'Admin')], max_length=2, verbose_name='Tipo de usuário')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
