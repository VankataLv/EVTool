from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from EVTool.services.forms import ServiceCreateForm, ServiceEditForm, ServiceDeleteForm
from EVTool.services.models import Service


class ServiceDashboardView(ListView):
    model = Service
    template_name = 'services/service-dashboard.html'
    context_object_name = 'all_services'
    paginate_by = 5

    def get_queryset(self):
        queryset = Service.objects.all()

        area = self.request.GET.get('area')
        if area:
            queryset = queryset.filter(area__icontains=area)

        return queryset.order_by('created_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['service_area_choices'] = Service.AREA_CHOICES
        return context


class ServiceAddPage(LoginRequiredMixin, CreateView):
    model = Service
    form_class = ServiceCreateForm
    template_name = 'services/service-create.html'

    def form_valid(self, form):
        service = form.save(commit=False)
        service.owner = self.request.user
        service.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('service-dashboard')


class ServiceEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Service
    form_class = ServiceEditForm
    template_name = 'services/service-edit.html'

    def get_success_url(self):
        return reverse_lazy('service-dashboard')

    def test_func(self):
        service = get_object_or_404(Service, slug=self.kwargs['slug'])
        return self.request.user == service.owner or self.request.user.is_staff or self.request.user.is_superuser


class ServiceDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Service
    form_class = ServiceDeleteForm
    template_name = 'services/service-delete.html'

    def get_success_url(self):
        return reverse_lazy('service-dashboard')

    def test_func(self):
        service = get_object_or_404(Service, slug=self.kwargs['slug'])
        return self.request.user == service.owner or self.request.user.is_staff or self.request.user.is_superuser
