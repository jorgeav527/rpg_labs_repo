from django.urls import path
from django.contrib.auth.views import LoginView

from members.views import signup_admin, logout_request, login_request, list_client, update_create_signup_client, client_delete


app_name = 'members'

urlpatterns = [
    path('login/', login_request, name='login'),
    path('logout/', logout_request, name='logout'),
    # admin urls
    path('signup/admin/', signup_admin, name='signup_admin'),
    # clients urls
    path('client/list/', list_client, name='list_client_hx'),
    path('client/list/create/<int:company_id>/',
         update_create_signup_client, name='create_signup_client'),
    path('client/list/update/<int:user_id>/',
         update_create_signup_client, name='update_signup_client'),
    path('client/list/delete/<int:user_id>/',
         client_delete, name='client_delete_hx'),
]
