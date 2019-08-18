from django.db import models
from django.utils.translation import ugettext_lazy as _

from ..users.models import User


class Post(models.Model):
    title = models.TextField(_("Title"))
    text = models.TextField(_("Text"))
    author = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(_("Created At"), auto_now=True)

    def __str__(self):
        return self.title
