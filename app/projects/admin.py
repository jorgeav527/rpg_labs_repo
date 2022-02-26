from django.contrib import admin

from projects.models import Project


@ admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('company', 'name', 'location', 'created', 'updated')
