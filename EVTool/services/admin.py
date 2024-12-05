from django.contrib import admin
from EVTool.services.models import Service
from django.utils.html import format_html


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'area', 'owner', 'profile_picture_tag', 'created_at', 'updated_at', 'slug')
    list_filter = ('area', 'created_at', 'updated_at', 'owner')
    search_fields = ('name', 'area', 'owner__username', 'slug')
    readonly_fields = ('created_at', 'updated_at', 'slug')
    ordering = ['-created_at']

    def profile_picture_tag(self, obj):
        if obj.owner.profile.profile_picture:
            return format_html(
                '<img src="{}" width="50" height="50" style="border-radius: 50%;"/>',
                obj.owner.profile.profile_picture.url
            )
        return "No Picture"

    profile_picture_tag.short_description = "Profile Picture"
