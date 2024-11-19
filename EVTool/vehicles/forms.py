from django import forms
from django.forms import ModelForm
from EVTool.vehicles.models import EVCar, EVBike, EVPhoto


class EVVehicleForm(ModelForm):

    class Meta:
        exclude = ('owner',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Disable all fields for the delete form, if needed
        if hasattr(self, 'disable_fields') and self.disable_fields:
            for field in self.fields.values():
                field.widget.attrs['disabled'] = True
                field.widget.attrs['readonly'] = True


# EVCar forms --------------------------------

class EVCarCreateForm(EVVehicleForm):
    class Meta(EVVehicleForm.Meta):
        model = EVCar


class EVCarChangeForm(EVVehicleForm):
    class Meta(EVVehicleForm.Meta):
        model = EVCar


class EVCarDeleteForm(EVVehicleForm):
    class Meta(EVVehicleForm.Meta):
        model = EVCar
        fields = '__all__'

    disable_fields = True


# EVBike forms --------------------------------

class EVBikeCreateForm(EVVehicleForm):
    class Meta(EVVehicleForm.Meta):
        model = EVBike


class EVBikeChangeForm(EVVehicleForm):
    class Meta(EVVehicleForm.Meta):
        model = EVBike


class EVBikeDeleteForm(EVVehicleForm):
    class Meta(EVVehicleForm.Meta):
        model = EVBike
        fields = '__all__'

    disable_fields = True


# EVPhoto forms --------------------------------
class EVPhotoCreateForm(ModelForm):
    class Meta:
        model = EVPhoto
        exclude = ['content_type', 'object_id',]


class EVPhotoEditForm(ModelForm):
    class Meta:
        model = EVPhoto
        fields = ['image', 'description']


class EVPhotoDeleteForm(ModelForm):
    class Meta:
        model = EVPhoto
        fields = '__all__'

    disable_fields = True

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['disabled'] = True
            field.widget.attrs['readonly'] = True
