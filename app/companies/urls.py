from django.urls import path

from .views import list_company, update_create_company, delete_company, detail_company

app_name = 'companies'

urlpatterns = [
    path('list/', list_company, name='list_company_hx'),
    path('list/create/', update_create_company,
         name='create_company'),
    path('list/<int:company_id>/update/', update_create_company,
         name='update_company'),
    path('list/<int:company_id>/', detail_company, name='detail_company_hx'),
    path('list/<int:company_id>/delete/',
         delete_company, name='delete_company_hx'),
]
