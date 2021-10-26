from django.urls import path

from . import views

app_name = 'core'
urlpatterns = [
    path('', views.ContactDetail, name='ContactDetail'),
    path('', views.StepHelpMessengerList, name='StepHelpMessengerList'),
]