from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class CustomUser(AbstractUser):
    email = models.CharField(
        max_length=255,
        verbose_name='email',
        unique=True,
    )
    phone_number = models.CharField(max_length=11, null=True)
    date_of_birth = models.DateTimeField(null=True)
    gender = models.CharField(max_length=1, null=True)
    address = models.CharField(max_length=44, null=True)
    enable_alarm = models.BooleanField(default=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
