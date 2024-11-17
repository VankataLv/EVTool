from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render
from django.views.generic import ListView, DetailView, DeleteView, UpdateView

from EVTool.vehicles.models import EVCar


# Cars views----------------------------------------------------------------------------------------
class CarDashboardView(ListView):
    model = EVCar
    template_name = 'vehicles/cars/car-dashboard.html'
    context_object_name = 'all_cars'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # context['search_form'] = SearchForm(self.request.GET) TODD
        return context


class CarDetailView(LoginRequiredMixin, DetailView):
    model = EVCar
    template_name = 'vehicles/cars/car-details.html'
    context_object_name = 'car'


class CarEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    pass
class CarDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    pass
