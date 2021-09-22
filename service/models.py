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
    name = models.CharField(max_length=100, default = "Имя картинки")
    img = models.ImageField(
        upload_to='../media_root',
        null=True,
        blank=True,
    )

    descriptions = models.TextField()

    @property
    def img_url(self):
        if self.img and hasattr(self.img, 'url'):
            return self.img.url


class Service_requirement(models.Model):
    requirement = models.TextField()


class Service(models.Model):
    name = models.CharField(
        max_length=100
    )

    img_title = models.ImageField(
        upload_to='../media_root',
        null=True,
        blank=True,
    )

    img_service = models.ManyToManyField(Image_service, related_name='img_serv')

    description = models.TextField()

    list_requirements = models.ManyToManyField(Service_requirement, related_name='layout_requirements')

    def __str__(self):
        return '{}'.format(self.name)

    class Meta:
        ordering = ('name','description')


