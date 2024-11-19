from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView

from EVTool.vehicles.forms import (
    EVCarChangeForm, EVCarCreateForm, EVBikeCreateForm, EVBikeChangeForm, EVPhotoCreateForm, EVPhotoEditForm,
)
from EVTool.vehicles.models import EVCar, EVBike, EVPhoto


# Cars Views ----------------------------------------------------------------------------------------
class CarDashboardView(ListView):
    model = EVCar
    template_name = 'vehicles/cars/car-dashboard.html'
    context_object_name = 'all_cars'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        car_content_type = ContentType.objects.get_for_model(EVCar)

        for car in context['all_cars']:
            first_photo = EVPhoto.objects.filter(content_type=car_content_type, object_id=car.pk).first()
            car.has_photo = first_photo is not None
            car.first_photo_url = first_photo.image.url if first_photo else None

        return context


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

        content_type = ContentType.objects.get_for_model(EVCar)
        context['photos'] = EVPhoto.objects.filter(content_type=content_type, object_id=car.pk)

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        bike_content_type = ContentType.objects.get_for_model(EVBike)

        for bike in context['all_bikes']:
            first_photo = EVPhoto.objects.filter(content_type=bike_content_type, object_id=bike.pk).first()
            bike.has_photo = first_photo is not None
            bike.first_photo_url = first_photo.image.url if first_photo else None

        return context

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

        content_type = ContentType.objects.get_for_model(EVBike)
        context['photos'] = EVPhoto.objects.filter(content_type=content_type, object_id=bike.pk)

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
class AddPhotoView(LoginRequiredMixin, CreateView):
    model = EVPhoto
    form_class = EVPhotoCreateForm
    template_name = 'vehicles/photos/photo-add-page.html'

    def get_success_url(self):
        photo = self.object
        if isinstance(photo.content_object, EVCar):
            return reverse_lazy('car-details', kwargs={'pk': photo.content_object.pk})
        elif isinstance(photo.content_object, EVBike):
            return reverse_lazy('bike-details', kwargs={'pk': photo.content_object.pk})

    def form_valid(self, form):
        # Dynamically fill `content_type` and `object_id`
        obj_pk = self.kwargs.get('car_pk') or self.kwargs.get('bike_pk')
        obj = EVCar.objects.filter(pk=obj_pk).first() or EVBike.objects.filter(pk=obj_pk).first()
        if obj:
            content_type = ContentType.objects.get_for_model(obj)
            photo = form.save(commit=False)
            photo.content_type = content_type
            photo.object_id = obj_pk

            photo.save()
            return super().form_valid(form)
        else:
            form.add_error(None, "Invalid object.")
            return self.form_invalid(form)


class PhotoDetailsView(LoginRequiredMixin, DetailView):
    model = EVPhoto
    template_name = 'vehicles/photos/photo-details-page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class PhotoEditView(LoginRequiredMixin, UpdateView):
    model = EVPhoto
    template_name = 'vehicles/photos/photo-edit-page.html'
    form_class = EVPhotoEditForm

    def get_success_url(self):
        return reverse_lazy('photo-details', kwargs={'pk': self.object.pk})


class PhotoDeleteView(LoginRequiredMixin, DeleteView):
    model = EVPhoto
    template_name = 'vehicles/photos/photo-delete-page.html'

    def get_success_url(self):
        return reverse_lazy('show-home-page')
