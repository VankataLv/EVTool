from django.shortcuts import render
from django.urls import path

from EVTool.common.views import IndexView, UnderConstructionView

urlpatterns = (
    path('', IndexView.as_view(), name='index'),
    path('under-construction/', UnderConstructionView.as_view(), name='under-construction'),
)
