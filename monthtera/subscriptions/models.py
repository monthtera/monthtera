from django.db import models
from django.utils.translation import ugettext_lazy as _

from ..items.models import Item
from ..users.models import User


class Subscription(models.Model):
    item = models.ForeignKey(to=Item,
                             on_delete=models.CASCADE)
    user = models.ForeignKey(to=User,
                             on_delete=models.CASCADE)
    start_date = models.DateField(_("Start Date"), auto_now=True)
    is_alarm = models.BooleanField(_("Is Alarm"), default=True)
    when_alarm = models.DateField(_("When Alarm"))
    note = models.TextField(_("Note"))

    def __str__(self):
        return self.item.name
