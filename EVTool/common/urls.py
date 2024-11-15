from django.shortcuts import render
from django.urls import path

from EVTool.common.views import IndexView

urlpatterns = (
    path('', IndexView.as_view(), name='index'),
)
