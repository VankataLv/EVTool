from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.utils.html import mark_safe

from EVTool.vehicles.models import EVCar, Municipality, Color, Brand, CarModel, EVBike, BikeModel, EVBikePhoto, \
    EVCarPhoto


@admin.register(EVCar)
class EvCarAdmin(ModelAdmin):
    list_display = ('pk', 'brand', 'model', 'owner', 'year', 'location', 'color', 'first_photo',)
    list_display_links = ('pk', 'brand', 'model', 'owner', 'year', 'location', 'color',)
    search_fields = ('owner__username', 'brand__name', 'model__name',)
    ordering = ('pk', 'brand', 'model', 'location',)
    list_filter = ('owner__username', 'brand', 'year', 'color',)

    def first_photo(self, obj):
        first_photo = obj.car_photos.first()
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
    list_filter = ('owner__username', 'brand', 'year', 'color', 'body_type',)

    def first_photo(self, obj):
        first_photo = obj.bike_photos.first()
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


@admin.register(EVCarPhoto)
class EVCarPhotoAdmin(ModelAdmin):
    list_display = ('pk', 'related_object', 'image_display', 'description')
    search_fields = ('description',)
    ordering = ('car',)
    list_filter = ('car',)

    def related_object(self, obj):
        return str(obj.car)
    related_object.short_description = 'Related Vehicle'

    def image_display(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="50" height="50" />')
        return '-'
    image_display.short_description = 'Image'



@admin.register(EVBikePhoto)
class EVBikePhotoAdmin(ModelAdmin):
    list_display = ('pk', 'related_object', 'image_display', 'description')
    search_fields = ('description',)
    ordering = ('bike',)
    list_filter = ('bike',)

    def related_object(self, obj):
        return str(obj.bike)
    related_object.short_description = 'Related Vehicle'

    def image_display(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="50" height="50" />')
        return '-'
    image_display.short_description = 'Image'
