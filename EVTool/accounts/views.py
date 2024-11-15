from django.contrib import messages
from django.contrib.auth import get_user_model, login
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


# ------------------------ Profile Views -----------------------------


class ProfileDetailView(DetailView, UserPassesTestMixin):
    model = UserModel
    template_name = 'accounts/profile-details-page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.object

        return context

    def test_func(self):
        return self.request.user.pk == self.kwargs['pk']

    def get_queryset(self):
        # Limit the queryset to the logged-in user's profile
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
        return self.request.user == self.get_object().user

    def get_queryset(self):
        # Limit the queryset to the logged-in user's profile
        return self.model.objects.filter(pk=self.request.user.pk)

    def handle_no_permission(self):
        messages.error(self.request, "You are not allowed to view this profile.")
        return redirect('index')

class ProfileDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Profile
    template_name = 'accounts/profile-delete-page.html'
    success_url = reverse_lazy('index')

    def test_func(self):
        profile = self.get_object()
        return self.request.user == profile.user

    def get_queryset(self):
        return self.model.objects.filter(pk=self.request.user.pk)

    def handle_no_permission(self):
        messages.error(self.request, "You are not allowed to view this profile.")
        return redirect('index')