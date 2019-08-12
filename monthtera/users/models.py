from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):
    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = models.CharField(_("Name of User"), blank=True, max_length=255)

    email = models.CharField(
        _("email"),
        max_length=255,
        unique=True,
    )
    phone_number = models.CharField(max_length=11, null=True)
    date_of_birth = models.DateTimeField(null=True)
    gender = models.CharField(max_length=1, null=True)
    address = models.CharField(max_length=44, null=True)
    enable_alarm = models.BooleanField(default=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})
