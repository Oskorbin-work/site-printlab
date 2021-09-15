from django.http import HttpResponse
from django.shortcuts import render
from core.models import Contact
from django.views.generic import (
    ListView
)


# def for base templates
def index(request):
    object_list = Contact.objects.all()
    return render(
        request,
        'core/contact_list.html',
        context={
            'object_list': object_list,
        }
    )
