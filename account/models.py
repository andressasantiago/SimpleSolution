from django.db import models
from django.conf import settings


class Profile(models.Model):
    PROFESSOR = 'PR'
    STUDENT = 'AL'
    ADMIN = 'AD'

    PROFILE_TYPE_CHOICES = (
        (PROFESSOR, 'Professor'),
        (STUDENT, 'Aluno'),
        (ADMIN, 'Admin')
    )

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    date_of_birth = models.DateField(blank=True, null=True, help_text='mm/dd/yy', verbose_name='Data nascimento')
    address = models.CharField(max_length=255, blank=True, verbose_name='Endereço')
    phone = models.CharField(max_length=255, blank=True, verbose_name='Telefone')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Data criação')
    profile_type = models.CharField(
        max_length=2,
        choices=PROFILE_TYPE_CHOICES, verbose_name='Tipo de usuário'
    )

    def __str__(self):
        return '{} {}'.format(self.user.first_name, self.user.last_name)
