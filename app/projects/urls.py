from django.urls import path

from projects import views

app_name = "projects"

urlpatterns = [
    path("list/", views.list_project, name="list_project"),
    path("create/<int:company_pk>/", views.create_project, name="create_project"),
    path("update/<int:project_pk>/", views.update_project, name="update_project"),
    path("delete/<int:project_pk>/", views.delete_project, name="delete_project"),
]
