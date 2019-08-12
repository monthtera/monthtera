from django.db import models

from monthtera.categories.models import Category


# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length=30, null=False)
    description = models.TextField()
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.name
