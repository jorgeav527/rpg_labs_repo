from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model

from .models import AdminProfile
USER = get_user_model()


@admin.register(USER)
class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'dni', 'is_staff',
                    'is_active', 'is_superuser', 'role', 'date_joined', 'last_login')
    list_filter = ('email', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {
            'fields': ('email', 'first_name', 'last_name', 'dni', 'password', 'role')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'dni', 'password1', 'password2', 'role')}),
        ('Permitions', {'fields': ('is_staff', 'is_active', 'is_superuser')}),
    )
    search_fields = ('email',)
    ordering = ('email',)


@ admin.register(AdminProfile)
class AdminProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'profession', 'cell_phone', 'created', 'updated')
