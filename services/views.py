from django.shortcuts import render

from .models import Service
from django.views.generic import (
    ListView
)
from core.models import Contact


class ServicesList(ListView):
    model = Service
    context_object_name = 'service_list'
    paginate_by = 12

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contact'] = Contact.objects.get(id=1)
        return context

