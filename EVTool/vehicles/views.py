from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView

from EVTool.vehicles.forms import EVCarChangeForm, EVCarDeleteForm, EVCarCreateForm
from EVTool.vehicles.models import EVCar


# Cars views----------------------------------------------------------------------------------------
class CarDashboardView(ListView):
    model = EVCar
    template_name = 'vehicles/cars/car-dashboard.html'
    context_object_name = 'all_cars'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class CarAddPage(LoginRequiredMixin, CreateView):
    model = EVCar
    form_class = EVCarCreateForm
    template_name = 'vehicles/cars/car-create.html'

    def form_valid(self, form):
        car = form.save(commit=False)
        car.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy(
            'car-details',
            kwargs={
                'pk': self.request.user.pk,
            }
        )


class CarDetailView(LoginRequiredMixin, DetailView):
    model = EVCar
    template_name = 'vehicles/cars/car-details.html'
    context_object_name = 'car'


class CarEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = EVCar
    template_name = 'vehicles/cars/car-edit.html'
    form_class = EVCarChangeForm

    def test_func(self):
        car = get_object_or_404(EVCar, pk=self.kwargs['pk'])
        user = self.request.user
        return user == car.owner or user.is_staff or user.is_superuser

    def get_success_url(self):
        return reverse_lazy('car-details',kwargs={'pk': self.kwargs['pk'], })


class CarDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = EVCar
    template_name = 'vehicles/cars/car-delete.html'
    # form_class = EVCarDeleteForm

    def get_success_url(self):
        return reverse_lazy('index')

    def test_func(self):
        car = get_object_or_404(EVCar, pk=self.kwargs['pk'])
        return self.request.user == car.owner or self.request.user.is_staff or self.request.user.is_superuser
