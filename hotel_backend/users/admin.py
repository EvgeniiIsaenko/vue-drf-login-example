from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import User

# Custom user creation panel 
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ("email", "first_name", "last_name", "is_staff",)
    list_filter = ("email", "is_staff",)
    fieldsets = (
        (None, {"fields": ("email", "first_name", "last_name", "password")}),
        ("Permissions", {"fields": ("is_staff", "groups", "user_permissions")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "email", "first_name", "last_name", "password1", "password2", "is_staff", "groups", "user_permissions"
            )}
        ),
    )
    search_fields = ("email",)
    ordering = ("email",)


admin.site.register(User, CustomUserAdmin)
