from django.urls import path

from . import views

app_name = 'core'
urlpatterns = [
    path('contact/', views.ContactDetail, name='ContactDetail'),
    path('help_messenger/', views.StepHelpMessengerDetail, name='StepHelpMessengerDetail'),
]