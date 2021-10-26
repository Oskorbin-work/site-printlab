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
class StepHelpMessengerList(ListView):
    model = StepHelpMessenger
    context_object_name = 'help_messenger'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Get information about company
        context['contact'] = Contact.objects.get(id=1)
        context['service_menu'] = Service.objects.all()
        return context
