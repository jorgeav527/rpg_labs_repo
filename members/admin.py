from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model

from members.models import AdminProfile, ClientProfile

USER = get_user_model()


@admin.register(USER)
class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'dni', 'profession', 'cell_phone', 'is_staff',
                    'is_active', 'is_superuser', 'role', 'date_joined', 'last_login')
    list_filter = ('date_joined', 'is_staff',)
    fieldsets = (
        (None, {
            'fields': ('email', 'first_name', 'last_name', 'dni', 'profession', 'cell_phone', 'password', 'role')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'dni', 'profession', 'cell_phone', 'password1', 'password2', 'role')}),
        ('Permitions', {'fields': ('is_staff', 'is_active', 'is_superuser')}),
    )
    search_fields = ('email',)
    ordering = ('email',)


@ admin.register(AdminProfile)
class AdminProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'created', 'updated')


@ admin.register(ClientProfile)
class AdminProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'company', 'created', 'updated')
