from django.urls import path

from companies import views

app_name = "companies"

urlpatterns = [
    path("list/", views.list_company, name="list_company"),
    path("search/list/", views.search_list_company, name="search_list_company"),
    path("list/create/", views.create_company, name="create_company"),
    path("list/<int:company_pk>/update/", views.update_company, name="update_company"),
    path("list/<int:company_pk>/", views.detail_company, name="detail_company"),
    path("list/<int:company_pk>/delete/", views.delete_company, name="delete_company"),
    path("csv/company/", views.csv_company, name="csv_company"),
]
