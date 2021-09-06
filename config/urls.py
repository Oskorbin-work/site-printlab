from django.contrib import admin
from django.urls import include, path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', include('core.urls', namespace = 'core')),
    path('admin/', admin.site.urls),
]

urlpatterns += staticfiles_urlpatterns()