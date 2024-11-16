from django import forms

from EVTool.vehicles.models import EVCar


class EVCarCreationForm(forms.ModelForm):
    class Meta:
        model = EVCar
        fields = '__all__'
        # labels = {
        #     'nickname': 'Nickname:',
        #     'first_name': 'First name:',
        #     'last_name': 'Last name:',
        #     'date_of_birth': 'DoB (YYYY-MM-DD):',
        #     'profile_picture': 'Profile picture:',
        # }


class EVCarChangeForm(forms.ModelForm):
    class Meta:
        model = EVCar
        fields = '__all__'
        # labels = {
        #     'nickname': 'Nickname:',
        #     'first_name': 'First name:',
        #     'last_name': 'Last name:',
        #     'date_of_birth': 'DoB (YYYY-MM-DD):',
        #     'profile_picture': 'Profile picture:',
        # }