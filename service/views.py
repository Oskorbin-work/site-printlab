from django.shortcuts import render

from .models import Service
from django.views.generic import (
    ListView, DetailView
)
from core.models import Contact


# View services on the main page
class ServiceList(ListView):
    model = Service
    context_object_name = 'service_list'
    paginate_by = 12

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Get information about company
        context['contact'] = Contact.objects.get(id=1)
        context['service_menu'] = Service.objects.all()
        return context


# View information for services
class ServiceDetail(DetailView):
    model = Service
    context_object_name = 'service_detail'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Get information about company
        context['contact'] = Contact.objects.get(id=1)
        # Get all list for menubar
        context['service_menu'] = Service.objects.all()
        return context
