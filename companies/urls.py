from django.urls import path

from .views import company_create, company_list

app_name = 'companies'

urlpatterns = [
    path('list/', company_list, name='company_list'),
    path('create/', company_create, name='company_create'),
]
