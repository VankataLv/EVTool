from django.forms import ModelForm

from EVTool.services.models import Service


class ServiceCreateForm(ModelForm):
    class Meta:
        model = Service
        fields = ['name', 'text', 'area']

class ServiceEditForm(ModelForm):
    class Meta:
        model = Service
        fields = ['name', 'text', 'area']


class ServiceDeleteForm(ModelForm):
    class Meta:
        model = Service
        fields = ['name', 'text', 'area']
