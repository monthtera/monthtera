from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class CategorySubName(models.Model):
    name = models.CharField(max_length=30, blank=True)
    category = models.ForeignKey(
        to=Category,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name
