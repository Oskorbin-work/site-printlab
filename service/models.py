from django.db import models

from django.db import models

# Storage images for services. Many to many
class Image_service(models.Model):
    name = models.CharField(max_length=100, default = "Имя картинки")
    img = models.ImageField(
        upload_to='../media_root',
        null=True,
        blank=True,
    )

    descriptions = models.TextField()

    # Get url img. This is safe way
    @property
    def img_url(self):
        if self.img and hasattr(self.img, 'url'):
            return self.img.url


#Storage requirements for services. Many to many
class Service_requirement(models.Model):
    requirement = models.TextField()

# Storage information about services
class Service(models.Model):
    # name services
    name = models.CharField(
        max_length=100
    )
    # images for list services
    img_title = models.ImageField(
        upload_to='../media_root',
        null=True,
        blank=True,
    )
    # images for detail services
    img_service = models.ManyToManyField(Image_service, related_name='img_serv')
    # description service
    description = models.TextField()
    # requirements service
    list_requirements = models.ManyToManyField(Service_requirement, related_name='layout_requirements')

    def __str__(self):
        return '{}'.format(self.name)

    class Meta:
        ordering = ('name','description')


