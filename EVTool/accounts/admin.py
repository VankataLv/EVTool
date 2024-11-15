from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model

from EVTool.accounts.forms import AppUserCreationForm, AppUserChangeForm

UserModel = get_user_model()


@admin.register(UserModel)
class AppUserAdmin(UserAdmin):
    model = UserModel
    add_form = AppUserCreationForm
    form = AppUserChangeForm

    list_display = ('pk', 'username', 'email', 'is_staff', 'is_superuser', 'is_active', 'is_business')
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

