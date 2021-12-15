from django.urls import path

from .views import home, blog_view

app_name = 'core'

urlpatterns = [
    path('', home, name='home'),
    path('blog/', blog_view, name='blog'),
]
