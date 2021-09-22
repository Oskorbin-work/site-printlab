from django.contrib import admin
from service.models import (
Service, Image_service, Service_requirement
)
admin.site.register(Service)
admin.site.register(Image_service)
admin.site.register(Service_requirement)
# Register your models here.
