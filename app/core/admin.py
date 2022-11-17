from django.contrib import admin
from django.contrib.auth.models import Group

from core.models import Sample

# admin.site.register(Sample)

# Register your models here.
admin.site.unregister(Group)
admin.site.site_header = "RPG Admin"
admin.site.site_title = "RPG Labs SAC"
# admin.site.site_url = 'http://127.0.0.1:8000/'
admin.site.index_title = "RPG Administración"
admin.empty_value_display = "**Empty**"
