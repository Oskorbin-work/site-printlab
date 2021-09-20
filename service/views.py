from django.shortcuts import render

from .models import Service
from django.views.generic import (
    ListView, DetailView
)
from core.models import Contact


class ServiceList(ListView):
    model = Service
    context_object_name = 'service_list'
    paginate_by = 12

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contact'] = Contact.objects.get(id=1)
        return context


class ServiceDetail(DetailView):
    model = Service
    context_object_name = 'service_detail'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contact'] = Contact.objects.get(id=1)
        context['object_list'] = Service.objects.all()
        return context
