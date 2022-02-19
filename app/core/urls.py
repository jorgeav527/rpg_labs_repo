from django.urls import path

from .views import home, blog_view, enrolling, requirement

app_name = 'core'

urlpatterns = [
    path('', home, name='home'),
    path('blog/', blog_view, name='blog'),
    path('registro/', enrolling, name='enrolling'),
    path('requerimiento/', requirement, name='requirement'),
]
