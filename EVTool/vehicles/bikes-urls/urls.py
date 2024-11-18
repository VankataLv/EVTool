from django.urls import path, include

from EVTool.vehicles.views import BikeDashboardView, BikeAddPage, BikeDetailView, BikeEditView, BikeDeleteView

urlpatterns = (
    path('', BikeDashboardView.as_view(), name='bike-dashboard'),
    path('create/', BikeAddPage.as_view(), name='bike-add'),
    path('<int:pk>/', include([
        path('', BikeDetailView.as_view(), name='bike-details'),
        path('edit/', BikeEditView.as_view(), name='bike-edit'),
        path('delete/', BikeDeleteView.as_view(), name='bike-delete'),
    ])),
)
