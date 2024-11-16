from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model

from EVTool.accounts.forms import AppUserCreationForm, AppUserChangeForm

UserModel = get_user_model()


from django.utils.html import format_html
from django.urls import reverse


@admin.register(UserModel)
class AppUserAdmin(UserAdmin):
    model = UserModel
    add_form = AppUserCreationForm
    form = AppUserChangeForm

    list_display = ('pk', 'username', 'email', 'is_staff', 'is_superuser', 'is_active', 'is_business', 'profile_link')
    search_fields = ('username',)
    ordering = ('pk', 'username')

    fieldsets = (
        ('Credentials', {'fields': ('username', 'password',)}),
        ('Personal info', {'fields': ('email',)}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_business', 'groups', 'user_permissions')}),
        ('Dates', {'fields': ('last_login',)}),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ('username', "email", "password1", "password2"),
            },
        ),
    )

    def profile_link(self, obj):
        if hasattr(obj, 'profile') and obj.profile:
            url = reverse('profile-details', kwargs={'pk': obj.profile.pk})
            profile_picture = obj.profile.profile_picture
            image_tag = format_html('<img src="{}" width="50" height="50" style="border-radius: 50%;"/>',
                                    profile_picture) if profile_picture else "No Picture"
            return format_html('{} <a href="{}"> / View Profile</a>', image_tag, url)
        return "No Picture / No Profile"

    profile_link.short_description = "Profile"


