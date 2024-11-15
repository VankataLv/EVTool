from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from EVTool.accounts.models import Profile

UserModel = get_user_model()


class AppUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = UserModel
        fields = ('username', 'email', 'password1', 'password2',)
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Enter your username'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter your email address'}),
        }
        labels = {
            'username': 'Username:',
            'email': 'Email:',
        }


class AppUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = UserModel


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user',]
        labels = {
            'nickname': 'Nickname:',
            'first_name': 'First name:',
            'last_name': 'Last name:',
            'date_of_birth': 'DoB (YYYY-MM-DD):',
            'profile_picture': 'Profile picture:',
        }