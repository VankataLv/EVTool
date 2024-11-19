from django.urls import path, include

from EVTool.vehicles.views import (
    BikeDashboardView, BikeAddPage, BikeDetailView, BikeEditView, BikeDeleteView,
    AddPhotoView, PhotoDetailsView, PhotoEditView, PhotoDeleteView
)

urlpatterns = (
    path('', BikeDashboardView.as_view(), name='bike-dashboard'),
    # CRUD for Bikes obj instance ---------------------------------------------------------
    path('create/', BikeAddPage.as_view(), name='bike-add'),
    path('<int:pk>/', include([
        path('', BikeDetailView.as_view(), name='bike-details'),
        path('edit/', BikeEditView.as_view(), name='bike-edit'),
        path('delete/', BikeDeleteView.as_view(), name='bike-delete'),
    ])),

    # CRUD for Photos obj instance--------------------------------------------------
    path('<int:bike_pk>/photos/', include([
        path('add/', AddPhotoView.as_view(), name='bike-photo-add'),
        path('<int:photo_pk>/', include([
            path('', PhotoDetailsView.as_view(), name='bike-photo-details'),
            path('edit/', PhotoEditView.as_view(), name='bike-photo-edit'),
            path('delete/', PhotoDeleteView.as_view(), name='bike-photo-delete'),
        ])),
    ])),
)
