from django.urls import path, include

from EVTool.vehicles.views import CarDashboardView, CarDetailView, CarEditView, CarDeleteView, CarAddPage

urlpatterns = (
    path('', CarDashboardView.as_view(), name='car-dashboard'),
    path('create/', CarAddPage.as_view(), name='car-add'),
    path('<int:pk>/', include([
        path('', CarDetailView.as_view(), name='car-details'),
        path('edit/', CarEditView.as_view(), name='car-edit'),
        path('delete/', CarDeleteView.as_view(), name='car-delete'),
    ])),
)
