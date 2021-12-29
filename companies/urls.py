from django.urls import path

from .views import company_create_update, company_delete

app_name = 'companies'

urlpatterns = [
    path('list/create/', company_create_update, name='company_create'),
    path('list/<int:id>/update/', company_create_update, name='company_update'),
    path('list/<int:id>/delete/', company_delete, name='company_delete_hx'),
]
