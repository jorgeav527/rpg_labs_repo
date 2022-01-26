from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('core.urls', namespace='core')),
    path('members/', include('members.urls', namespace='members')),
    path('companies/', include('companies.urls', namespace='companies')),
    path('projects/', include('projects.urls', namespace='projects')),
    path('labs/', include('labs.urls', namespace='labs')),
    path('tests_labs/', include('tests_labs.urls', namespace='tests_labs')),
    path('admin/', admin.site.urls),
]
