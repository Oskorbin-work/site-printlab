from django.http import HttpResponse
from django.shortcuts import render

from core.models import Contact
from django.views.generic import (
    ListView
)


class BaseContact(ListView):
    template_name = 'base.html'
    queryset = Contact.objects.filter(id=1)
    context_object_name = 'contact'


class index(ListView):
    model = Contact