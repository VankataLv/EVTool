from django.urls import path, include

from EVTool.vehicles.views import CarDashboardView, CarDetailView, CarEditView, CarDeleteView, CarAddPage, AddPhotoView, \
    PhotoDetailsView, PhotoEditView, PhotoDeleteView

urlpatterns = (
    path('', CarDashboardView.as_view(), name='car-dashboard'),
    # CRUD for Cars obj instance--------------------------------------------------
    path('create/', CarAddPage.as_view(), name='car-add'),
    path('<int:pk>/', include([
        path('', CarDetailView.as_view(), name='car-details'),
        path('edit/', CarEditView.as_view(), name='car-edit'),
        path('delete/', CarDeleteView.as_view(), name='car-delete'),
    ])),

    # CRUD for Photos obj instance--------------------------------------------------
    path('<int:car_pk>/photos/', include([
        path('add/', AddPhotoView.as_view(), name='car-photo-add'),
        path('<int:photo_pk>/', include([
            path('', PhotoDetailsView.as_view(), name='car-photo-details'),
            path('edit/', PhotoEditView.as_view(), name='car-photo-edit'),
            path('delete/', PhotoDeleteView.as_view(), name='car-photo-delete'),
        ])),
    ])),
)
# urlpatterns = (
#     path('', CarDashboardView.as_view(), name='car-dashboard'),
#     # CRUD for Cars object instance
#     path('create/', CarAddPage.as_view(), name='car-add'),
#     path('<int:pk>/', CarDetailView.as_view(), name='car-details'),
#     path('<int:pk>/edit/', CarEditView.as_view(), name='car-edit'),
#     path('<int:pk>/delete/', CarDeleteView.as_view(), name='car-delete'),
#
#     # CRUD for Photos object instance
#     path('<int:car_pk>/photos/add/', AddPhotoView.as_view(), name='car-photo-add'),
#     path('<int:car_pk>/photos/<int:photo_pk>/', PhotoDetailsView.as_view(), name='car-photo-details'),
#     path('<int:car_pk>/photos/<int:photo_pk>/edit/', PhotoEditView.as_view(), name='car-photo-edit'),
#     path('<int:car_pk>/photos/<int:photo_pk>/delete/', PhotoDeleteView.as_view(), name='car-photo-delete'),
# )
