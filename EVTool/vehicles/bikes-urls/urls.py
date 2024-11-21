from django.urls import path, include

from EVTool.vehicles.views import (
    BikeDashboardView, BikeAddPage, BikeDetailView, BikeEditView, BikeDeleteView, AddBikePhotoView, PhotoBikeDetailsDeleteView,

)

urlpatterns = (
    path('', BikeDashboardView.as_view(), name='bike-dashboard'),
    # CRUD for Bikes obj instance ---------------------------------------------------------
    path('create/', BikeAddPage.as_view(), name='bike-add'),
    path('<int:pk>/', include([
        path('', BikeDetailView.as_view(), name='bike-details'),
        path('edit/', BikeEditView.as_view(), name='bike-edit'),
        path('delete/', BikeDeleteView.as_view(), name='bike-delete'),
    ])
),

    # CRUD for Photos obj instance--------------------------------------------------
    path('<int:bike_pk>/photos/', include([
        path('add/', AddBikePhotoView.as_view(), name='bike-photo-add'),
        path('<int:photo_pk>/delete/', PhotoBikeDetailsDeleteView.as_view(), name='bike-photo-delete'),
        ])
    ),
)
