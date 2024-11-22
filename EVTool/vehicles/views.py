from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView

from EVTool.vehicles.forms import (
    EVCarChangeForm, EVCarCreateForm, EVBikeCreateForm, EVBikeChangeForm, EVCarPhotoCreateForm,
    EVBikePhotoCreateForm,
)
from EVTool.vehicles.models import EVCar, EVBike, EVCarPhoto, EVBikePhoto


# Cars Views ----------------------------------------------------------------------------------------
class CarDashboardView(ListView):
    model = EVCar
    template_name = 'vehicles/cars/car-dashboard.html'
    context_object_name = 'all_cars'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        for car in context['all_cars']:
            first_photo = car.car_photos.first()
            if first_photo:
                car.has_photo = True
                car.first_photo_url = first_photo.image.url
            else:
                car.has_photo = False

        return context

    def get_queryset(self):
        return EVCar.objects.all().order_by('date_published')


class CarAddPage(LoginRequiredMixin, CreateView):
    model = EVCar
    form_class = EVCarCreateForm
    template_name = 'vehicles/cars/car-create.html'

    def form_valid(self, form):
        car = form.save(commit=False)
        car.owner = self.request.user
        car.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('car-details', kwargs={'pk': self.object.pk})


class CarDetailView(LoginRequiredMixin, DetailView):
    model = EVCar
    template_name = 'vehicles/cars/car-details.html'
    context_object_name = 'car'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        car = self.object
        context['photos'] = EVCarPhoto.objects.filter(car=car)

        return context


class CarEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = EVCar
    template_name = 'vehicles/cars/car-edit.html'
    form_class = EVCarChangeForm

    def test_func(self):
        car = get_object_or_404(EVCar, pk=self.kwargs['pk'])
        return self.request.user == car.owner or self.request.user.is_staff or self.request.user.is_superuser

    def get_success_url(self):
        return reverse_lazy('car-details', kwargs={'pk': self.kwargs['pk']})


class CarDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = EVCar
    template_name = 'vehicles/cars/car-delete.html'

    def get_success_url(self):
        return reverse_lazy('index')

    def test_func(self):
        car = get_object_or_404(EVCar, pk=self.kwargs['pk'])
        return self.request.user == car.owner or self.request.user.is_staff or self.request.user.is_superuser


# Bikes Views ---------------------------------------------------------------------------------------
class BikeDashboardView(ListView):
    model = EVBike
    template_name = 'vehicles/bikes/bike-dashboard.html'
    context_object_name = 'all_bikes'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        for bike in context['all_bikes']:
            first_photo = bike.bike_photos.first()
            if first_photo:
                bike.has_photo = True
                bike.first_photo_url = first_photo.image.url
            else:
                bike.has_photo = False

        return context

    def get_queryset(self):
        return EVBike.objects.all().order_by('date_published')

class BikeAddPage(LoginRequiredMixin, CreateView):
    model = EVBike
    form_class = EVBikeCreateForm
    template_name = 'vehicles/bikes/bike-create.html'

    def form_valid(self, form):
        bike = form.save(commit=False)
        bike.owner = self.request.user
        bike.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('bike-details', kwargs={'pk': self.object.pk})


class BikeDetailView(LoginRequiredMixin, DetailView):
    model = EVBike
    template_name = 'vehicles/bikes/bike-details.html'
    context_object_name = 'bike'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        bike = self.object
        context['photos'] = EVBikePhoto.objects.filter(bike=bike)

        return context


class BikeEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = EVBike
    template_name = 'vehicles/bikes/bike-edit.html'
    form_class = EVBikeChangeForm

    def test_func(self):
        bike = get_object_or_404(EVBike, pk=self.kwargs['pk'])
        return self.request.user == bike.owner or self.request.user.is_staff or self.request.user.is_superuser

    def get_success_url(self):
        return reverse_lazy('bike-details', kwargs={'pk': self.kwargs['pk']})


class BikeDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = EVBike
    template_name = 'vehicles/bikes/bike-delete.html'

    def get_success_url(self):
        return reverse_lazy('index')

    def test_func(self):
        bike = get_object_or_404(EVBike, pk=self.kwargs['pk'])
        return self.request.user == bike.owner or self.request.user.is_staff or self.request.user.is_superuser


# Photos Views --------------------------------------------------------------------------------------
# -------- Add Photos Views --------------------------------------------------------------------------------------
class AddCarPhotoView(LoginRequiredMixin, CreateView):
    model = EVCarPhoto
    form_class = EVCarPhotoCreateForm
    template_name = 'vehicles/photos/car-photo-add-page.html'

    def get_success_url(self):
        car = self.object.car
        return reverse_lazy('car-details', kwargs={'pk': car.pk})

    def form_valid(self, form):
        car_pk = self.kwargs['car_pk']
        car = EVCar.objects.get(pk=car_pk)
        form.instance.car = car
        return super().form_valid(form)


class AddBikePhotoView(LoginRequiredMixin, CreateView):
    model = EVBikePhoto
    form_class = EVBikePhotoCreateForm
    template_name = 'vehicles/photos/bike-photo-add-page.html'

    def get_success_url(self):
        bike = self.object.bike
        return reverse_lazy('bike-details', kwargs={'pk': bike.pk})

    def form_valid(self, form):
        bike_pk = self.kwargs['bike_pk']
        bike = EVBike.objects.get(pk=bike_pk)
        form.instance.bike = bike
        return super().form_valid(form)


# -------- Details Delete Photos Views --------------------------------------------------------------------------------
class PhotoCarDetailsDeleteView(LoginRequiredMixin, DeleteView):
    model = EVCarPhoto
    template_name = 'vehicles/photos/car-photo-details-delete-page.html'

    def get_success_url(self):
        car = self.object.car
        return reverse_lazy('car-details', kwargs={'pk': car.pk})

    def get_object(self, queryset=None):
        car_pk = self.kwargs.get('car_pk')
        photo_pk = self.kwargs.get('photo_pk')
        return self.model.objects.get(pk=photo_pk, car_id=car_pk)


class PhotoBikeDetailsDeleteView(LoginRequiredMixin, DeleteView):
    model = EVBikePhoto
    template_name = 'vehicles/photos/bike-photo-details-delete-page.html'

    def get_success_url(self):
        bike = self.object.bike
        return reverse_lazy('bike-details', kwargs={'pk': bike.pk})

    def get_object(self, queryset=None):
        bike_pk = self.kwargs.get('bike_pk')
        photo_pk = self.kwargs.get('photo_pk')
        return self.model.objects.get(pk=photo_pk, bike_id=bike_pk)
