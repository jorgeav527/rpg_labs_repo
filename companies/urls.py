from django.urls import path

from .views import company_list_create_update, company_delete, company_detail, company_list

app_name = 'companies'

urlpatterns = [
    path('list/', company_list, name='company_list'),
    path('list/create/', company_list_create_update,
         name='company_list_create'),
    path('list/<int:id>/update/', company_list_create_update,
         name='company_list_update'),
    path('list/<int:id>/', company_detail, name='company_detail_hx'),
    path('list/<int:id>/delete/', company_delete, name='company_delete_hx'),
]
