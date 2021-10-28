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
        upload_to='../media_root',
        null=True,
        blank=True,
    )

    def __str__(self):
        return '{}'.format(self.name)


class StepHelpMessenger(models.Model):

    TYPE_HELP_CHOICES = [
        ("TM", "Telegram"),
        ("VR", "Viber"),
    ]

    # for i in TypeHelpMessenger.get_all_names(TypeHelpMessenger):
    #    print(i)

    description_stage = models.TextField(
        blank=True,
    )

    img_step = models.ImageField(
        upload_to='../media_root',
        null=True,
        blank=True,
    )


class TypeHelpMessenger(models.Model):
    name = models.CharField(
        max_length=100
    )
    description_name = models.TextField(
        blank=True,
    )
    steps = models.ManyToManyField(StepHelpMessenger, related_name='steps', blank=True,)

    # def get_all_names(self):
    #    list = []
    #    for i in TypeHelpMessenger.objects.all():
    #        list.append(i.name)
    #    return list


