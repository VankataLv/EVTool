from django.urls import path, include

from EVTool.services.views import ServiceDashboardView, ServiceAddPage, ServiceEditView, ServiceDeleteView

urlpatterns = (
    path('', ServiceDashboardView.as_view(), name='service-dashboard'),

    path('create/', ServiceAddPage.as_view(), name='service-add'),
    path('<slug:slug>/', include([
        path('edit/', ServiceEditView.as_view(), name='service-edit'),
        path('delete/', ServiceDeleteView.as_view(), name='service-delete'),
    ])),
)

