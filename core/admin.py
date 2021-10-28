from django.contrib import admin
from core.models import (
   Contact, StepHelpMessenger, TypeHelpMessenger
)

admin.site.register(Contact)
admin.site.register(TypeHelpMessenger)
admin.site.register(StepHelpMessenger)
# Register your models here.
