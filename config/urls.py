from django.contrib import admin
from django.urls import include, path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', include('service.urls', namespace='service')),
    path('admin/', admin.site.urls),
    path('info/', include('core.urls', namespace='info')),
]

urlpatterns += staticfiles_urlpatterns()