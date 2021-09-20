from django.urls import path

from . import views

app_name = 'services'
urlpatterns = [
    path('', views.ServiceList.as_view(), name='index'),
    path('service/<int:pk>', views.ServiceDetail.as_view(), name='ServicesDetail'),
]
