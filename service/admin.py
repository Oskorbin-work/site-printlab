from django.contrib import admin
from service.models import (
    Service, ImageService, ServiceRequirement
)
admin.site.register(Service)
admin.site.register(ImageService)
admin.site.register(ServiceRequirement)
