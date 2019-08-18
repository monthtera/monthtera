from django.db import models
from django.utils.translation import ugettext_lazy as _

from ..categories.models import Category


class Brand(models.Model):
    name = models.CharField(_("Name"), max_length=30)
    description = models.TextField(_("Description"))
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.name


class BrandSubName(models.Model):
    name = models.CharField(max_length=30, blank=True)
    brand = models.ForeignKey(
        to=Brand,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name
