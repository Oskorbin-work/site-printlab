from django.contrib import admin
from django.urls import include, path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', include('service.urls', namespace='service')),
    path('admin/', admin.site.urls),
    path('contact/', include('core.urls', namespace='contact')),
    path('help_messenger/', include('core.urls', namespace='help_messenger')),
]

urlpatterns += staticfiles_urlpatterns()