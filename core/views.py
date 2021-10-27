from django.http import HttpResponse
from django.shortcuts import render
from core.models import (
    Contact, StepHelpMessenger
)
from service.models import Service
from django.views.generic import (
    ListView, DetailView
)


def ContactDetail(request):
    contact = Contact.objects.get(id=1)
    context = {
        'contact': contact,
        'service_menu': Service.objects.all(),

    }
    return render(request, 'core/contact_detail.html', context)


# View help messenger
def StepHelpMessengerDetail(request):
    contact = Contact.objects.get(id=1)
    context = {
        'contact': contact,
        'service_menu': Service.objects.all(),
        'step_help_messenger': StepHelpMessenger.objects.all(),

    }
    return render(request, 'core/help_messenger.html', context)
