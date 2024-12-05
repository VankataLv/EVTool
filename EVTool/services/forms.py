from django.forms import ModelForm
from EVTool.services.models import Service


class ServiceBaseForm(ModelForm):
    class Meta:
        model = Service
        fields = ['name', 'text', 'area']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Disable fields for delete form
        if hasattr(self, 'disable_fields') and self.disable_fields:
            for field in self.fields.values():
                field.widget.attrs['disabled'] = True
                field.widget.attrs['readonly'] = True


class ServiceCreateForm(ServiceBaseForm):
    pass


class ServiceEditForm(ServiceBaseForm):
    pass


class ServiceDeleteForm(ServiceBaseForm):
    class Meta:
        model = Service
        fields = []

    disable_fields = True  # Disables form fields for delete action
    