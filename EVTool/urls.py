from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from EVTool import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('EVTool.common.urls')),
    path('accounts/', include('EVTool.accounts.urls')),
    path('vehicles/cars/', include('EVTool.vehicles.cars-urls.urls')),
    path('vehicles/bikes/', include('EVTool.vehicles.bikes-urls.urls')),
    path('services', include('EVTool.services.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)