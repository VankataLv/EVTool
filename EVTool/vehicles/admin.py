from django.contrib import admin
from django.contrib.admin import ModelAdmin

from EVTool.vehicles.forms import EVCarChangeForm, EVCarCreateForm
from EVTool.vehicles.models import EVCar, Municipality, Color, Brand, CarModel, EVPhoto, EVBike, BikeModel
from django.utils.html import mark_safe


@admin.register(EVCar)
class EvCarAdmin(ModelAdmin):
    add_form = EVCarCreateForm
    form = EVCarChangeForm

    list_display = ('pk', 'brand', 'model', 'owner', 'year',  'location', 'color', 'first_photo',)
    list_display_links = ('pk', 'brand', 'model', 'owner', 'year',  'location', 'color',)
    search_fields = ('owner__username', 'brand__name', 'model__name',)
    ordering = ('pk', 'brand', 'model', 'location',)
    list_filter = ('brand', 'year', 'color', )

    def first_photo(self, obj):
        first_photo = EVPhoto.objects.filter(content_type__model='evcar', object_id=obj.pk).first()
        if first_photo and first_photo.image:
            return mark_safe(f'<img src="{first_photo.image.url}" width="50" height="50" />')
        return '-'
    first_photo.short_description = 'First Photo'

@admin.register(Municipality)
class MunicipalityAdmin(ModelAdmin):
    list_display = ('pk', 'municipality_name')
    search_fields = ('municipality_name',)
    ordering = ('municipality_name',)


@admin.register(Color)
class ColorAdmin(ModelAdmin):
    list_display = ('pk', 'name')
    search_fields = ('name',)
    ordering = ('name',)


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'display_logo')
    search_fields = ('name',)
    ordering = ('name',)

    def display_logo(self, obj):
        if obj.logo:
            return mark_safe(f'<img src="{obj.logo.url}" style="height: 50px; width: auto;" />')
        return "No Logo"
    display_logo.short_description = "Logo"


@admin.register(CarModel)
class CarModelAdmin(ModelAdmin):
    list_display = ('pk', 'brand', 'name')
    search_fields = ('name',)
    ordering = ('brand__name', 'name',)
    list_filter = ('brand',)


# BIKES logic --------------------------------------------------
@admin.register(EVBike)
class EVBikeAdmin(admin.ModelAdmin):
    list_display = ('pk', 'brand', 'model', 'owner', 'year', 'location', 'color', 'body_type', 'first_photo',)
    list_display_links = ('pk', 'brand', 'model', 'owner', 'year', 'location', 'color',)
    search_fields = ('owner__username', 'brand__name', 'model__name',)
    ordering = ('pk', 'brand', 'model', 'location',)
    list_filter = ('brand', 'year', 'color', 'body_type',)

    def first_photo(self, obj):
        first_photo = EVPhoto.objects.filter(content_type__model='evbike', object_id=obj.pk).first()
        if first_photo and first_photo.image:
            return mark_safe(f'<img src="{first_photo.image.url}" width="50" height="50" />')
        return '-'
    first_photo.short_description = 'First Photo'


@admin.register(BikeModel)
class BikeModelAdmin(ModelAdmin):
    list_display = ('pk', 'brand', 'name')
    search_fields = ('name',)
    ordering = ('brand__name', 'name',)
    list_filter = ('brand',)


@admin.register(EVPhoto)
class EVPhotoAdmin(ModelAdmin):
    list_display = ('pk', 'related_object', 'image_display', 'description')
    search_fields = ('description', 'content_type__model',)
    ordering = ('content_type', 'object_id',)
    list_filter = ('content_type',)

    def related_object(self, obj):
        return str(obj.content_object)
    related_object.short_description = 'Related Object'

    def image_display(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="50" height="50" />')
        return '-'
    image_display.short_description = 'Image'
