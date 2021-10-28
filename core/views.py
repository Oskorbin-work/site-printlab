from django.http import HttpResponse
from django.shortcuts import render
from core.models import (
    Contact, TypeHelpMessenger
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
def step_help_messenger_detail(request):
    contact = Contact.objects.get(id=1)
    context = {
        'contact': contact,
        'service_menu': Service.objects.all(),
        'type_help_messenger': TypeHelpMessenger.objects.all(),

    }
    return render(request, 'core/help_messenger.html', context)
