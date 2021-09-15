from django.db import models

# Create your models here.

from django.db import models

"""
class Parameters_service(models.Model):
    name = models.CharField(
        max_length=400
    )
    descriptions = models.CharField(
        max_length=400
    )
"""

class Image_service(models.Model):
    img = models.ImageField(
        upload_to='../media_root',
        null=True,
        blank=True,
    )
    descriptions = models.TextField()


class Service(models.Model):
    name = models.CharField(
        max_length=100
    )
    img = models.ForeignKey(Image_service, on_delete=models.CASCADE)

    descriptions = models.TextField()

    def __str__(self):
        return '{}'.format(self.name)


