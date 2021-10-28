from django.urls import path

from . import views

app_name = 'core'
urlpatterns = [
    path('contact/', views.ContactDetail, name='ContactDetail'),
    path('help_messenger/', views.step_help_messenger_detail, name='step_help_messenger_detail'),
]