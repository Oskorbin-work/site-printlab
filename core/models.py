from django.db import models


class Contact(models.Model):
    name = models.CharField(
        max_length=100
    )
    address_shop = models.CharField(
        max_length=100
    )
    email = models.CharField(
        max_length=100
    )
    telephone = models.CharField(
        max_length=100
    )

    def __str__(self):
        return '{}'.format(self.name)
# Create your models here.
