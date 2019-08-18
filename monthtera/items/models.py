from django.db import models
from djmoney.models.fields import MoneyField
from django.utils.translation import ugettext_lazy as _

from ..brands.models import Brand


class Item(models.Model):
    CHANNELS = [
        ('WEB', 'Web'),
        ('WEB/APP', 'Web/App'),
        ('APP', 'App'),
        ('OFFLINE', 'Offline'),
    ]
    name = models.CharField(_("Name"), max_length=100)
    brand = models.ForeignKey(to=Brand,
                              on_delete=models.CASCADE)
    cycle = models.DurationField(_("Cycle"))
    price = MoneyField(_("Price"),
                       max_digits=14,
                       decimal_places=0,
                       default_currency='KRW')
    channel = models.CharField(_("Channel"),
                               max_length=30,
                               choices=CHANNELS,
                               blank=True)
    cancel_channel = models.CharField(_("Channel"),
                                      max_length=30,
                                      choices=CHANNELS,
                                      blank=True)
    how_to_cancel = models.TextField(_("How to cancel"))

    def __str__(self):
        return self.name
