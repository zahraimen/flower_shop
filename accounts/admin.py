from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, UserChangeForm
from .models import CustomUser


# Register your models here.
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = UserChangeForm
    model = CustomUser
    list_display = ['username', 'city', 'is_staff']
    fieldsets = UserAdmin.fieldsets + (

        (None, {'fields': ('city',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('city',)}),
    )


admin.site.register(CustomUser, CustomUserAdmin)
