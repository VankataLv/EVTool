from django import forms

from EVTool.vehicles.models import EVCar


class EVCarCreateForm(forms.ModelForm):
    class Meta:
        model = EVCar
        exclude = ('owner',)


class EVCarChangeForm(forms.ModelForm):
    class Meta:
        model = EVCar
        exclude = ('owner',)


class EVCarDeleteForm(forms.ModelForm):
    class Meta:
        model = EVCar
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs['disabled'] = True
            field.widget.attrs['readonly'] = True