from django.urls import path

from projects.views import list_project, update_create_list_project, delete_project

app_name = 'projects'

urlpatterns = [
    path('list/', list_project, name='list_project_hx'),
    path('list/create/<int:company_id>/',
         update_create_list_project, name='create_project'),
    path('list/update/<int:project_id>/',
         update_create_list_project, name='update_project'),
    path('list/delete/<int:project_id>/',
         delete_project, name='delete_project_hx'),
]
