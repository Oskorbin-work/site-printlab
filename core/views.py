from django.http import HttpResponse
from django.shortcuts import render
from core.models import Contact
from service.models import Service


def ContactDetail(request):
    contact = Contact.objects.get(id=1)
    context = {
        'contact': contact,
        'service_menu': Service.objects.all(),

    }
    return render(request, 'core/contact_detail.html', context)
