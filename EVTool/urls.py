from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('EVTool.common.urls')),
    path('accounts/', include('EVTool.accounts.urls')),
    # path('pets/', include('EVTool.')),
    # path('photos/', include('EVTool.')),
]
