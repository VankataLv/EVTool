from django.contrib import messages
from django.contrib.auth import get_user_model, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView

from EVTool.accounts.forms import AppUserCreationForm, ProfileEditForm
from EVTool.accounts.models import Profile

UserModel = get_user_model()


# ------------------------ AppUser Views -----------------------------
class AppUserRegisterView(CreateView):
    model = UserModel
    form_class = AppUserCreationForm
    template_name = 'accounts/register-page.html'

    def get_success_url(self):
        return reverse_lazy(
            'profile-details',
            kwargs={'pk': self.object.pk},
        )

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        messages.success(self.request, "Account created successfully!")
        return response


class AppUserLoginView(LoginView):
    template_name = 'accounts/login-page.html'

    def form_valid(self, form):
        user = form.get_user()
        if not user.is_active:

            messages.error(self.request,
                           'Your account has been deactivated. '
                           'If you need assistance, please contact support at 0900-123456.')
            return redirect(reverse_lazy('index'))
        return super().form_valid(form)


class ProfileDetailView(DetailView, UserPassesTestMixin):
    model = UserModel
    template_name = 'accounts/profile-details-page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.object

        return context

    def test_func(self):
        is_allowed = self.request.user.is_staff or self.request.user.is_superuser
        is_own_profile = self.request.user.pk == self.kwargs['pk']
        return is_allowed or is_own_profile

    def get_queryset(self):
        if self.request.user.is_staff or self.request.user.is_superuser:
            return self.model.objects.all()
        return self.model.objects.filter(pk=self.request.user.pk)

    def handle_no_permission(self):
        messages.error(self.request, "You are not allowed to view this profile.")
        return redirect('index')


class ProfileEditView(LoginRequiredMixin, UpdateView, UserPassesTestMixin):
    model = Profile
    form_class = ProfileEditForm
    template_name = 'accounts/profile-edit-page.html'

    def get_success_url(self):
        return reverse_lazy(
            'profile-details',
            kwargs={'pk': self.object.user.pk},
        )

    def test_func(self):
        is_allowed = self.request.user.is_staff or self.request.user.is_superuser
        is_own_profile = self.request.user.pk == self.kwargs['pk']
        return is_allowed or is_own_profile

    def get_queryset(self):
        if self.request.user.is_staff or self.request.user.is_superuser:
            return self.model.objects.all()
        return self.model.objects.filter(pk=self.request.user.pk)

    def handle_no_permission(self):
        messages.error(self.request, "You are not allowed to view this profile.")
        return redirect('index')


class ProfileDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Profile
    template_name = 'accounts/profile-delete-page.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        user = self.get_object().user
        user.is_active = False
        user.save()

        logout(self.request)

        return super().form_valid(form)

    def test_func(self):
        is_allowed = self.request.user.is_staff or self.request.user.is_superuser
        is_own_profile = self.request.user.pk == self.kwargs['pk']
        return is_allowed or is_own_profile

    def get_queryset(self):
        if self.request.user.is_staff or self.request.user.is_superuser:
            return self.model.objects.all()
        return self.model.objects.filter(pk=self.request.user.pk)

    def handle_no_permission(self):
        messages.error(self.request, "You are not allowed to view this profile.")
        return redirect('index')