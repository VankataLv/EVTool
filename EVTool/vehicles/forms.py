from django.forms import ModelForm
from EVTool.vehicles.models import EVCar, EVBike
from EVTool.vehicles.models.ev_car_bike_photo import EVCarPhoto, EVBikePhoto


class EVVehicleForm(ModelForm):

    class Meta:
        exclude = ('owner',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
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


# EVPhotoCreate forms --------------------------------
class EVCarPhotoCreateForm(ModelForm):
    class Meta:
        model = EVCarPhoto
        fields = ['image', 'description',]


class EVBikePhotoCreateForm(ModelForm):
    class Meta:
        model = EVBikePhoto
        fields = ['image', 'description',]

# EVPhotoEdit forms --------------------------------


class EVCarPhotoEditForm(ModelForm):
    class Meta:
        model = EVCarPhoto
        fields = ['image', 'description']


class EVBikePhotoEditForm(ModelForm):
    class Meta:
        model = EVBikePhoto
        fields = ['image', 'description']


# EVPhotoDelete forms --------------------------------
class PhotoDeleteForm(ModelForm):
    disable_fields = True

    class Meta:
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['disabled'] = True
            field.widget.attrs['readonly'] = True


class EVCarPhotoDeleteForm(PhotoDeleteForm):
    class Meta(PhotoDeleteForm.Meta):
        model = EVCarPhoto


class EVBikePhotoDeleteForm(PhotoDeleteForm):
    class Meta(PhotoDeleteForm.Meta):
        model = EVBikePhoto
