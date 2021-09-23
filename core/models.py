from django.db import models


# Storage information about company
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

    img_logo = models.ImageField(
        upload_to = '../media_root',
        null = True,
        blank = True,
    )

    def __str__(self):
        return '{}'.format(self.name)
