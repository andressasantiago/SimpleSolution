from django.db import models
from django.conf import settings


class Profile(models.Model):
    PROFESSOR = 'PR'
    STUDENT = 'ST'
    ADMIN = 'AD'

    PROFILE_TYPE_CHOICES = (
        (PROFESSOR, 'Professor'),
        (STUDENT, 'Student'),
        (ADMIN, 'Admin')
    )

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    date_of_birth = models.DateField(blank=True, null=True, help_text='mm/dd/yy')
    address = models.CharField(max_length=255, blank=True)
    phone = models.CharField(max_length=255, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    profile_type = models.CharField(
        max_length=2,
        choices=PROFILE_TYPE_CHOICES,
    )

    def __str__(self):
        return '{}, {}'.format(self.user.first_name, self.user.last_name)
